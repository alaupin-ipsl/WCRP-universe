#!/usr/bin/env python3
"""
Converter for the domain_id collection.
Converts CORDEX-CMIP6_domain_id.json to ESGVOC format.
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
OUTPUT_DIR = Path("./region")  # the script need to be run from root repo dir !

# URLs of the JSON files on GitHub
json_url = "https://raw.githubusercontent.com/WCRP-CORDEX/cordex-cmip6-cv/refs/heads/main/CORDEX-CMIP6_domain_id.json"

# Function to fetch and load JSON data from a URL
def fetch_json(url):
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors
    return response.json()

print(fetch_json(json_url))

domain_data = fetch_json(json_url)

for term, dic in domain_data["domain_id"].items():
    term_data = {
        "@context": "000_context.jsonld",
        "id": term.lower(),
        "type": "region",  # here we have to tell the type from Universe DD to get the pydantic in esgvoc
        "drs_name": term,  # mandatory to get esgvoc plain term working
        "description": dic["domain"],
    }

    # Write term file
    term_path = OUTPUT_DIR / f"{term.lower()}.json"
    with open(term_path, "w", encoding="utf-8") as f:
        print("create", term_path)
        json.dump(term_data, f, indent=4)
