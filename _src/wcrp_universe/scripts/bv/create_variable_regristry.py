#!/usr/bin/env python3

import json
import logging
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

from dotenv import load_dotenv
from pyairtable import Api
from pydantic import Field, ValidationError
from wcrp_universe.models.data_descriptor import PlainTermDataDescriptor

# Load environment variables
load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class KnownBrandedVariable(PlainTermDataDescriptor):
    """
    A climate-related quantity or measurement, including information about sampling.

    The concept of a branded variable was introduced in CMIP7.
    A branded variable is composed of two parts.
    The first part is the root variable (see :py:class:`Variable`).
    The second is the suffix (see :py:class:`BrandedSuffix`).

    For further details on the development of branded variables,
    see [this paper draft](https://docs.google.com/document/d/19jzecgymgiiEsTDzaaqeLP6pTvLT-NzCMaq-wu-QoOc/edit?pli=1&tab=t.0).
    """

    # CF Standard Name context (flattened from hierarchy)
    cf_standard_name: str = Field(
        description="CF standard name, e.g., 'air_temperature'"
    )
    cf_units: str = Field(description="CF standard units, e.g., 'K'")
    cf_sn_status: str = Field(description="CF standard name status, e.g., 'approved'")

    # Variable Root context (flattened from hierarchy)
    variable_root_name: str = Field(description="Variable root name, e.g., 'ta'")
    var_def_qualifier: str = Field(
        default="", description="Variable definition qualifier"
    )
    branding_suffix_name: str = Field(
        description="Branding suffix, e.g., 'tavg-p19-hxy-air'"
    )

    # Variable metadata
    description: str = Field(description="Human-readable description")
    dimensions: List[str] = Field(description="NetCDF dimensions")
    cell_methods: str = Field(default="", description="CF cell_methods attribute")
    cell_measures: str = Field(default="", description="CF cell_measures attribute")
    history: str = Field(default="", description="Processing history")
    realm: str = Field(description="Earth system realm, e.g., 'atmos'")

    # Label components (embedded, not references)
    temporal_label: str = Field(description="Temporal label, e.g., 'tavg'")
    vertical_label: str = Field(description="Vertical label, e.g., 'p19'")
    horizontal_label: str = Field(description="Horizontal label, e.g., 'hxy'")
    area_label: str = Field(description="Area label, e.g., 'air'")

    # Status
    bn_status: str = Field(description="Branded variable status, e.g., 'accepted'")

    # Additional required fields from specifications
    positive_direction: str = Field(
        default="", description="Positive direction for the variable"
    )


class AirtableVariableClient:
    """Client for interacting with Airtable variable data."""

    def __init__(self, api_key: str, base_id: str, table_name: str = "variable"):
        """
        Initialize the Airtable client.

        Args:
            api_key: Airtable API key
            base_id: Airtable base ID
            table_name: Name of the table containing variable data
        """
        self.api = Api(api_key)
        self.base_id = base_id
        self.table = self.api.table(base_id, table_name)
        self._linked_record_cache = {}

    def fetch_all_records(self, max_records: int = None) -> List[Dict[str, Any]]:
        """
        Fetch all records from the Airtable with pagination support.

        Args:
            max_records: Maximum number of records to fetch (None for all)

        Returns:
            List of records from the table
        """

        try:
            # Use pyairtable's built-in pagination with limit
            if max_records:
                all_records = self.table.all(max_records=max_records)
            else:
                all_records = self.table.all()
            return all_records

        except Exception as e:
            raise

    def resolve_linked_record(
        self, record_id: str, table_name: str, field_name: str = "Name"
    ) -> Optional[str]:
        """
        Resolve a linked record ID to get the actual value.

        Args:
            record_id: The Airtable record ID to resolve
            table_name: The name of the table containing the linked record
            field_name: The field name to extract from the linked record

        Returns:
            The resolved value or None if not found
        """
        cache_key = f"{table_name}:{record_id}:{field_name}"

        # Check cache first
        if cache_key in self._linked_record_cache:
            return self._linked_record_cache[cache_key]

        try:
            linked_table = self.api.table(self.base_id, table_name)
            record = linked_table.get(record_id)

            # Try different possible field names based on table type
            if table_name == "Cell Methods":
                possible_fields = [
                    "Cell Methods",
                    field_name,
                    "Name",
                    "Title",
                    "Value",
                    "Label",
                ]
            elif table_name == "Cell Measures":
                possible_fields = [
                    "Cell Measures",
                    field_name,
                    "Name",
                    "Title",
                    "Value",
                    "Label",
                ]
            else:
                possible_fields = [field_name, "Name", "Title", "Value", "Label"]

            for field in possible_fields:
                if field in record["fields"]:
                    value = record["fields"][field]
                    self._linked_record_cache[cache_key] = value
                    return value

            self._linked_record_cache[cache_key] = record_id
            return record_id

        except Exception:
            self._linked_record_cache[cache_key] = None
            return None

    def resolve_linked_records_list(
        self, record_ids: List[str], table_name: str, field_name: str = "Name"
    ) -> List[str]:
        """
        Resolve a list of linked record IDs.

        Args:
            record_ids: List of Airtable record IDs to resolve
            table_name: The name of the table containing the linked records
            field_name: The field name to extract from the linked records

        Returns:
            List of resolved values
        """
        resolved = []
        for record_id in record_ids:
            value = self.resolve_linked_record(record_id, table_name, field_name)
            if value:
                resolved.append(value)
        return resolved


