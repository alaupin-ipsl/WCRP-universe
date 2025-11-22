"""
Generate area label entries

Following Table F4 of
[Taylor et al.](https://docs.google.com/document/d/19jzecgymgiiEsTDzaaqeLP6pTvLT-NzCMaq-wu-QoOc/edit?pli=1&tab=t.0)
"""

import json


def main():
    for drs_name, description, cf_area_type in (
        (
            "air",
            (
                "Data is only included where the reporting point is in air "
                "(this isn't always the case e.g. if a variable is reported at sea level pressure "
                "but there is a mountain then the surface would not be air)."
            ),
            "air",
        ),
        (
            "cl",
            ("Data is only included where the reporting point is in cloud."),
            "cloud",
        ),
        (
            "ccl",
            ("Data is only included where the reporting point is in convective cloud."),
            "convective_cloud",
        ),
        (
            "crp",
            (
                "Data is only included where the reporting point is in an area of crops. "
                "Crops is loosely defined and model dependent."
            ),
            "crops",
        ),
        (
            "fis",
            (
                "Data is only included where the reporting point is in an area of floating ice shelf. "
                "Ice shelves are the component of ice sheets that flow over the ocean."
            ),
            "floating_ice_shelf",
        ),
        (
            "gis",
            (
                "Data is only included where the reporting point is in an area of grounded ice sheet. "
                "Grounded ice sheets rest over bedrock, excluding ice-caps, glaciers and floating ice shelves."
            ),
            "grounded_ice_sheet",
        ),
        (
            "ifs",
            (
                "Data is only included where the reporting point is in an area of sea without ice."
            ),
            "ice_free_sea",
        ),
        (
            "is",
            (
                "Data is only included where the reporting point is in an area where ice sheets are present. "
                "It includes both grounded ice sheets resting over bedrock and any ice shelves flowing over the ocean "
                "that are attached to grounded ice sheets. "
                "It excludes ice-caps and glaciers and any floating ice shelves and ice tongues "
                "attached to them."
            ),
            "ice_sheet",
        ),
        (
            "lnd",
            ("Data is only included where the reporting point is in on land."),
            "land",
        ),
        (
            "li",
            (
                "Data is only included where the reporting point is in an area where land ice is present. "
                "'Land ice' means glaciers, ice-caps, grounded ice sheets resting on bedrock and floating ice-shelves."
            ),
            "land_ice",
        ),
        (
            "ng",
            (
                "Data is only included where the reporting point is in an area where natural grasses are present. "
                "'Natural grasses' means grasses growing in areas of low productivity, "
                "often situated on rough or uneven ground. This can include rocky areas, briars and heathland."
            ),
            "natural_grasses",
        ),
        (
            "pst",
            (
                "Data is only included where the reporting point is in an area of pasture. "
                "Pastures are assumed to be anthropogenic in origin. "
                "They include anthropogenically managed pastureland and rangeland."
            ),
            "pastures",
        ),
        (
            "sea",
            (
                "Data is only included where there is sea (both ice-free sea and areas with sea ice)"
            ),
            "sea",
        ),
        (
            "si",
            (
                "Data is only included where the reporting point is in an area where sea ice is present."
            ),
            "sea_ice",
        ),
        (
            "simp",
            (
                "Data is only included where the reporting point is in an area where melt pond on top of sea ice is present."
            ),
            "sea_ice_melt_pond",
        ),
        (
            "sir",
            (
                "Data is only included where the reporting point is in an area where 'ridged' sea ice is present."
            ),
            "sea_ice_ridges",
        ),
        (
            "multi",
            (
                "Data is reported on multiple areas. These are indicated by a 'sector' dimension."
                "This area type is typically used for including multiple land-use or vegetation area types in a single file."
            ),
            None,
        ),
        (
            "shb",
            (
                "Data is only included where the reporting point is in an area of shrubs. "
                "Shrubs is loosely defined and model dependent."
            ),
            "shrubs",
        ),
        (
            "sn",
            ("Data is only included where the reporting point is in an area of snow."),
            "snow",
        ),
        (
            "scl",
            ("Data is only included where the reporting point is in stratiform cloud."),
            "stratiform_cloud",
        ),
        (
            "tree",
            (
                "Data is only included where the reporting point is in an area of trees. "
                "All trees are in the C3 plant functional type. "
                "Trees is loosely defined and model dependent."
            ),
            "trees",
        ),
        (
            "ufs",
            (
                "Data is only included where the reporting point is in an area of unfrozen soil. "
                "Unfrozen soil means that the soil at the surface is unfrozen. "
                "Frozen soil may be present at lower levels."
            ),
            "unfrozen_soil",
        ),
        (
            "veg",
            (
                "Data is only included where the reporting point is in an area of vegetation."
            ),
            "vegetation",
        ),
        (
            "wl",
            (
                "Data is only included where the reporting point is in an area of wetland. "
                "Wetlands are areas where water covers the soil, "
                "or is present either at or near the surface of the soil all year "
                "or for varying periods of time during the year, including during the growing season."
            ),
            "wetland",
        ),
        (
            "lsi",
            (
                "Data is only included where the reporting point is in an area of land or sea ice."
            ),
            None,
        ),
        ("u", ("Unmasked i.e. all areas are included/sampled"), None),
    ):
        id = drs_name.lower()
        content = {
            "@context": "000_context.jsonld",
            "id": id,
            "type": "area_label",
            "description": description,
            "drs_name": drs_name,
            "cf_area_type": cf_area_type,
        }

        out_file = f"area_label/{id}.json"
        with open(out_file, "w") as fh:
            json.dump(content, fh, indent=4)
            fh.write("\n")

        print(f"Wrote {out_file}")


if __name__ == "__main__":
    main()
