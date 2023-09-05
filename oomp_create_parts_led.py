import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "led"
    part_details["size"] = ["3_mm","5_mm","10_mm","0201","0402","0603","0805","1206"]
    part_details["color"] = ["","red","green","blue","yellow"]
    part_details["description_main"] = [""]
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "L"
    parts.append(part_details)

    #addressable
    #      xinglight
    #            1010    
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "led"
    part_details["size"] = ["1010"]
    part_details["color"] = ["rgb"]
    part_details["description_main"] = ["ws2812b"]
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "xinglight"
    part_details["part_number"] = "1010rgbc"
    part_details["kicad_reference"] = "L"
    parts.append(part_details)        


    oomp.add_parts(parts, **kwargs)
    