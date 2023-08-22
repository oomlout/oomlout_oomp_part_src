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
    pins = {}
    pins["1"] = ({"name": "gnd", "number": "1", "type": "signal"})
    pins["2"] = ({"name": "txd", "number": "2", "type": "signal"})
    pins["3"] = ({"name": "rxd", "number": "3", "type": "signal"})
    pins["4"] = ({"name": "v3", "number": "4", "type": "signal"})
    pins["5"] = ({"name": "ud_plus", "number": "5", "type": "signal"})
    part_details["pins"] = pins
    

    

    
    
    oomp.add_parts(parts, make_files=make_files)
    