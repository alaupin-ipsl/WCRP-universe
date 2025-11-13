# DO NOT USE THIS SCRIPT, IT WAS USED AS AN InTERMEDIATE TO BUILT vertical_label from OLD vertical_label. Therefore it cant be use anymore as is

import json
from pathlib import Path
import esgvoc.api as ev
from icecream import IceCreamDebugger
import devtools
import re

ic = IceCreamDebugger(argToStringFunction=devtools.pformat)


def main():
    known_bv_in_universe = ev.get_all_terms_in_data_descriptor("known_branded_variable")
    for bv in known_bv_in_universe:
        vertical_label = bv.vertical_label

        all_vl_in_universe = ev.get_all_terms_in_data_descriptor("vertical_label")

        vl_term_in_universe = ev.get_term_in_data_descriptor(
            "vertical_label", vertical_label
        )
        if vertical_label in all_vl_in_universe and not vl_term_in_universe:
            # create it with the good description
            vertical_label_data = {
                "id": vertical_label,
                "label": vertical_label,
                "description": vl_term_in_universe.description,
                "type": "vertical_label",
                "drs_name": vertical_label,
                "@context": "000_context.jsonld",
            }
            with open(Path("vertical_label") / f"{vertical_label}.json", "w") as f:
                json.dump(vertical_label_data, f, indent=4, ensure_ascii=False)

        elif not vl_term_in_universe:
            # create it :
            # lets try to get a basic description
            # lets retrieve the term where the regex match the current term
            description = "TODO"
            for uvl in all_vl_in_universe:
                if re.fullmatch(uvl.regex, vertical_label):
                    description = uvl.description
                    ic(description)
                    break
            vertical_label_data = {
                "id": vertical_label,
                "label": vertical_label,
                "description": description,
                "type": "vertical_label",
                "drs_name": vertical_label,
                "@context": "000_context.jsonld",
            }
            with open(Path("vertical_label") / f"{vertical_label}.json", "w") as f:
                json.dump(vertical_label_data, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
