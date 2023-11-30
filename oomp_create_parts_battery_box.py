import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 

    ## color used for chip type

    
    # panel_mount
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "battery_box"
    part_details["size"] = ["aa_battery"]
    part_details["color"] = [""]
    part_details["description_main"] = "4_cell"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = ""  
    part_details["distributors"] = []
    parts.append(part_details)    

    
    oomp.add_parts(parts, make_files=make_files)
    