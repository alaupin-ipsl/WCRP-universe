import json
import os
from pathlib import Path
from pprint import pprint

import requests

# Directory of CMOR Table to retrieve variable_id
table_dir_url = (
    "https://api.github.com/repos/PCMDI/obs4MIPs-cmor-tables/contents/Tables"
)

# Directory where the JSON files will be saved
save_dir = "variable"

# Create the directory if it doesn't exist
os.makedirs(save_dir, exist_ok=True)


known_variables_in_universe = []
for file in Path(save_dir).iterdir():
    known_variables_in_universe.append(file.name.split(".")[0])


# Function to fetch and load JSON data from a URL
def fetch_json(url):
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors
    return response.json()


var_to_create = {}
data = fetch_json(table_dir_url)
for item in data:
    print(item["name"])
    skip = ["obs4MIPs_coordinate.json", "obs4MIPs_grids.json"]
    if item["name"] in skip:
        continue
    json_data = fetch_json(item["download_url"])
    var_dict = []
    if "variable_entry" in json_data.keys():
        vars_dict = json_data["variable_entry"]

    else:
        if "variable_entry" in json_data[list(json_data.keys())[0]]:
            vars_dict = json_data[list(json_data.keys())[0]]["variable_entry"]

    for var_id, var_data in vars_dict.items():
        if var_id not in known_variables_in_universe:
            print(f"Must create {var_id}")
            if var_id not in var_to_create.keys():
                var_to_create[var_id] = [var_data]
            else:
                var_to_create[var_id].append(var_data)


def all_dicts_equal_verbose(dicts):
    if not dicts:
        print("The list of dicts is empty.")
        return True  # or False, depending on how you want to handle empty lists

    ref = dicts[0]
    for i, d in enumerate(dicts[1:], start=1):
        if d != ref:
            keys = ref.keys() | d.keys()
            diffs = {
                k: (ref.get(k, "<missing>"), d.get(k, "<missing>"))
                for k in keys
                if ref.get(k) != d.get(k)
            }
            print(f"Dict at index {i} differs: {diffs}")
            return False
    print("All dicts are equal.")
    return True


for var_id, var_data_list in var_to_create.items():
    # if len(var_data_list) >= 2:
    #     print(var_id)
    #     all_dicts_equal_verbose(var_data_list) # only sfcWind long_name differs depending on frequency, just take the first one is good
    create_file_data = {
        "@context": "000_context.jsonld",
        "id": var_id,
        "cmip_acronym": var_id,
        "long_name": var_data_list[0]["long_name"],
        "standard_name": var_data_list[0]["standard_name"],
        "type": "variable",
        "units": var_data_list[0]["units"],
        "drs_name": var_id,
    }
    print(create_file_data)

    with open(Path(save_dir) / f"{var_id}.json", "w") as f:
        json.dump(create_file_data, f, indent=4)