class VariableDataMapper:
    """Maps Airtable data to KnownBrandedVariable model."""

    def __init__(self, airtable_client: AirtableVariableClient):
        """Initialize with an Airtable client for resolving linked records."""
        self.client = airtable_client

    def map_airtable_to_model(
        self, record: Dict[str, Any]
    ) -> Optional[KnownBrandedVariable]:
        """
        Map an Airtable record to KnownBrandedVariable model.

        Args:
            record: Airtable record dictionary

        Returns:
            KnownBrandedVariable instance or None if mapping fails
        """
        try:
            fields = record.get("fields", {})

            def get_field(field_name: str, default: Any = "") -> Any:
                value = fields.get(field_name, default)
                return value if value is not None else default

            def resolve_linked_field(
                field_name: str, table_name: str, field_to_extract: str = "Name"
            ) -> str:
                linked_ids = get_field(field_name, [])
                if isinstance(linked_ids, list) and linked_ids:
                    return (
                        self.client.resolve_linked_record(
                            linked_ids[0], table_name, field_to_extract
                        )
                        or ""
                    )
                return ""

            branded_variable_name = get_field("Branded Variable Name", "")
            if not branded_variable_name:
                return None

            # Parse dimensions
            dimensions_raw = get_field("Dimensions", "")
            if isinstance(dimensions_raw, str) and dimensions_raw:
                dimensions = [
                    dim.strip() for dim in dimensions_raw.split(",") if dim.strip()
                ]
            else:
                dimensions = []

            # Resolve linked fields
            cf_standard_name = ""
            cf_units = ""
            physical_param_ids = get_field("Physical Parameter", [])
            if physical_param_ids:
                cf_standard_name_ids = get_field(
                    "CF Standard Name (from Physical Parameter)", []
                )
                if cf_standard_name_ids:
                    cf_standard_name = (
                        self.client.resolve_linked_record(
                            cf_standard_name_ids[0], "CF Standard Names", "Name"
                        )
                        or ""
                    )

                units_ids = get_field("Units (from Physical Parameter)", [])
                if units_ids:
                    cf_units = (
                        str(units_ids[0])
                        if isinstance(units_ids[0], str)
                        and not units_ids[0].startswith("rec")
                        else ""
                    )

            # Resolve realm - use ID field instead of Name
            realm = resolve_linked_field(
                "Modelling Realm - Primary", "Modelling Realm", "id"
            )

            # Resolve cell methods and measures
            cell_methods = resolve_linked_field(
                "Cell Methods", "Cell Methods", "Cell Methods"
            )
            cell_measures = resolve_linked_field(
                "Cell Measures", "Cell Measures", "Name"
            )

            # Extract labels from branded variable name (simplified approach)
            branded_parts = branded_variable_name.split("_")
            variable_root_name = branded_parts[0] if branded_parts else ""
            branding_suffix = (
                "_".join(branded_parts[1:]) if len(branded_parts) > 1 else ""
            )

            # Parse branding suffix for labels (format: temporal-vertical-horizontal-area)
            suffix_parts = branding_suffix.split("-") if branding_suffix else []
            temporal_label = suffix_parts[0] if len(suffix_parts) > 0 else ""
            vertical_label = suffix_parts[1] if len(suffix_parts) > 1 else ""
            horizontal_label = suffix_parts[2] if len(suffix_parts) > 2 else ""
            area_label = suffix_parts[3] if len(suffix_parts) > 3 else ""

            # Create the model instance
            variable = KnownBrandedVariable(
                # ESGVoc required fields (from PlainTermDataDescriptor)
                id=branded_variable_name,
                type="known_branded_variable",
                drs_name=branded_variable_name,
                # CF Standard Name context
                cf_standard_name=cf_standard_name,
                cf_units=cf_units,
                cf_sn_status="approved" if cf_standard_name else "pending",
                # Variable Root context
                variable_root_name=variable_root_name,
                var_def_qualifier="",
                branding_suffix_name=branding_suffix,
                # Variable metadata
                description=get_field("Description", ""),
                dimensions=dimensions,
                cell_methods=cell_methods,
                cell_measures=cell_measures,
                history="",
                realm=realm,
                # Label components
                temporal_label=temporal_label,
                vertical_label=vertical_label,
                horizontal_label=horizontal_label,
                area_label=area_label,
                # Status
                bn_status=get_field("Branded Variable Name status", "pending"),
                positive_direction="",
            )

            return variable

        except (ValidationError, Exception):
            return None


