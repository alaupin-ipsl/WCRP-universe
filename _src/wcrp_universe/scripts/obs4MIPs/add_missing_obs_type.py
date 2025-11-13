#!/usr/bin/env python3
"""
Converter for the source_id collection.
Converts input4MIPs_source_id.json to ESGVOC format.
"""

import json
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)
OUTPUT_DIR = Path("./obs_type")  # the script need to be run from root repo dir !
# script path
script_dir = Path(__file__).resolve().parent
LOCAL_CV_DIR = script_dir / "./original_CVs"

filename = "obs4MIPs_source_type.json"
source_path = LOCAL_CV_DIR / filename
assert isinstance(source_path, Path)

with open(source_path, "r", encoding="utf-8") as f:
    source_data = json.load(f)
"""

activity_participation: list[str] | None
cohort: list[str] = Field(default_factory=list)
organisation_id: list[str] = Field(default_factory=list)
label: str
label_extended: Optional[str] = None
license: dict = Field(default_factory=dict)
model_component: Optional[dict] = None
release_year: Optional[int] = None
"""


for term, desc in source_data["source_type"].items():
    term_data = {
        "@context": "000_context.jsonld",
        "id": term.lower(),
        "type": "obs_type",  # here we have to tell the type from Universe DD to get the pydantic in esgvoc
        "drs_name": term,  # mandatory to get esgvoc plain term working
        "description": desc,
    }

    # Write term file
    term_path = OUTPUT_DIR / f"{term.lower()}.json"
    with open(term_path, "w", encoding="utf-8") as f:
        print("create", term_path)
        json.dump(term_data, f, indent=4)
