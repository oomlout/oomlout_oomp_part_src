import oomp

def get_footprints(**kwargs):

    matches = []

    #make a pattern match dict for the part, take each element on oomp.names_of_main_elements if the part matches all the items then add the footprint to kwargs

    ###### ic

    match = {}
    match["size"] = "soic_28_wide"
    match["footprint"] = []
    match["footprint"].append({"link": "https://github.com/oomlout/oomlout_OOMP_eda_V2/tree/main/FOOTPRINT/kicad/kicad-footprints/Package_SO/SOIC-28W_7.5x17.9mm_P1.27mm",
                                 "name": "SOIC-28W_7.5x17.9mm_P1.27mm",
                                 "id":"FOOTPRINT-kicad-kicad-footprints-Package_SO-SOIC-28W_7.5x17.9mm_P1.27mm",
                                 "directory": "FOOTPRINT/kicad/kicad-footprints/Package_SO/SOIC-28W_7.5x17.9mm_P1.27mm"})
    matches.append(match)    

    ###### led

    match = {}
    match["classification"] = "electronic"
    match["type"] = "led"
    match["size"] = "5_mm"
    match["footprint"] = []
    match["footprint"].append({"link": "https://github.com/oomlout/oomlout_OOMP_eda_V2/tree/main/FOOTPRINT/kicad/kicad-footprints/LED_THT/LED_D5.0mm/", 
                               "name": "LED_D5.0mm", 
                               "id":"FOOTPRINT-kicad-kicad-footprints-LED_THT-LED_D5.0mm",
                               "directory": "FOOTPRINT/kicad/kicad-footprints/LED_THT/LED_D5.0mm/"})
    matches.append(match)






    footprints = []
    #go through the keys in oomp.names_of_main_elements if all the values in match match (ignore non mentioned keys) then add it to footprints
    for match in matches:
        match_count = 0
        # get a list with oomp.names_of_main_elements and "id"
        elements_to_check = oomp.names_of_main_elements.copy()
        elements_to_check.append("id")
        for name in elements_to_check:
            try:
                if match[name] == kwargs[name]:
                    match_count += 1
            except:
                pass
                #value not in match check
        if match_count == len(match)-1:
            footprints.extend(match["footprint"])

    if len(footprints) > 0:
        kwargs["footprint"] = footprints
    return kwargs