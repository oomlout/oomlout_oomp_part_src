import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    
    #headers up to 40 pin
    #define a part 
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "header"
    part_details["size"] = ["2d54_mm"]
    part_details["color"] = [""]
    part_details["description_main"] = []
    # add 1- 40 _pin
    for pin_count in range(1, 41):
        part_details["description_main"].append(f"{pin_count}_pin")
    part_details["description_extra"] = ["right_angle","surface_mount","","surface_mount_right_angle"]
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "J"
    #add the part to the list of parts
    parts.append(part_details)

    #headers up to 10 pins
    #define a part 
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "header"
    part_details["size"] = ["2_mm_jst_ph","2d54_mm_jst_xh","1_mm_jst_sh"]
    part_details["color"] = [""]
    part_details["description_main"] = []
    # add 1- 10 _pin
    for pin_count in range(1, 11):
        part_details["description_main"].append(f"{pin_count}_pin")
    part_details["description_extra"] = ["right_angle","surface_mount","","surface_mount_right_angle"]
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "J"
    #add the part to the list of parts
    parts.append(part_details)



    #2 row headers
    #headers up to 40 pin
    #define a part 
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "header"
    part_details["size"] = ["2d54_mm_dual_row"]
    part_details["color"] = [""]
    part_details["description_main"] = []
    # add 1- 40 _pin
    for pin_count in range(4, 40, 2):
        part_details["description_main"].append(f"2x{int(pin_count/2)}_dual_row_{pin_count}_pin")
    #part_details["description_extra"] = ["right_angle","surface_mount","","surface_mount_right_angle"]
    part_details["description_extra"] = [""]
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "J"
    #add the part to the list of parts
    parts.append(part_details)
    


    oomp.add_parts(parts, make_files=make_files)
    