#!/usr/bin/env python3
"""
Converter for the source_id collection.
Converts CORDEX-CMIP6_source_id.json to ESGVOC format.
"""

import json
import logging
from pathlib import Path

import requests

# Setup logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)
OUTPUT_DIR = Path("./source")  # the script need to be run from root repo dir !

# URLs of the JSON files on GitHub
json_url = "https://raw.githubusercontent.com/WCRP-CORDEX/cordex-cmip6-cv/refs/heads/main/CORDEX-CMIP6_source_id.json"

# Function to fetch and load JSON data from a URL
def fetch_json(url):
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors
    return response.json()

print(fetch_json(json_url))

source_data = fetch_json(json_url)

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


for term, dic in source_data["source_id"].items():
    term_data = {
        "@context": "000_context.jsonld",
        "id": term.lower(),
        "type": "source",  # here we have to tell the type from Universe DD to get the pydantic in esgvoc
        "drs_name": term,  # mandatory to get esgvoc plain term working
        "activity_participation": dic["activity_participation"],
        "cohort": dic["cohort"],
        "organisation_id": dic["institution_id"],
        "label": dic["label"],
        "label_extended": dic["label_extended"],
        "license": {},
        "model_component": None,
        "release_year": dic["release_year"],
    }

    # Write term file
    term_path = OUTPUT_DIR / f"{term.lower()}.json"
    with open(term_path, "w", encoding="utf-8") as f:
        print("create", term_path)
        json.dump(term_data, f, indent=4)
