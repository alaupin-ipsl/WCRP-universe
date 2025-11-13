# the idea is to modify type of all variable cause for now the type is the more the technical type of the variable (real, float, integer)
# but need to be of type of the datadescriptor they are in ("variable")
# run this script from root of WCRP-Universe

from pathlib import Path
import json


variable_dir = Path("variable")

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
        if data["type"] != "variable":
            data["variable_type"]=data["type"]
            data["type"] = "variable"
        save_data(data,term_path)

