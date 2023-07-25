import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "ic"
    part_details["size"] = ["soic_28_wide"]
    part_details["color"] = [""]
    part_details["description_main"] = "led_matrix_driver_16_x_8"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "wuxi_i_core_electronics_co_ltd"
    part_details["part_number"] = "aip1640"
    part_details["short_name"] = "16x8 led matrix driver (aip1640)"
    pins = {}
    pins["1"] = ({"name": "grid12", "number": "1", "type": "signal"})
    pins["2"] = ({"name": "grid13", "number": "2", "type": "signal"})
    pins["3"] = ({"name": "grid14", "number": "3", "type": "signal"})
    pins["4"] = ({"name": "grid15", "number": "4", "type": "signal"})
    pins["5"] = ({"name": "grid16", "number": "5", "type": "signal"})
    pins["6"] = ({"name": "vss", "number": "6", "type": "gnd"})
    pins["7"] = ({"name": "din", "number": "7", "type": "signal"})
    pins["8"] = ({"name": "sclk", "number": "8", "type": "signal"})
    pins["9"] = ({"name": "seg1", "number": "9", "type": "signal"})
    pins["10"] = ({"name": "seg2", "number": "10", "type": "signal"})
    pins["11"] = ({"name": "seg3", "number": "11", "type": "signal"})
    pins["12"] = ({"name": "seg4", "number": "12", "type": "signal"})
    pins["13"] = ({"name": "seg5", "number": "13", "type": "signal"})
    pins["14"] = ({"name": "seg6", "number": "14", "type": "signal"})
    pins["15"] = ({"name": "seg7", "number": "15", "type": "signal"})
    pins["16"] = ({"name": "seg8", "number": "16", "type": "signal"})
    pins["17"] = ({"name": "vdd", "number": "17", "type": "power"})
    pins["18"] = ({"name": "grid1", "number": "18", "type": "signal"})
    pins["19"] = ({"name": "grid2", "number": "19", "type": "signal"})
    pins["20"] = ({"name": "grid3", "number": "20", "type": "signal"})
    pins["21"] = ({"name": "grid4", "number": "21", "type": "signal"})
    pins["22"] = ({"name": "grid5", "number": "22", "type": "signal"})
    pins["23"] = ({"name": "grid6", "number": "23", "type": "signal"})
    pins["24"] = ({"name": "grid7", "number": "24", "type": "signal"})
    pins["25"] = ({"name": "grid8", "number": "25", "type": "signal"})
    pins["26"] = ({"name": "grid9", "number": "26", "type": "signal"})
    pins["27"] = ({"name": "grid10", "number": "27", "type": "signal"})
    pins["28"] = ({"name": "grid11", "number": "28", "type": "signal"})
    part_details["pins"] = pins
    part_details["kicad_reference"] = "U"
    part_details["notes"] = []
    part_details["notes"].append("common cathode (cathode to grid)")
    

    #add the part to the list of parts
    parts.append(part_details)

    
    oomp.add_parts(parts, make_files=make_files)
    