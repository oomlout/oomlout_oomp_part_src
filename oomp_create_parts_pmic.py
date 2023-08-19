import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 

    ## color used for chip type

    ##### atmega

    ##### 1117
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "pmic"
    part_details["size"] = ["sot_223"]
    part_details["color"] = ["linear"]
    part_details["description_main"] = "1117"
    part_details["description_extra"] = ["1_5_volt","1_8_volt","2_5_volt","3_3_volt","5_volt","adj"]
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = ""    
    parts.append(part_details)

    import copy
    
    #add the part to the list of parts
    parts.append(part_details)

    
    oomp.add_parts(parts, make_files=make_files)
    