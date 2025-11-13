#!/usr/bin/env python3
"""
Converter for the dataset_category collection.
Converts input4MIPs_dataset_category.json to ESGVOC format.
"""

import json
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)
OUTPUT_DIR = Path("./realm")  # the script need to be run from root repo dir !
# script path
script_dir = Path(__file__).resolve().parent
LOCAL_CV_DIR = script_dir / "./original_CVs"


def get_cv_path(collection_name: str) -> Path | None:
    """
    Get the local path to a CV file.

    Args:
        collection_name: Name of the collection (e.g., 'activity_id')

    Returns:
        Path to the local CV file, or None if the file doesn't exist
    """
    filename = f"input4MIPs_{collection_name}.json"
    file_path = LOCAL_CV_DIR / filename

    if not file_path.exists():
        logger.warning(f"CV file not found: {file_path}")
        return None

    return file_path


def convert() -> None:
    """Convert source_id collection to ESGVOC format."""
    # Define collection name
    collection_name = "dataset_category"

    try:
        # Ensure the CV file is available locally
        filename = f"input4MIPs_{collection_name}.json"
        source_path = get_cv_path(collection_name)
        if not source_path or not source_path.exists():
            logger.info(f"Fetching {filename} from GitHub...")
            source_path = get_cv_path(filename)

        # Read source file
        assert isinstance(source_path, Path)
        with open(source_path, "r", encoding="utf-8") as f:
            source_data = json.load(f)

        # Create term files for each source ID
        for term_id in source_data:
            # Use lowercase for id

            # Create term file
            term_data = {
                "@context": "000_context.jsonld",
                "id": term_id.lower(),
                "type": "realm",  # here we have to tell the type from Universe DD to get the pydantic in esgvoc
                "drs_name": term_id,  # mandatory to get esgvoc plain term working
                "name": term_id,
                "description": "",
            }

            # Write term file
            term_path = OUTPUT_DIR / f"{term_id.lower()}.json"
            with open(term_path, "w", encoding="utf-8") as f:
                json.dump(term_data, f, indent=4)

            logger.info(f"Created term file: {term_path}")

        logger.info(f"Successfully converted {collection_name} collection")

    except Exception as e:
        logger.error(f"Error converting {collection_name}: {str(e)}")
        raise


if __name__ == "__main__":
    convert()
