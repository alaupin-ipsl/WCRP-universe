
from pathlib import Path
import json

base_dir = Path("")

def load_data(term_path:Path):
    with open(term_path,"r") as f:
        data = json.load(f)
    return data

def save_data(data:dict, term_path:Path):
    with open(term_path,"w") as f:
        json.dump(data, f, indent=4)

def add_type(dir_path:Path):
 for term_path in (base_dir / dir_path).iterdir():
    # print(term_path)
    if term_path.suffix==".json":
        print(term_path)
        data = load_data(term_path)
        print(data)
        data["@context"] = "000_context.jsonld"
        save_data(data,term_path)


add_type(Path("area_label"))
add_type(Path("temporal_label"))
add_type(Path("horizontal_label"))
add_type(Path("vertical_label"))
add_type(Path("branded_suffix"))
add_type(Path("branded_variable"))
