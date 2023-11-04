import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    
    resistor_values = []    
    resistor_values.append("10000_ohm")
    


    #define a part 
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "potentiometer"
    part_details["size"] = ["17_mm"]
    part_details["color"] = [""]
    part_details["description_main"] = resistor_values
    part_details["description_extra"] = [""]
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "VR"

    #add the part to the list of parts
    parts.append(part_details)

    
    oomp.add_parts(parts, **kwargs)
    