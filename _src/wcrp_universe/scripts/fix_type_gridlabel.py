# the idea is to modify type of all grid cause for now the type is grid-label 
# but need to be of type of the datadescriptor they are in ("grid")
# run this script from root of WCRP-Universe

from pathlib import Path
import json


variable_dir = Path("grid")

def load_data(term_path:Path):
    with open(term_path,"r") as f:
        data = json.load(f)
    return data

def save_data(data:dict, term_path:Path):
    with open(term_path,"w") as f:
        json.dump(data, f, indent=4)

for term_path in variable_dir.iterdir():
    # print(term_path)
    if term_path.suffix==".json":
        #print(term_path)
        data = load_data(term_path)
        print(data)
        if data["type"] != "grid":
            data["type"] = "grid"
        save_data(data,term_path)

