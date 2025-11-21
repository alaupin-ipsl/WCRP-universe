"""
Generate realm entries
"""

import json


def main():
    for drs_name, description in (
        (
            "aerosol",
            (
                "Dataset which applies (or mostly applies) to "
                "components of the Earth system related to aerosol chemistry."
            ),
        ),
        (
            "atmos",
            (
                "Dataset which applies (or mostly applies) to "
                "or is reported in the atmosphere part of the earth system."
            ),
        ),
        (
            "atmosChem",
            (
                "Dataset which applies (or mostly applies) to "
                "components of the Earth system related to atmospheric chemistry."
            ),
        ),
        (
            "land",
            (
                "Dataset which applies (or mostly applies) to "
                "or is reported in "
                "the land surface and/or sub-surface part of the earth system."
            ),
        ),
        (
            "landIce",
            (
                "Dataset which applies (or mostly applies) to "
                "or is reported on land ice."
            ),
        ),
        (
            "ocean",
            (
                "Dataset which applies (or mostly applies) to "
                "or is reported in the ocean part of the earth system."
            ),
        ),
        (
            "ocnBgchem",
            (
                "Dataset which applies (or mostly applies) to "
                "components of the Earth system related to ocean biogeochemistry."
            ),
        ),
        (
            "seaIce",
            (
                "Dataset which applies (or mostly applies) to "
                "or is reported on sea ice."
            ),
        ),
    ):
        id = drs_name.lower()
        content = {
            "@context": "000_context.jsonld",
            "id": id,
            "type": "realm",
            "description": description,
            "drs_name": drs_name,
        }

        out_file = f"realm/{id}.json"
        with open(out_file, "w") as fh:
            json.dump(content, fh, indent=4)
            fh.write("\n")

        print(f"Wrote {out_file}")


if __name__ == "__main__":
    main()
