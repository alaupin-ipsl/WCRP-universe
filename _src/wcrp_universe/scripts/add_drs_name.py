# The idea is to add the key:value "drs_name" to all terms that appears in DRS
# The DRS is not only the filename,dataset, directory , it is also the global attribute
# therefore need to change that : the key drs_name need to appears in ALL plain_term
# at this point .. the drs_name will be the current id .. for those taht doesnt have drs_name yet (fev 2025)


import json
from pathlib import Path

base_dir = Path("")


def load_data(term_path: Path):
    with open(term_path, "r") as f:
        data = json.load(f)
    return data


def save_data(data: dict, term_path: Path):
    with open(term_path, "w") as f:
        json.dump(data, f, indent=4)


def add_drs(dir_path: Path, key: str):
    for term_path in (base_dir / dir_path).iterdir():
        # print(term_path)
        if term_path.suffix == ".json":
            print(term_path)
            data = load_data(term_path)
            print(data)
            data["drs_name"] = data[key].upper()
            save_data(data, term_path)


# add_drs(Path("activity"),"cmip_acronym")
# add_drs(Path("consortia"),"cmip-acronym")
# add_drs(Path("experiment"),"experiment_id")
# add_drs(Path("grid"),"name")
# add_drs(Path("institution"),"cmip-acronym")
# add_drs(Path("mip_era"),"name")
# add_drs(Path("model_component"),"name")
add_drs(Path("source"), "id")
# add_drs(Path("sub_experiment"),"id")
# add_drs(Path("table"),"id")
# add_drs(Path("variable"),"cmip_acronym")

# Plainterm taht doesnt appears in DRS (filename,dataset,directory)
# add_drs(Path("frequency"),"id")
# add_drs(Path("product"),"id")
# add_drs(Path("resolution"),"id")
# add_drs(Path("source_type"),"id")
# add_drs(Path("license"),"id")

# add_drs(Path("realm"),"id")
# add_drs(Path("area_label"),"label")
# add_drs(Path("horizontal_label"),"label")
# add_drs(Path("temporal_label"),"label")

# add_drs(Path("organisation"),"id")
