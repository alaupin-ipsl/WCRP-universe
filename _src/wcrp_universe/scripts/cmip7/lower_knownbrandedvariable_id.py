"""
Generate branded_variables entries
"""

import json
import os
from pathlib import Path


def main():
    repo_root = Path(__file__).parents[4]
    print(repo_root)
    include_from = repo_root / "known_branded_variable"

    for src_file in include_from.glob("*.json"):
        with src_file.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
        id = src_file.stem.lower()
        if src_file.stem != id and data["id"] != id:
            data["id"] = id

            out_file = f"{include_from}/{id}.json"
            with open(out_file, "w") as fh:
                json.dump(data, fh, indent=2)
            
            os.remove(src_file)

            print(f"Wrote {out_file}")


if __name__ == "__main__":
    main()
