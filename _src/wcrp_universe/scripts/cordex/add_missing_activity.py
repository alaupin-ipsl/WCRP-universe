#!/usr/bin/env python3
"""
Converter for the activity_id collection.
Converts CORDEX-CMIP6_activity_id.json to ESGVOC format.
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
OUTPUT_DIR = Path("./activity")  # the script need to be run from root repo dir !

# URLs of the JSON files on GitHub
json_url = "https://raw.githubusercontent.com/WCRP-CORDEX/cordex-cmip6-cv/refs/heads/main/CORDEX-CMIP6_activity_id.json"

# Function to fetch and load JSON data from a URL
def fetch_json(url):
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors
    return response.json()

print(fetch_json(json_url))

activity_data = fetch_json(json_url)

for key, value in activity_data["activity_id"].items():
    term_data = {
        '@context': "000_context.jsonld",
        'type':'activity',
        'id': key.lower(),
        'name': key,
        'cmip_acronym': key,
        'long_name': value,
        'url': None,
        'drs_name': key,
    }

    # Write term file
    term_path = OUTPUT_DIR / f"{key.lower()}.json"
    with open(term_path, "w", encoding="utf-8") as f:
        print("create", term_path)
        json.dump(term_data, f, indent=4)
