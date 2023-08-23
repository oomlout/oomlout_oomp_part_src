import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 
    part_details = {}
    part_details["description"] = "A popular arduino compatible atmega328 board from aliexpress" 
    part_details["classification"] = "electronic"
    part_details["type"] = "breakout_board"
    part_details["size"] = [""]
    part_details["color"] = ["mcu"]
    part_details["description_main"] = "atmega328"
    part_details["description_extra"] = "shennie"
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = ""
    pins = {}
    pins["pin_1"] = ({"name": "tx1", "number": "1", "type": "signal"})
    pins["pin_2"] = ({"name": "rx0", "number": "2", "type": "signal"})
    pins["pin_3"] = ({"name": "rst", "number": "3", "type": "signal"})
    pins["pin_4"] = ({"name": "gnd", "number": "4", "type": "power"})
    pins["pin_5"] = ({"name": "d2", "number": "5", "type": "signal"})
    pins["pin_6"] = ({"name": "d3", "number": "6", "type": "signal"})
    pins["pin_7"] = ({"name": "d4", "number": "7", "type": "signal"})
    pins["pin_8"] = ({"name": "d5", "number": "8", "type": "signal"})
    pins["pin_9"] = ({"name": "d6", "number": "9", "type": "signal"})
    pins["pin_10"] = ({"name": "d7", "number": "10", "type": "signal"})
    pins["pin_11"] = ({"name": "d8", "number": "11", "type": "signal"})
    pins["pin_12"] = ({"name": "d9", "number": "12", "type": "signal"})
    pins["pin_13"] = ({"name": "d10", "number": "13", "type": "signal"})
    pins["pin_14"] = ({"name": "d11", "number": "14", "type": "signal"})
    pins["pin_15"] = ({"name": "d12", "number": "15", "type": "signal"})
    pins["pin_16"] = ({"name": "d13", "number": "16", "type": "signal"})
    pins["pin_17"] = ({"name": "3v3", "number": "17", "type": "power"})
    pins["pin_18"] = ({"name": "ref", "number": "18", "type": "signal"})
    pins["pin_19"] = ({"name": "a0", "number": "19", "type": "signal"})
    pins["pin_20"] = ({"name": "a1", "number": "20", "type": "signal"})
    pins["pin_21"] = ({"name": "a2", "number": "21", "type": "signal"})
    pins["pin_22"] = ({"name": "a3", "number": "22", "type": "signal"})
    pins["pin_23"] = ({"name": "a4", "number": "23", "type": "signal"})
    pins["pin_24"] = ({"name": "a5", "number": "24", "type": "signal"})
    pins["pin_25"] = ({"name": "a6", "number": "25", "type": "signal"})
    pins["pin_26"] = ({"name": "a7", "number": "26", "type": "signal"})
    pins["pin_27"] = ({"name": "5v", "number": "27", "type": "power"})
    pins["pin_28"] = ({"name": "rst", "number": "28", "type": "signal"})
    pins["pin_29"] = ({"name": "gnd", "number": "29", "type": "gnd"})
    pins["pin_30"] = ({"name": "vin", "number": "30", "type": "power"})
    part_details["pins"] = pins
    part_details["kicad_reference"] = "U"
    part_details["notes"] = []
    
    

    #add the part to the list of parts
    parts.append(part_details)

    
    oomp.add_parts(parts, make_files=make_files)
    