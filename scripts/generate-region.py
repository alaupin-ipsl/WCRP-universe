"""
Generate region entries
"""

import json


def main():
    for id, drs_name, description, cf_standard_region, iso_region in (
        ("global", "glb", "The entire globe i.e. earth.", "global", None),
        ("antarctica", "ata", "Antarcica.", "antarctica", "ata"),
        ("greenland", "grl", "Greenland.", "greenland", "grl"),
        (
            "30s-90s",
            "30S-90S",
            "The area of the globe south of the latitude 30S.",
            None,
            None,
        ),
        (
            "northern-hemisphere",
            "nh",
            "The northern hemisphere.",
            "northern_hemisphere",
            None,
        ),
        (
            "southern-hemisphere",
            "sh",
            "The southern hemisphere.",
            "southern_hemisphere",
            None,
        ),
    ):
        content = {
            "@context": "000_context.jsonld",
            "id": id,
            "type": "region",
            "description": description,
            "drs_name": drs_name,
            "cf_standard_region": cf_standard_region,
            "iso_region": iso_region,
        }

        out_file = f"region/{id}.json"
        with open(out_file, "w") as fh:
            json.dump(content, fh, indent=4)
            fh.write("\n")

        print(f"Wrote {out_file}")


if __name__ == "__main__":
    main()
