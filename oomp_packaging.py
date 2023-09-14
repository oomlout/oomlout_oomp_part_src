import oomp

github_footprint_base = "https://github.com/oomlout/oomlout_oomp_footprint_bot/tree/main/foootprntss"
directory_footprint_base = "oomlout_oomp_footprint_bot/footprints"
directory_footprint_end = "/working/working.kicad_mod"

def get_packaging(**kwargs):

    matches = []

    #make a pattern match dict for the part, take each element on oomp.names_of_main_elements if the part matches all the items then add the footprint to kwargs

    # standard tape
    #      0603
    match = {}
    match["size"] = "0603"
    match["extra_data"] = []
    #reference https://www.vishay.com/docs/20014/smdpack.pdf
    match["extra_data"].append({"key": "package_style", 
                                "value": "smd_tape"})    
    match["extra_data"].append({"key": "smd_tape_width", 
                                "value": "8_mm"})    
    match["extra_data"].append({"key": "smd_tape_depth", 
                                "value": "1_5_mm"})   
    match["extra_data"].append({"key": "smd_tape_pitch", 
                                "value": "4_mm"})       
    matches.append(match)
    
    
    #      0805
    import copy
    match = copy.deepcopy(match)
    match["size"] = "0805"
    matches.append(match)

    #      1206
    match = copy.deepcopy(match)
    match["size"] = "1206"
    matches.append(match)

    #      0402
    match = copy.deepcopy(match)
    match["size"] = "0402"
    match["extra_data"] = []
    #reference https://www.vishay.com/docs/20014/smdpack.pdf
    match["extra_data"].append({"key": "package_style", 
                                "value": "smd_tape"})    
    match["extra_data"].append({"key": "smd_tape_width", 
                                "value": "8_mm"})    
    match["extra_data"].append({"key": "smd_tape_depth", 
                                "value": "1_5_mm"})   
    match["extra_data"].append({"key": "smd_tape_pitch", 
                                "value": "2_mm"})       
    matches.append(match)
    
    matches.append(match)

    # button
    match = {}
    match["id"] = "electronic_button_3_5_mm_x_6_mm_x_2_5_mm_surface_mount"
    match["extra_data"] = []
    #reference https://www.vishay.com/docs/20014/smdpack.pdf
    match["extra_data"].append({"key": "package_style", 
                                "value": "smd_tape"})    
    match["extra_data"].append({"key": "smd_tape_width", 
                                "value": "8_mm"})    
    match["extra_data"].append({"key": "smd_tape_depth", 
                                "value": "3_mm"})   
    match["extra_data"].append({"key": "smd_tape_pitch", 
                                "value": "8_mm"})  
    matches.append(match)
    standard_16mm_tape = copy.deepcopy(match)

    ###### ics
    match = {}
    match["part_number"] = "atmega328p_au"
    match["extra_data"] = []
    match["extra_data"].append({"key": "package_style", 
                                "value": "tray"})    
    matches.append(match)
    
    #      ch340
    match = {}
    match["id"] = "converter_usb_to_serial_converter_wch_ch340g"
    match["extra_data"] = []
    match["extra_data"].append({"key": "package_style", 
                                "value": "smd_tape"})    
    matches.append(match)
    match = {}
    match["id"] = "converter_usb_to_serial_converter_wch_ch340c"
    match["extra_data"] = []
    match["extra_data"].append({"key": "package_style", 
                                "value": "smd_tape"})    
    matches.append(match)

    # header
    match = {}
    match["id"] = "electronic_header_1_mm_jst_sh_4_pin_surface_mount_right_angle"
    match["extra_data"] = []
    #reference https://www.vishay.com/docs/20014/smdpack.pdf
    match["extra_data"].append({"key": "package_style", 
                                "value": "smd_tape"})    
    match["extra_data"].append({"key": "smd_tape_width", 
                                "value": "16_mm"})    
    match["extra_data"].append({"key": "smd_tape_depth", 
                                "value": "4_mm"})   
    match["extra_data"].append({"key": "smd_tape_pitch", 
                                "value": "4_mm"})       
    matches.append(match)
    

    ###### pmic
    match = {}
    match["size"] = "sot_223"
    match["extra_data"] = []
    #reference https://www.nxp.com/docs/en/packing/SOT223_135.pdf
    match["extra_data"].append({"key": "package_style", 
                                "value": "smd_tape"})    
    match["extra_data"].append({"key": "smd_tape_width", 
                                "value": "12_mm"})    
    match["extra_data"].append({"key": "smd_tape_depth", 
                                "value": "2_mm"})    
    match["extra_data"].append({"key": "smd_tape_pitch", 
                                "value": "8_mm"})    
    matches.append(match)
    
    

    ###### add smd magazine
    ###### not working
    for match in matches:
        if "smd_tape_width" and "smd_tape_depth" in match:
            tape_width = match["smd_tape_width"].replace("_mm","")
            tape_depth = match["smd_tape_depth"].replace("_mm","")
            tape_depth_d = tape_depth.replace("_","d")
            extra = {}
            ##example
            ## obb_smd_magazine_03_03_10_nm_8_mm_tape_width_1_5_mm_tape_thickness_ex_1d5
            sizes = ["03", "04", "05", "07", "09" ]
            magazines = []
            for size in sizes:
                magazines.append(f"oobb_smd_magazine_{size}_{size}_{tape_width+2}_nm_{tape_width}_mm_tape_width_{tape_depth}_mm_tape_thickness_ex_{tape_depth_d}")
            if magazines != []:
                match["extra_data"].append = {"key": "smd_magazines", 
                                            "value": magazines}

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
                    print("match")
            except:
                pass
                #value not in match check
        if match_count == len(match)-1:
            for key in match["extra_data"]:
                kwargs[key["key"]] = key["value"]
            

    return kwargs