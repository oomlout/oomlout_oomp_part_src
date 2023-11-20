import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []
   

    #define a part 
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "prototyping_breadboard"
    part_details["size"] = ["800_point","400_point"]
    part_details["color"] = [""]
    part_details["description_main"] = [""]
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = ""
    parts.append(part_details)
    

    oomp.add_parts(parts, **kwargs)
    