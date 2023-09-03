import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 

    ##### arduino compatible
    #      shennie
    part_details = {}
    part_details["description"] = "An interposer between an i2c chip and a soic_14_wide package, The pins are numbered in the reverse order of being expected because the footprint is used as a mirror image, ie. it is the chip rather than a chuip being palced on it" 
    part_details["classification"] = "electronic"
    part_details["type"] = "interposer"
    part_details["size"] = ["soic_14_wide"]
    part_details["color"] = [""]
    part_details["description_main"] = "i2c"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = ""
    pins = {}
    pins["pin_1"] = ({"name": "pin_14", "number": "1", "type": "power"})
    pins["pin_2"] = ({"name": "pin_13", "number": "2", "type": "power"})
    pins["pin_3"] = ({"name": "pin_12", "number": "3", "type": "signal"})
    pins["pin_4"] = ({"name": "pin_11", "number": "4", "type": "signal"})
    pins["pin_5"] = ({"name": "pin_10", "number": "5", "type": "signal"})
    pins["pin_6"] = ({"name": "pin_9", "number": "6", "type": "signal"})
    pins["pin_7"] = ({"name": "pin_8", "number": "7", "type": "signal"})
    pins["pin_8"] = ({"name": "pin_7", "number": "8", "type": "signal"})
    pins["pin_9"] = ({"name": "address", "number": "9", "type": "signal"})
    pins["pin_10"] = ({"name": "cs", "number": "10", "type": "signal"})
    pins["pin_11"] = ({"name": "scl_3v3", "number": "11", "type": "signal"})
    pins["pin_12"] = ({"name": "sda_3v3", "number": "12", "type": "signal"})
    pins["pin_13"] = ({"name": "3v3", "number": "13", "type": "signal"})
    pins["pin_14"] = ({"name": "gnd", "number": "14", "type": "signal"})
    part_details["pins"] = pins
    part_details["kicad_reference"] = "U"
    part_details["notes"] = []
    
    
    

    #add the part to the list of parts
    parts.append(part_details)

    
    oomp.add_parts(parts, make_files=make_files)
    