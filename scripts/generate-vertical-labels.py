"""
Generate vertical label entries

Following Table F2 of
[Taylor et al.](https://docs.google.com/document/d/19jzecgymgiiEsTDzaaqeLP6pTvLT-NzCMaq-wu-QoOc/edit?pli=1&tab=t.0)
"""

import json


def main():
    for drs_name, description in (
        ("sl", "Data is reported on the model's soil model levels."),
        ("al", "Data is reported on the model's atmospheric model levels."),
        (
            "alh",
            (
                "Data is reported on the model's atmospheric model half-levels "
                "(i.e. at the interfaces between model vertical layers)."
            ),
        ),
        ("ol", "Data is reported on the model's ocean model levels."),
        (
            "olh",
            (
                "Data is reported on the model's ocean model half-levels "
                "(i.e. at the interfaces between model vertical layers)."
            ),
        ),
        ("rho", "Data is reported on specific density surface(s)."),
        ("h2m", "Data is reported at a vertical height of 2m."),
        ("h10m", "Data is reported at a vertical height of 10m."),
        ("h100m", "Data is reported at a vertical height of 100m."),
        ("d10cm", "Data is reported at a vertical depth of 0.1m (10cm)."),
        ("d100cm", "Data is reported at a vertical depth of 1m (100cm)."),
        ("d0m", "Data is reported at the surface."),
        ("d100m", "Data is reported at a vertical depth of 100m."),
        # Should these be e.g. o300m as they're not depth, but 'upper ocean' ?
        ("d300m", "Data is reported over the upper 300m of the ocean."),
        ("d700m", "Data is reported over the upper 700m of the ocean."),
        ("d2000m", "Data is reported over the upper 2000m of the ocean."),
        ("20bar", "Data is reported at a pressure depth of 20 bar."),
        ("10hPa", "Data is reported at an atmospheric pressure of 10 hPa."),
        ("100hPa", "Data is reported at an atmospheric pressure of 100 hPa."),
        ("200hPa", "Data is reported at an atmospheric pressure of 200 hPa."),
        ("220hPa", "Data is reported at an atmospheric pressure of 220 hPa."),
        ("500hPa", "Data is reported at an atmospheric pressure of 500 hPa."),
        ("560hPa", "Data is reported at an atmospheric pressure of 560 hPa."),
        ("700hPa", "Data is reported at an atmospheric pressure of 700 hPa."),
        ("840hPa", "Data is reported at an atmospheric pressure of 840 hPa."),
        ("850hPa", "Data is reported at an atmospheric pressure of 850 hPa."),
        ("925hPa", "Data is reported at an atmospheric pressure of 925hPa."),
        ("1000hPa", "Data is reported at an atmospheric pressure of 1000 hPa."),
        ("h16", "Data is reported at 16 height levels."),
        ("h40", "Data is reported at 40 height levels"),
        ("p3", "Data is reported at 3 pressure levels"),
        ("p4", "Data is reported at 4 pressure levels."),
        ("p5u", "Data is reported at 5 pressure levels."),
        ("p6", "Data is reported at 6 pressure levels."),
        ("p8", "Data is reported at 8 pressure levels."),
        (
            "p7c",
            "Data is reported at 7 pressure levels "
            "(although they're not the same pressure levels as `p7h`).",
        ),
        (
            "p7h",
            "Data is reported at 7 pressure levels "
            "(although they're not the same pressure levels as `p7c`).",
        ),
        ("p19", "Data is reported at 19 pressure levels."),
        ("p27", "Data is reported at 27 pressure levels."),
        ("p39", "Data is reported at 39 pressure levels."),
        ("op4", "Data is reported at 4 ocean pressure layers."),
        (
            "u",
            (
                "Data is reported with no vertical dimension. "
                "This does not necessarily mean that there is no vertical information "
                "attached to the variable, it is just not included in the dimension information. "
                "Vertical information could alternately be found in the variable's standard name "
                "or cell methods."
            ),
        ),
    ):
        id = drs_name.lower()
        content = {
            "@context": "000_context.jsonld",
            "id": id,
            "type": "vertical_label",
            "description": description,
            "drs_name": drs_name,
        }

        out_file = f"vertical_label/{id}.json"
        with open(out_file, "w") as fh:
            json.dump(content, fh, indent=4)
            fh.write("\n")

        print(f"Wrote {out_file}")


if __name__ == "__main__":
    main()
