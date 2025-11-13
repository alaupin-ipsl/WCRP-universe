import json
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)
OUTPUT_DIR = Path("./region")  # the script need to be run from root repo dir !

# script path
script_dir = Path(__file__).resolve().parent
LOCAL_CV_DIR = script_dir / "./original_CVs"

filename = "obs4MIPs_region.json"
source_path = LOCAL_CV_DIR / filename
assert isinstance(source_path, Path)

with open(source_path, "r", encoding="utf-8") as f:
    source_data = json.load(f)

for term in source_data["region"]:
    term_data = {
        "@context": "000_context.jsonld",
        "id": term.lower(),
        "type": "region",  # here we have to tell the type from Universe DD to get the pydantic in esgvoc
        "drs_name": term,  # mandatory to get esgvoc plain term working
        "description": "",
    }

    # Write term file
    term_path = OUTPUT_DIR / f"{term.lower()}.json"
    with open(term_path, "w", encoding="utf-8") as f:
        print("create", term_path)
        json.dump(term_data, f, indent=4)
