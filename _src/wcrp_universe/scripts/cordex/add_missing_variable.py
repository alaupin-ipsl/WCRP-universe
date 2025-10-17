#!/usr/bin/env python3
"""
Converter for the domain_id collection.
Converts CORDEX-CMIP6_domain_id.json to ESGVOC format.
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
OUTPUT_DIR = Path("./variable")  # the script need to be run from root repo dir !

# URLs of the JSON files on GitHub
# Clone or download the repo to have local access at : https://github.com/WCRP-CORDEX/cordex-cmip6-cmor-tables
json_folder = "_src/wcrp_universe/scripts/cordex/cordex-cmip6-cmor-tables/Tables"
# Create the directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)
print(Path(json_folder))
json_files = [f for f in Path(json_folder).glob("*.json")]
print(json_files)

for json_file in json_files:
    print(json_file)
    print("Processing file:", json_file)
    with open(json_file, "r") as f:
        try:
            raw_data = json.load(f)
        except json.JSONDecodeError:
            print(f"Erreur de lecture JSON pour {json_file}, fichier ignoré")
            continue

    data = raw_data.get("variable_entry")

    if data is None:
        print(f"{json_file} n'a pas de clé 'variable_entry', fichier ignoré")
        continue

    for term, dic in data.items():
        term_data = {
            "@context": "000_context.jsonld",
            "id": term.lower(),
            "cmip_acronym": term,
            "long_name": dic["long_name"],
            "standard_name": dic["standard_name"],
            "type": "variable",
            "units": dic["units"],
            "drs_name": term,
        }

        # Write term file
        term_path = OUTPUT_DIR / f"{term.lower()}.json"
        with open(term_path, "w", encoding="utf-8") as f:
            print("create", term_path)
            json.dump(term_data, f, indent=4)
