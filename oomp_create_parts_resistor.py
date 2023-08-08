import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "resistor"
    part_details["size"] = ["quarter_watt_through_hole","0402","0603","0805","1206"]
    part_details["color"] = [""]
    part_details["description_main"] = ["220_ohm","330_ohm","560_ohm","1000_ohm","2200_ohm","10000_ohm"]
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "R"

    #add the part to the list of parts
    parts.append(part_details)

    
    oomp.add_parts(parts, **kwargs)
    