class JSONFileGenerator:
    """Generates JSON files from KnownBrandedVariable instances."""

    def __init__(self, output_dir: Path):
        """
        Initialize the JSON file generator.

        Args:
            output_dir: Directory where JSON files will be saved
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate_json_file(self, variable: KnownBrandedVariable) -> bool:
        """
        Generate a JSON file for a single variable.

        Args:
            variable: KnownBrandedVariable instance

        Returns:
            True if successful, False otherwise
        """
        try:
            # Use the variable ID as filename
            filename = f"{variable.id}.json"
            filepath = self.output_dir / filename

            # Convert to dictionary and save as JSON
            variable_dict = variable.model_dump()
            variable_dict["@context"] = "000_context.jsonld"
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(variable_dict, f, indent=2, ensure_ascii=False)

            return True

        except Exception:
            return False

    def generate_all_files(self, variables: List[KnownBrandedVariable]) -> int:
        """
        Generate JSON files for all variables.

        Args:
            variables: List of KnownBrandedVariable instances

        Returns:
            Number of successfully generated files
        """
        success_count = 0

        for variable in variables:
            if self.generate_json_file(variable):
                success_count += 1

        return success_count


def main():
    """Main execution function."""
    # Configuration
    API_KEY = os.getenv("AIRTABLE_API_KEY")
    BASE_ID = os.getenv("AIRTABLE_BASE_ID")
    TABLE_NAME = os.getenv("AIRTABLE_TABLE_NAME", "variable")
    OUTPUT_DIR = Path("known_branded_variable")

    # Validate configuration
    if not API_KEY:
        return 1

    if not BASE_ID:
        return 1

    try:
        # Initialize components

        # Step 1: Initialize Airtable client
        airtable_client = AirtableVariableClient(API_KEY, BASE_ID, TABLE_NAME)

        # Step 2: Fetch all records
        records = airtable_client.fetch_all_records()

        # Step 3: Map records to model instances
        mapper = VariableDataMapper(airtable_client)
        variables = []

        for record in records:
            variable = mapper.map_airtable_to_model(record)
            if variable:
                variables.append(variable)

        # Step 4: Generate JSON files
        json_generator = JSONFileGenerator(OUTPUT_DIR)
        success_count = json_generator.generate_all_files(variables)

        return 0

    except Exception as e:
        return 1


if __name__ == "__main__":
    exit(main())
