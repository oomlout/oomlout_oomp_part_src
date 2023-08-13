import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 

    ## color used for chip type

    ##### atmega

    ##### atmega328
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "socket"
    part_details["size"] = ["usb_mini"]
    part_details["color"] = [""]
    part_details["description_main"] = "surface_mount_only"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = ""    
    parts.append(part_details)

    

    
    
    oomp.add_parts(parts, make_files=make_files)
    