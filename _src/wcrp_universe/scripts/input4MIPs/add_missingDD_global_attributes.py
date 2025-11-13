import json
import os

json_file = (
    "_src/wcrp_universe/scripts/input4MIPs/original_CVs/input4MIPs_db_file_entries.json"
)


def extract_unique_field_ids(field: str, json_file_path: str):
    """Extract unique variable_id values from JSON database."""
    with open(json_file_path, "r") as f:
        data = json.load(f)

    res = set()
    for entry in data:
        if field in entry:
            if entry[field] is not None:
                res.add(entry[field])

    return sorted(list(res))


def create_convention_terms(ids: list, output_dir: str) -> None:
    """Create individual JSON files for each conventions."""
    os.makedirs(output_dir, exist_ok=True)

    for term in ids:
        json_content = {
            "@context": "000_context.jsonld",
            "id": term.lower().replace(" ", "_"),
            "label": term,
            "type": "conventions",
            "drs_name": term,
            "description": "",
        }

        filename = f"{json_content['id']}.json"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, "w") as f:
            json.dump(json_content, f, indent=4)

        print(f"Created: {filepath}")


def create_region_terms(ids: list, output_dir: str) -> None:
    """Create individual JSON files for each region."""
    os.makedirs(output_dir, exist_ok=True)

    for term in ids:
        json_content = {
            "@context": "000_context.jsonld",
            "id": term.lower(),
            "label": term,
            "type": "region",
            "drs_name": term,
            "description": "",
        }

        filename = f"{json_content['id']}.json"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, "w") as f:
            json.dump(json_content, f, indent=4)

        print(f"Created: {filepath}")


if __name__ == "__main__":
    allconventions = extract_unique_field_ids("Conventions", json_file)
    create_convention_terms(allconventions, "conventions")

    allvalues = extract_unique_field_ids("region", json_file)
    print(allvalues)
    create_region_terms(allvalues, "region")
