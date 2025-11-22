"""
Generate temporal label entries

Following Table F1 of
[Taylor et al.](https://docs.google.com/document/d/19jzecgymgiiEsTDzaaqeLP6pTvLT-NzCMaq-wu-QoOc/edit?pli=1&tab=t.0)
"""

import json


def main():
    for drs_name, description in (
        (
            "tmax",
            (
                "Data is the maximum within each time period "
                "(i.e. interval defined by the time bounds)."
            ),
        ),
        (
            "tmin",
            (
                "Data is the minimum within each time period "
                "(i.e. interval defined by the time bounds)."
            ),
        ),
        (
            "tsum",
            (
                "Data is the sum over each time period "
                "(i.e. interval defined by the time bounds)."
            ),
        ),
        (
            "tavg",
            (
                "Data is the average over each time period "
                "(i.e. interval defined by the time bounds)."
            ),
        ),
        (
            "tpt",
            (
                "Data represents the value at the specific point in time "
                "at which the data is reported "
                "(all other time points within each time interval are not considered)."
            ),
        ),
        (
            "tclm",
            (
                "Data is a climatology. "
                "In this case, it is a monthly climatology "
                "i.e. each set of time bounds represents a month "
                "and the values show the monthy-by-month variation "
                "(derived by averaging over a number of years)."
            ),
        ),
        (
            "tclmdc",
            (
                "Data is a climatology. "
                "In this case, it is a diurnal cycle climatology "
                "i.e. each set of time bounds represents an hour "
                "and the values show the hour-by-hour variation "
                "(derived by averaging over a number of days or months or years)."
            ),
        ),
        (
            "tmaxavg",
            (
                "Data is the mean of daily maximum over each time period "
                "(i.e. interval defined by the time bounds)."
                "For example, the data may be reported monthly, "
                "with each value being the mean of the daily maximum temperature "
                "for each day in the month."
            ),
        ),
        (
            "tminavg",
            (
                "Data is the mean of daily minimum over each time period "
                "(i.e. interval defined by the time bounds)."
                "For example, the data may be reported monthly, "
                "with each value being the mean of the daily minimum temperature "
                "for each day in the month."
            ),
        ),
        (
            "ti",
            (
                "Data is time independent i.e. has no time dimension. "
                "This does not necessarily mean the data has no time relevance "
                "e.g. the data may be a mean over all time "
                "(therefore not having a time dimension), "
                "although such cases are rare (if they exist at all) in CMIP contexts."
            ),
        ),
    ):
        id = drs_name.lower()
        content = {
            "@context": "000_context.jsonld",
            "id": id,
            "type": "temporal_label",
            "description": description,
            "drs_name": drs_name,
        }

        out_file = f"temporal_label/{id}.json"
        with open(out_file, "w") as fh:
            json.dump(content, fh, indent=4)
            fh.write("\n")

        print(f"Wrote {out_file}")


if __name__ == "__main__":
    main()
