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
    part_details["size"] = ["2_54_mm"]
    part_details["color"] = [""]
    part_details["description_main"] = []
    # add 1- 40 _pin
    for pin_count in range(1, 41):
        part_details["description_main"].append(f"{pin_count}_pin")
    part_details["description_extra"] = ["right_angle","surface_mount","through_hole","surface_mount_right_angle","through_hole_right_angle"]
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "CONN"
    #add the part to the list of parts
    parts.append(part_details)

    """
    ###1d27 headers
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "header"
    part_details["size"] = ["1d27_mm"]
    part_details["color"] = [""]
    part_details["description_main"] = []
    # add 1- 40 _pin
    for pin_count in range(1, 21):
        part_details["description_main"].append(f"{pin_count}_pin")
    part_details["description_extra"] = [""]
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "CONN"
    #add the part to the list of parts
    parts.append(part_details)
    """

    ###### jst
    #      2_5 xh
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "header"
    part_details["size"] = ["2_5_mm_jst_xh"]
    part_details["color"] = [""]
    part_details["description_main"] = []
    # add 1- 10 _pin
    for pin_count in range(2, 11):
        part_details["description_main"].append(f"{pin_count}_pin")
    part_details["description_extra"] = ["through_hole_right_angle","surface_mount","through_hole","surface_mount_right_angle"]
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "CONN"
    #add the part to the list of parts
    parts.append(part_details)

    """
    
    #      2 mm ph
    #define a part 
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "header"
    part_details["size"] = ["2_mm_jst_ph"]
    part_details["color"] = [""]
    part_details["description_main"] = []
    # add 1- 10 _pin
    for pin_count in range(1, 11):
        part_details["description_main"].append(f"{pin_count}_pin")
    part_details["description_extra"] = ["right_angle","surface_mount","","surface_mount_right_angle"]
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "CONN"
    #add the part to the list of parts
    parts.append(part_details)
    """
    
    #      1_mm_sh    
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "header"
    part_details["size"] = ["1_mm_jst_sh"]
    part_details["color"] = [""]
    part_details["description_main"] = []
    # add 1- 10 _pin
    for pin_count in range(2, 11):
        part_details["description_main"].append(f"{pin_count}_pin")
    part_details["description_extra"] = ["surface_mount","surface_mount_right_angle"]
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "CONN"
    #add the part to the list of parts
    parts.append(part_details)



    #2 row headers
    #headers up to 40 pin
    #define a part 
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "header"
    part_details["size"] = ["2_54_mm_dual_row"]
    part_details["color"] = [""]
    part_details["description_main"] = []
    # add 1- 40 _pin
    for pin_count in range(4, 40, 2):
        part_details["description_main"].append(f"2x{int(pin_count/2)}_{pin_count}_pin")
    part_details["description_extra"] = ["through_hole","through_hole_right_angle","surface_mount","surface_mount_right_angle"]
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "CONN"
    #add the part to the list of parts
    parts.append(part_details)
    

    #3 row headers
    #headers up to 40 pin
    #define a part 
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "header"
    part_details["size"] = ["2_54_mm_triple_row"]
    part_details["color"] = [""]
    part_details["description_main"] = []
    # add 1- 40 _pin
    for pin_count in range(6, 30, 3):
        part_details["description_main"].append(f"3x{int(pin_count/3)}_{pin_count}_pin")
    part_details["description_extra"] = ["through_hole","through_hole_right_angle"]
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "CONN"
    #add the part to the list of parts
    parts.append(part_details)

    oomp.add_parts(parts, make_files=make_files)
    