"""
Generate horizontal label entries

Following Table F3 of
[Taylor et al.](https://docs.google.com/document/d/19jzecgymgiiEsTDzaaqeLP6pTvLT-NzCMaq-wu-QoOc/edit?pli=1&tab=t.0)
"""

import json


def main():
    for drs_name, description in (
        (
            "hxy",
            ("Data on x-y (often lat-lon) grid, also referred to as gridded data."),
        ),
        (
            "hy",
            (
                "Data on y (often just lat) grid. "
                "This is usually zonal-mean or zonal-sum or some other zonal-aggregate data."
            ),
        ),
        (
            "hs",
            ("Data reported at specific sites."),
        ),
        (
            "hyb",
            (
                "Data on y (often just lat) grids in specific basins. "
                "This is usually zonal-mean or zonal-sum or some other zonal-aggregate data."
            ),
        ),
        (
            "ht",
            (
                "Data along a transect. "
                "This is usually some aggregate (sum, mean etc.) along the transect(s)."
            ),
        ),
        (
            "hm",
            (
                "No other horizontal label. "
                "This usually means the data is a horizontal mean "
                "(therefore has no horizontal dimensions)."
            ),
        ),
    ):
        id = drs_name.lower()
        content = {
            "@context": "000_context.jsonld",
            "id": id,
            "type": "horizontal_label",
            "description": description,
            "drs_name": drs_name,
        }

        out_file = f"horizontal_label/{id}.json"
        with open(out_file, "w") as fh:
            json.dump(content, fh, indent=4)
            fh.write("\n")

        print(f"Wrote {out_file}")


if __name__ == "__main__":
    main()
