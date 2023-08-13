import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "capacitor"
    part_details["size"] = ["0603"]
    part_details["color"] = [""]
    part_details["description_main"] = ["100_nano_farad","1_micro_farad","10_micro_farad""4_7_micro_farad"]
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "C"
    parts.append(part_details)


    import copy 
    part_details = copy.deepcopy(part_details)
    part_details["size"] = ["0402"]
    part_details["description_main"] = ["100_nano_farad","1_micro_farad","10_nano_farad","22_nano_farad"]
    parts.append(part_details)

    #tantalum capacitors

    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "capacitor"
    part_details["size"] = ["3216_avx_a"]
    part_details["color"] = ["tantalum"]
    part_details["description_main"] = ["4_7_micro_farad"]
    part_details["description_extra"] = ["16_volt"]
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "C"    
    parts.append(part_details)


    #add the part to the list of parts
    parts.append(part_details)

    
    oomp.add_parts(parts, **kwargs)
    