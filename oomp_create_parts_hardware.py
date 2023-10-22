import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 
    # screw
    part_details = {}
    part_details["classification"] = "hardware"
    part_details["type"] = "screw_flat_head"
    part_details["size"] = ["2_5_mm"]
    part_details["color"] = ["black"]
    part_details["description_main"] = ["4_mm"]
    part_details["description_extra"] = "phillips"
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = ""
    parts.append(part_details)

    # standoff
    #      standard    
    part_details = {}
    part_details["classification"] = "hardware"
    part_details["type"] = "standoff"
    part_details["size"] = ["2_5_mm"]
    part_details["color"] = ["black"]
    part_details["description_main"] = ["10_mm"]
    part_details["description_extra"] = "nut_and_nut"
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = ""
    parts.append(part_details)

    #      screw_and_nut
    part_details = {}
    part_details["classification"] = "hardware"
    part_details["type"] = "standoff"
    part_details["size"] = ["2_5_mm"]
    part_details["color"] = ["black"]
    part_details["description_main"] = ["12_mm"]
    part_details["description_extra"] = "screw_and_nut"
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = ""
    parts.append(part_details)

    oomp.add_parts(parts, **kwargs)
    