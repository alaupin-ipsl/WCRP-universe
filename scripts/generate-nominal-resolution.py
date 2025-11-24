"""
Generate nominal resolution entries
"""

import json


def main():
    nominal_resolutions = [
        0.5,
        1.0,
        2.5,
        5.0,
        10.0,
        25.0,
        50.0,
        100.0,
        250.0,
        500.0,
        1000.0,
        2500.0,
        5000.0,
        10000.0,
    ]
    thresholds = [
        0.0,
        0.72,
        1.6,
        3.6,
        7.2,
        16.0,
        36.0,
        72.0,
        160.0,
        360.0,
        720.0,
        1600.0,
        3600.0,
        7200.0,
        1.0e5,
    ]

    for i, resolution in enumerate(nominal_resolutions):
        if resolution > 5.0:
            id = f"{resolution:.0f}-km"
        else:
            id = f"{resolution * 1000:.0f}-m"

        drs_name = id

        content = {
            "@context": "000_context.jsonld",
            "id": id,
            "type": "nominal_resolution",
            "description": (
                "Should drs name include whitespace? "
                "Having whitespace in drs name isn't ideal, but if this will only ever be used in global attributes, "
                "it won't technically break things. "
                f"{resolution:.1f}km nominal resolution. "
                "This value isn't uniform, "
                "but provides an esimate of the resolution of the dataset on average."
            ),
            "drs_name": drs_name,
            "magnitude": resolution,
            "range": [thresholds[i], thresholds[i + 1]],
            "units": "km",
        }

        out_file = f"nominal_resolution/{id}.json"
        with open(out_file, "w") as fh:
            json.dump(content, fh, indent=4)
            fh.write("\n")

        print(f"Wrote {out_file}")


if __name__ == "__main__":
    main()
