import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []
   

    #define a part 
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "connector"
    part_details["size"] = ["wago_221"]
    part_details["color"] = [""]
    part_details["description_main"] = ["3_pole","5_pole","2_pole_inline"]
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "L"
    parts.append(part_details)
    

    oomp.add_parts(parts, **kwargs)
    