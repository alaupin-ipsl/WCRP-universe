import json
import os
from pathlib import Path

import requests

# Directory of CMOR Table to retrieve variable_id
table_dir_url = "https://api.github.com/repos/PCMDI/cmip6-cmor-tables/contents/Tables"

# Directory where the JSON files will be saved
save_dir = "variable"

# Create the directory if it doesn't exist
os.makedirs(save_dir, exist_ok=True)


# Function to fetch and load JSON data from a URL
def fetch_json(url):
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors
    return response.json()


def process_variable(var_id, var_dict_from_table: dict) -> None:
    # print(var_dict_from_table)
    dict_to_save = {
        "@context": "000_context.jsonld",
        "id": var_id,
        "cmip_acronym": var_dict_from_table["out_name"],
        "long_name": var_dict_from_table["long_name"],
        "standard_name": var_dict_from_table["standard_name"],
        "type": "variable",
        "units": var_dict_from_table["units"],
        "drs_name": var_dict_from_table["out_name"],
    }
    if f"{var_id}.json" not in [p.name for p in Path(save_dir).iterdir()]:
        print(f"save {var_id}")
        with open(Path(save_dir) / f"{var_id}.json", "w") as f:
            json.dump(dict_to_save, f, indent=4)

    else:
        print(".")


variables_list = []
data = fetch_json(table_dir_url)
for item in data:
    json_data = fetch_json(item["download_url"])
    print(item["name"])
    # print(json_data.keys())
    if "variable_entry" in json_data.keys():
        for var in list(json_data["variable_entry"].keys()):
            process_variable(var, json_data["variable_entry"][var])
    else:
        if "variable_entry" in json_data[list(json_data.keys())[0]]:
            for var in list(json_data["variable_entry"].keys()):
                process_variable(var, json_data["variable_entry"][var])
