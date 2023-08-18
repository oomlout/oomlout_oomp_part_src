import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    parts = []
    
    #define a part 
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "nettie"
    part_details["size"] = ["2_nets","3_nets", "4_nets"]
    part_details["color"] = [""]
    #part_details["description_main"] = ["220_ohm","330_ohm","560_ohm","1000_ohm","2200_ohm","10000_ohm"]
    #e12 values
    part_details["description_main"] = ["smd","through_hole"]
    
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = ""

    #add the part to the list of parts
    parts.append(part_details)

    
    oomp.add_parts(parts, **kwargs)
    