"""
Generate ScenarioMIP experiment names
"""

import json


def get_tier(experiment: str) -> int:
    # TODO: confirm this
    return 0


def main():
    bases = ["vl", "ln", "l", "ml", "m", "hl", "h"]

    for base in bases:
        for prefix in [
            "scen7-",
            "esm-scen7-",
        ]:
            for suffix in [
                "",
                "-ext",
            ]:
                experiment_name = f"{prefix}{base}{suffix}"

                id = experiment_name.lower()

                content = {
                    "@context": "000_context.jsonld",
                    "id": id,
                    "type": "experiment",
                    "drs_name": experiment_name,
                    "activity": "scenariomip",
                    "additional_allowed_model_components": ["aer", "chem", "bgc"],
                    "required_model_components": ["aogcm"],
                }

                out_file = f"experiment/{id}.json"
                with open(out_file, "w") as fh:
                    json.dump(content, fh, indent=4)

                print(f"Wrote {out_file}")


if __name__ == "__main__":
    main()
