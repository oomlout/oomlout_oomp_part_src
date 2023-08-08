import oomp

github_footprint_base = "https://github.com/oomlout/oomlout_oomp_footprint_bot/tree/main/foootprntss"
directory_footprint_base = "oomlout_oomp_footprint_bot/footprints"
directory_footprint_end = "/working/working.kicad_mod"

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
        match["footprint"] = []
        footprint_name = f"kicad_connector_pinheader_2_54mm_pinheader_1x{pin_s}_p2_54mm_vertical"
        match["footprint"].append({"link": f"{github_footprint_base}/{footprint_name}", 
                            "oomp_key": f"oomp_{footprint_name}",                                 
                            "directory": f"{directory_footprint_base}/{footprint_name}/{directory_footprint_end}"})
        matches.append(match)   
        #surface mount regular
        match = {}
        match["type"] = "header"
        match["size"] = "2d54_mm"
        match["description_main"] = f"{pin_count}_pin"
        match["description_extra"] = "surface_mount"
        match["footprint"] = []
        footprint_name = f"kicad_connector_pinheader_2_54mm_pinheader_1x{pin_s}_p2_54mm_vertical_smd_pin"
        match["footprint"].append({"link": f"{github_footprint_base}/{footprint_name}", 
                            "oomp_key": f"oomp_{footprint_name}",                                 
                            "directory": f"{directory_footprint_base}/{footprint_name}/{directory_footprint_end}"})
        matches.append(match)  
        #surface mount right angle
        match = {}
        match["type"] = "header"
        match["size"] = "2d54_mm"
        match["description_main"] = f"{pin_count}_pin"
        match["description_extra"] = "surface_mount_right_angle"
        match["footprint"] = []
        footprint_name = f"kicad_connector_harwin_m20_890{pin_s}xx_1x{pin_s}_p2_54mm_horizontal"
        match["footprint"].append({"link": f"{github_footprint_base}/{footprint_name}", 
                        "oomp_key": f"oomp_{footprint_name}",                                 
                        "directory": f"{directory_footprint_base}/{footprint_name}/{directory_footprint_end}"})
        matches.append(match) 
        #jst sh
        match = {}
        match["type"] = "header"
        match["size"] = "1_mm_jst_sh"
        match["description_main"] = f"{pin_count}_pin"
        match["description_extra"] = "surface_mount_right_angle"
        match["footprint"] = []
        footprint_name = f"kicad_connector_jst_jst_sh_sm{pin_s}b_srss_tb_1x{pin_s}_1mp_p1_00mm_horizontal"
        match["footprint"].append({"link": f"{github_footprint_base}/{footprint_name}", 
                        "oomp_key": f"oomp_{footprint_name}",                                 
                        "directory": f"{directory_footprint_base}/{footprint_name}/{directory_footprint_end}"})
        matches.append(match) 

    ###### ic

    match = {}
    match["size"] = "soic_28_wide"
    match["footprint"] = []
    footprint_name = f"kicad_package_so_soic_28w_7_5x17_9mm_p1_27mm"
    match["footprint"].append({"link": f"{github_footprint_base}/{footprint_name}", 
                        "oomp_key": f"oomp_{footprint_name}",                                 
                        "directory": f"{directory_footprint_base}/{footprint_name}/{directory_footprint_end}"})
    matches.append(match)  

    #for pins 1-40
    ###### is dip
    for pin_count in range(2, 40, 2):
        #regular pin through hole
        pin_s = str(pin_count).zfill(2)

        match = {}
        match["size"] = f"dip_{pin_s}"
        match["footprint"] = []
        footprint_name = f"kicad_package_dip_dip_{pin_s}_w7_62mm"
        match["footprint"].append({"link": f"{github_footprint_base}/{footprint_name}", 
                            "oomp_key": f"oomp_{footprint_name}",                                 
                            "directory": f"{directory_footprint_base}/{footprint_name}/{directory_footprint_end}"})
        matches.append(match)  

    ###### ic mlf (also called vqfn by microchip)
    match = {}
    match["size"] = "mlf_32"
    match["footprint"] = []
    footprint_name = f"kicad_package_dfn_qfn_vqfn_32_1ep_5x5mm_p0_5mm_ep3_1x3_1mm"
    match["footprint"].append({"link": f"{github_footprint_base}/{footprint_name}", 
                        "oomp_key": f"oomp_{footprint_name}",                                 
                        "directory": f"{directory_footprint_base}/{footprint_name}/{directory_footprint_end}"})
    matches.append(match) 
    
    ###### ic tqfp #microchip calls the pitch 1mm kicad 0.8mm 
    match = {}
    match["size"] = "tqfp_32"
    match["footprint"] = []
    footprint_name = f"kicad_package_qfp_tqfp_32_7x7mm_p0_8mm"
    match["footprint"].append({"link": f"{github_footprint_base}/{footprint_name}", 
                        "oomp_key": f"oomp_{footprint_name}",                                 
                        "directory": f"{directory_footprint_base}/{footprint_name}/{directory_footprint_end}"})
    matches.append(match) 
    ###### ic qfn
    match = {}
    match["size"] = "qfn_32"
    match["footprint"] = []
    footprint_name = f"kicad_package_dfn_qfn_qfn_32_1ep_5x5mm_p0_5mm_ep3_1x3_1mm"
    match["footprint"].append({"link": f"{github_footprint_base}/{footprint_name}", 
                        "oomp_key": f"oomp_{footprint_name}",                                 
                        "directory": f"{directory_footprint_base}/{footprint_name}/{directory_footprint_end}"})
    matches.append(match) 
    
    ###### ic vqfn
    match = {}
    match["size"] = "vqfn_28"
    match["footprint"] = []
    footprint_name = f"kicad_package_dfn_qfn_vqfn_28_1ep_4_4mm_p0_45mm_ep2_4x2_4mm"
    match["footprint"].append({"link": f"{github_footprint_base}/{footprint_name}", 
                        "oomp_key": f"oomp_{footprint_name}",                                 
                        "directory": f"{directory_footprint_base}/{footprint_name}/{directory_footprint_end}"})
    matches.append(match)  



    ###### led

    match = {}
    match["classification"] = "electronic"
    match["type"] = "led"
    match["size"] = "5_mm"
    match["footprint"] = []
    footprint_name = f"kicad_led_tht_led_d5_00mm"
    match["footprint"].append({"link": f"{github_footprint_base}/{footprint_name}", 
                        "oomp_key": f"oomp_{footprint_name}",                                 
                        "directory": f"{directory_footprint_base}/{footprint_name}/{directory_footprint_end}"})
    matches.append(match)  

    ###### mounting_holes

    match["type"] = "mounting_hole"
    match["size"] = "m3"
    match["footprint"] = []
    footprint_name = f"kicad_mountinghole_mountinghole_3_2mm_m3"
    match["footprint"].append({"link": f"{github_footprint_base}/{footprint_name}", 
                        "oomp_key": f"oomp_{footprint_name}",                                 
                        "directory": f"{directory_footprint_base}/{footprint_name}/{directory_footprint_end}"})
    matches.append(match)  

    match["type"] = "mounting_hole"
    match["size"] = "m6"
    match["footprint"] = []
    footprint_name = f"kicad_mountinghole_mountinghole_6_4mm_m6"
    match["footprint"].append({"link": f"{github_footprint_base}/{footprint_name}", 
                        "oomp_key": f"oomp_{footprint_name}",                                 
                        "directory": f"{directory_footprint_base}/{footprint_name}/{directory_footprint_end}"})
    matches.append(match)  


    ###### resistor
    match = {}
    match["classification"] = "electronic"
    match["type"] = "resistor"
    match["size"] = "0603"
    match["footprint"] = []
    footprint_name = f"kicad_resistor_smd_r_0603_1608metric"
    match["footprint"].append({"link": f"{github_footprint_base}/{footprint_name}", 
                        "oomp_key": f"oomp_{footprint_name}",                                 
                        "directory": f"{directory_footprint_base}/{footprint_name}/{directory_footprint_end}"})
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