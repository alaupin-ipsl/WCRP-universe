"""
Generate frequency entries
"""

import json


def main():
    for drs_name, description, interval, units in (
        (
            "1hr",
            "Hourly samples.",
            1.0,
            "hour",
        ),
        (
            "1hrCM",
            "Monthly climatology (i.e. mean over a number of months) at hourly resolution.",
            1.0,
            "hour",
        ),
        (
            "1hrPt",
            (
                "Hourly samples. This is a legacy label that indicated that the sample was a point sample "
                "i.e. represented the value at a specific point in time. "
                "This information is now conveyed via the temporal label instead."
            ),
            1.0,
            "hour",
        ),
        (
            "3hr",
            "Three hourly samples.",
            3.0,
            "hour",
        ),
        (
            "3hrPt",
            (
                "Three hourly samples. This is a legacy label that indicated that the sample was a point sample "
                "i.e. represented the value at a specific point in time. "
                "This information is now conveyed via the temporal label instead."
            ),
            3.0,
            "hour",
        ),
        (
            "6hr",
            "Three hourly samples.",
            6.0,
            "hour",
        ),
        (
            "6hrPt",
            (
                "Six hourly samples. This is a legacy label that indicated that the sample was a point sample "
                "i.e. represented the value at a specific point in time. "
                "This information is now conveyed via the temporal label instead."
            ),
            6.0,
            "hour",
        ),
        (
            "day",
            "Daily samples.",
            1.0,
            "day",
        ),
        (
            "dec",
            (
                "Decadal samples."
                "Note that this means that the time interval between each sample is not constant for some calendars.",
            ),
            10.0,
            "year",
        ),
        (
            "fx",
            "Fixed field i.e. no time dimension and therefore no applicable frequency information.",
            None,
            None,
        ),
        (
            "mon",
            "Monthly samples. Note that this means that the time interval between each sample is not constant for some calendars.",
            1.0,
            "month",
        ),
        (
            "monC",
            (
                "Monthly climatology (i.e. mean over a number of months) at monthly resolution. "
                "Note that this means that the time interval between each sample is not constant for some calendars."
            ),
            1.0,
            "month",
        ),
        (
            "monPt",
            (
                "Monthly samples. This is a legacy label that indicated that the sample was a point sample "
                "i.e. represented the value at a specific point in time. "
                "This information is now conveyed via the temporal label instead."
            ),
            1.0,
            "month",
        ),
        (
            "subhrPt",
            (
                "Sub-hourly (i.e. more frequently than once per hour) samples. "
                "This is a legacy label that indicated that the sample was a point sample "
                "i.e. represented the value at a specific point in time. "
                "This information is now conveyed via the temporal label instead."
            ),
            # Not uniquely defined therefore None
            None,
            "minute",
        ),
        (
            "yr",
            (
                "Yearly (i.e. annual) samples. "
                "Note that this means that the time interval between each sample is not constant for some calendars."
            ),
            1.0,
            "year",
        ),
        (
            "yrPt",
            (
                "Yearly (i.e. annual) samples. This is a legacy label that indicated that the sample was a point sample "
                "i.e. represented the value at a specific point in time. "
                "This information is now conveyed via the temporal label instead."
            ),
            1.0,
            "year",
        ),
    ):
        id = drs_name.lower()
        content = {
            "@context": "000_context.jsonld",
            "id": id,
            "type": "frequency",
            "description": description,
            "drs_name": drs_name,
            "interval": interval,
            "units": units,
        }

        out_file = f"frequency/{id}.json"
        with open(out_file, "w") as fh:
            json.dump(content, fh, indent=4)
            fh.write("\n")

        print(f"Wrote {out_file}")


if __name__ == "__main__":
    main()
