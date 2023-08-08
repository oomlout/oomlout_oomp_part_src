import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 
    part_details = {}
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
    pins["1"] = ({"name": "tx1", "number": "1", "type": "signal"})
    pins["2"] = ({"name": "rx0", "number": "2", "type": "signal"})
    pins["3"] = ({"name": "rst", "number": "3", "type": "signal"})
    pins["4"] = ({"name": "gnd", "number": "4", "type": "power"})
    pins["5"] = ({"name": "d2", "number": "5", "type": "signal"})
    pins["6"] = ({"name": "d3", "number": "6", "type": "signal"})
    pins["7"] = ({"name": "d4", "number": "7", "type": "signal"})
    pins["8"] = ({"name": "d5", "number": "8", "type": "signal"})
    pins["9"] = ({"name": "d6", "number": "9", "type": "signal"})
    pins["10"] = ({"name": "d7", "number": "10", "type": "signal"})
    pins["11"] = ({"name": "d8", "number": "11", "type": "signal"})
    pins["12"] = ({"name": "d9", "number": "12", "type": "signal"})
    pins["13"] = ({"name": "d10", "number": "13", "type": "signal"})
    pins["14"] = ({"name": "d11", "number": "14", "type": "signal"})
    pins["15"] = ({"name": "d12", "number": "15", "type": "signal"})
    pins["16"] = ({"name": "d13", "number": "16", "type": "signal"})
    pins["17"] = ({"name": "3v3", "number": "17", "type": "power"})
    pins["18"] = ({"name": "ref", "number": "18", "type": "signal"})
    pins["19"] = ({"name": "a0", "number": "19", "type": "signal"})
    pins["20"] = ({"name": "a1", "number": "20", "type": "signal"})
    pins["21"] = ({"name": "a2", "number": "21", "type": "signal"})
    pins["22"] = ({"name": "a3", "number": "22", "type": "signal"})
    pins["23"] = ({"name": "a4", "number": "23", "type": "signal"})
    pins["24"] = ({"name": "a5", "number": "24", "type": "signal"})
    pins["25"] = ({"name": "a6", "number": "25", "type": "signal"})
    pins["26"] = ({"name": "a7", "number": "26", "type": "signal"})
    pins["27"] = ({"name": "5v", "number": "27", "type": "power"})
    pins["28"] = ({"name": "rst", "number": "28", "type": "signal"})
    pins["29"] = ({"name": "gnd", "number": "29", "type": "gnd"})
    pins["30"] = ({"name": "vin", "number": "30", "type": "power"})
    part_details["pins"] = pins
    part_details["kicad_reference"] = "U"
    part_details["notes"] = []
    
    

    #add the part to the list of parts
    parts.append(part_details)

    
    oomp.add_parts(parts, make_files=make_files)
    