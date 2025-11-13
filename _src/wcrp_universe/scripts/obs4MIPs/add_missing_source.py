#!/usr/bin/env python3
"""
Converter for the source_id collection.
Converts input4MIPs_source_id.json to ESGVOC format.
"""

import json
import logging
import os
from pathlib import Path

import requests

# Setup logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


"""

activity_participation: list[str] | None
cohort: list[str] = Field(default_factory=list)
organisation_id: list[str] = Field(default_factory=list)
label: str
label_extended: Optional[str] = None
license: dict = Field(default_factory=dict)
model_component: Optional[dict] = None
release_year: Optional[int] = None
"""
# URLs of the JSON files on GitHub
json_url = "https://raw.githubusercontent.com/PCMDI/obs4MIPs-cmor-tables/refs/heads/master/obs4MIPs_source_id.json"

# Directory where the JSON files will be saved
save_dir = Path("source")

# Create the directory if it doesn't exist
os.makedirs(save_dir, exist_ok=True)


# Function to fetch and load JSON data from a URL
def fetch_json(url):
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors
    return response.json()


data = fetch_json(json_url)

for term, dic in data["source_id"].items():
    term_data = {
        "@context": "000_context.jsonld",
        "id": term.lower(),
        "type": "source",  # here we have to tell the type from Universe DD to get the pydantic in esgvoc
        "drs_name": term,  # mandatory to get esgvoc plain term working
        "activity_participation": ["obs4mips"],
        "cohort": [],
        "organisation_id": [],
        "label": dic["source_label"],
        "label_extended": dic["source_description"],
        "license": {},
        "model_component": None,
        "release_year": None,
    }

    # Write term file
    term_path = save_dir / f"{term.lower()}.json"
    print(term_path)
    if not term_path.exists():
        with open(term_path, "w", encoding="utf-8") as f:
            print("create", term_path)
            json.dump(term_data, f, indent=4)
