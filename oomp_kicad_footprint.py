import oomp

def get_footprints(**kwargs):

    matches = []

    #make a pattern match dict for the part, take each element on oomp.names_of_main_elements if the part matches all the items then add the footprint to kwargs

    ###### header
    #for pins 1-40
    for pin_count in range(1, 41):
        #regular pin through hole
        pin_s = str(pin_count).zfill(2)
        match = {}
        match["type"] = "header"
        match["size"] = "2d54_mm"
        match["description_main"] = f"{pin_count}_pin"
        match["description_extra"] = ""
        match["footprint"] = []
        match["footprint"].append({"link": f"https://github.com/oomlout/oomlout_OOMP_eda_V2/tree/main/FOOTPRINT/kicad/kicad-footprints/Connector_PinHeader_2.54mm/PinHeader_1x{pin_s}_P2.54mm_Vertical",
                                    "name": f"Connector_PinHeader_2.54mm : PinHeader_1x{pin_s}_P2.54mm_Vertical",
                                    "id":f"FOOTPRINT-kicad-kicad-footprints-Connector_PinHeader_2.54mm-PinHeader_1x{pin_s}_P2.54mm_Vertical",
                                    "directory": f"FOOTPRINT/kicad/kicad-footprints/Connector_PinHeader_2.54mm/PinHeader_1x{pin_s}_P2.54mm_Vertical/"})
        matches.append(match)   
        #surface mount regular
        match = {}
        match["type"] = "header"
        match["size"] = "2d54_mm"
        match["description_main"] = f"{pin_count}_pin"
        match["description_extra"] = "surface_mount"
        match["footprint"] = []
        match["footprint"].append({"link": f"https://github.com/oomlout/oomlout_OOMP_eda_V2/tree/main/FOOTPRINT/kicad/kicad-footprints/Connector_PinHeader_2.54mm/PinHeader_1x{pin_s}_P2.54mm_Vertical_SMD_Pin1Left",
                                    "name": f"Connector_PinHeader_2.54mm : PinHeader_1x{pin_s}_P2.54mm_Vertical_SMD_Pin1Left",
                                    "id":f"FOOTPRINT-kicad-kicad-footprints-Connector_PinHeader_2.54mm-PinHeader_1x{pin_s}_P2.54mm_Vertical_SMD_Pin1Left",
                                    "directory": f"FOOTPRINT/kicad/kicad-footprints/Connector_PinHeader_2.54mm/PinHeader_1x{pin_s}_P2.54mm_Vertical_SMD_Pin1Left/"})
        #surface mount right angle
        match = {}
        match["type"] = "header"
        match["size"] = "2d54_mm"
        match["description_main"] = f"{pin_count}_pin"
        match["description_extra"] = "surface_mount_right_angle"
        match["footprint"] = []
        match["footprint"].append({"link": f"https://github.com/oomlout/oomlout_OOMP_eda_V2/tree/main/FOOTPRINT/kicad/kicad-footprints/Connector_Harwin/Harwin_M20-890{pin_s}xx_1x{pin_s}_P2.54mm_Horizontal",
                                    "name": f"Connector_Harwin : Harwin_M20-890{pin_s}xx_1x{pin_s}_P2.54mm_Horizontal",
                                    "id":f"FOOTPRINT-kicad-kicad-footprints-Connector_Harwin-Harwin_M20-890{pin_s}xx_1x{pin_s}_P2.54mm_Horizontal",
                                    "directory": f"FOOTPRINT/kicad/kicad-footprints/Connector_Harwin/Harwin_M20-890{pin_s}xx_1x{pin_s}_P2.54mm_Horizontal/"})
        matches.append(match) 
        #jst sh
        match = {}
        match["type"] = "header"
        match["size"] = "1_mm_jst_sh"
        match["description_main"] = f"{pin_count}_pin"
        match["description_extra"] = "surface_mount_right_angle"
        match["footprint"] = []
        match["footprint"].append({"link": f"https://github.com/oomlout/oomlout_OOMP_eda_V2/tree/main/FOOTPRINT/kicad/kicad-footprints/Connector_JST/JST_SH_SM{pin_s}B-SRSS-TB_1x{pin_s}-1MP_P1.00mm_Horizontal",
                                    "name": f"Connector_JST : JST_SH_SM{pin_s}B-SRSS-TB_1x{pin_s}-1MP_P1.00mm_Horizontal",
                                    "id":f"FOOTPRINT-kicad-kicad-footprints-Connector_JST-JST_SH_SM{pin_s}B-SRSS-TB_1x{pin_s}-1MP_P1.00mm_Horizontal",
                                    "directory": f"FOOTPRINT/kicad/kicad-footprints/Connector_JST/JST_SH_SM{pin_s}B-SRSS-TB_1x{pin_s}-1MP_P1.00mm_Horizontal/"})
        matches.append(match) 

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