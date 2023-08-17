import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "ceramic_resonator"
    part_details["size"] = ["3213"]
    part_details["color"] = ["3_pin_ground_pin_2"]
    part_details["description_main"] = ["12_mega_hertz","8_mega_hertz","16_mega_hertz"]
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "x"

    #add the part to the list of parts
    parts.append(part_details)

    
    oomp.add_parts(parts, **kwargs)
    