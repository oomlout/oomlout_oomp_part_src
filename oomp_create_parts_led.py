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
    pins = {}
    pins["pin_1"] = ({"name": "do", "number": "1", "type": "signal"})
    pins["pin_2"] = ({"name": "vdd", "number": "2", "type": "power"})
    pins["pin_3"] = ({"name": "gnd", "number": "3", "type": "power"})
    pins["pin_4"] = ({"name": "sdi", "number": "4", "type": "signal"})
    part_details["pins"] = pins

    oomp.add_parts(parts, **kwargs)
    
    #            5050
    #                  https://www.lcsc.com/product-detail/Light-Emitting-Diodes-LED_Worldsemi-WS2812B-B_C114586.html
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "led"
    part_details["size"] = ["5050"]
    part_details["color"] = ["rgb"]
    part_details["description_main"] = ["ws2812b"]
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "worldsemi"
    part_details["part_number"] = "ws2812b_b_w"
    part_details["kicad_reference"] = "L"
    parts.append(part_details)        
    pins = {}
    pins["pin_1"] = ({"name": "vdd", "number": "1", "type": "signal"})
    pins["pin_2"] = ({"name": "dout", "number": "2", "type": "power"})
    pins["pin_3"] = ({"name": "vss", "number": "3", "type": "power"})
    pins["pin_4"] = ({"name": "din", "number": "4", "type": "signal"})
    part_details["pins"] = pins

    oomp.add_parts(parts, **kwargs)
    