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
    part_details["type"] = "crimp_housing"
    part_details["size"] = ["2_54_mm"]
    part_details["color"] = ["black"]
    part_details["description_main"] = []
    # add 1- 40 _pin
    for pin_count in range(1, 21):
        part_details["description_main"].append(f"{pin_count}_pin")
    part_details["description_extra"] = ["dupont"]
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "CRHO"
    #add the part to the list of parts
    parts.append(part_details)


    oomp.add_parts(parts, make_files=make_files)
    