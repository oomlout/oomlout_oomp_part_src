import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    
    # nut
    part_details = {}
    part_details["classification"] = "hardware"
    part_details["type"] = ["nut"]
    sizes = [2,"2_5","2_7",3,4,5,6]
    part_details["size"] = []
    for size in sizes:
        part_details["size"].append(f"{size}_mm")
    part_details["color"] = [""]
    part_details["description_main"] = [""]
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = ""
    parts.append(part_details)

    # screw

    #      m2 self_tapping
    part_details = {}
    part_details["classification"] = "hardware"
    part_details["type"] = ["screw_self_tapping"]
    part_details["size"] = ["2_mm"]
    part_details["color"] = [""]
    lengths = [10]
    part_details["description_main"] = []
    for length in lengths:
        part_details["description_main"].append(f"{length}_mm")
    part_details["description_extra"] = "phillips"
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = ""
    parts.append(part_details)

    #      m3 common
    part_details = {}
    part_details["classification"] = "hardware"
    part_details["type"] = ["screw_countersunk","screw_socket_cap"]
    part_details["size"] = ["3_mm"]
    part_details["color"] = ["black"]
    lengths = [6,8,10,12,15,20,25,30,35,40]
    part_details["description_main"] = []
    for length in lengths:
        part_details["description_main"].append(f"{length}_mm")
    part_details["description_extra"] = "hex"
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = ""
    parts.append(part_details)


    #      flat_head
    #            niche for omer    
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
    