import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    # mcu

    #      atmega328p

    #            shennie
    if True:
        part_details = {}
        part_details["description"] = "A popular arduino compatible atmega328 board from aliexpress" 
        part_details["classification"] = "electronic"
        part_details["type"] = "breakout_board"
        part_details["size"] = ["shennie"]
        part_details["color"] = ["mcu"]
        part_details["description_main"] = "atmega328p"
        part_details["description_extra"] = "arduino_compatible"
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
        part_details["kicad_reference"] = "BB"
        part_details["notes"] = []
        parts.append(part_details)

    #             pro_mini
    if True:
        part_details = {}
        part_details["description"] = "A mini usb port free arduino compatible breakout" 
        part_details["classification"] = "electronic"
        part_details["type"] = "breakout_board"
        part_details["size"] = ["pro_mini"]
        part_details["color"] = ["mcu"]
        part_details["description_main"] = "atmega328p"
        part_details["description_extra"] = "arduino_compatible"
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
        pins["pin_17"] = ({"name": "a0", "number": "17", "type": "power"})
        pins["pin_18"] = ({"name": "a1", "number": "18", "type": "signal"})
        pins["pin_19"] = ({"name": "a2", "number": "19", "type": "signal"})
        pins["pin_20"] = ({"name": "a3", "number": "20", "type": "signal"})
        pins["pin_21"] = ({"name": "vcc", "number": "21", "type": "signal"})
        pins["pin_22"] = ({"name": "rst", "number": "22", "type": "signal"})
        pins["pin_23"] = ({"name": "gnd", "number": "23", "type": "signal"})
        pins["pin_24"] = ({"name": "vin", "number": "24", "type": "signal"})
        pins["pin_25"] = ({"name": "a6", "number": "25", "type": "signal"})
        pins["pin_26"] = ({"name": "a7", "number": "26", "type": "signal"})
        pins["pin_27"] = ({"name": "a4", "number": "27", "type": "power"})
        pins["pin_28"] = ({"name": "a5", "number": "28", "type": "signal"})
        pins["pin_29"] = ({"name": "black", "number": "29", "type": "gnd"})
        pins["pin_30"] = ({"name": "gnd", "number": "30", "type": "power"})
        pins["pin_31"] = ({"name": "vcc", "number": "30", "type": "power"})
        pins["pin_32"] = ({"name": "rx0", "number": "30", "type": "power"})
        pins["pin_33"] = ({"name": "tx1", "number": "30", "type": "power"})
        pins["pin_34"] = ({"name": "green", "number": "30", "type": "power"})
        
        part_details["pins"] = pins
        part_details["kicad_reference"] = "BB"
        part_details["notes"] = []
        parts.append(part_details)

    #      espressif 32c
    
    #            devkitc
    if True:
        part_details = {}
        part_details["description"] = "Devkitc pinout version of espresif esp32 breakout." 
        part_details["classification"] = "electronic"
        part_details["type"] = "breakout_board"
        part_details["size"] = ["devkitc"]
        part_details["color"] = ["mcu"]
        part_details["description_main"] = "espressif_esp32"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""
        pins = {}
        pins["pin_1"] = ({"name": "3v3", "number": "1", "type": "signal"})
        pins["pin_2"] = ({"name": "enable", "number": "2", "type": "signal"})
        pins["pin_3"] = ({"name": "vp", "number": "3", "type": "signal"})
        pins["pin_4"] = ({"name": "vn2", "number": "4", "type": "power"})
        pins["pin_5"] = ({"name": "io34", "number": "5", "type": "signal"})
        pins["pin_6"] = ({"name": "io35", "number": "6", "type": "signal"})
        pins["pin_7"] = ({"name": "io32", "number": "7", "type": "signal"})
        pins["pin_8"] = ({"name": "io33", "number": "8", "type": "signal"})
        pins["pin_9"] = ({"name": "io25", "number": "9", "type": "signal"})
        pins["pin_10"] = ({"name": "io26", "number": "10", "type": "signal"})
        pins["pin_11"] = ({"name": "io27", "number": "11", "type": "signal"})
        pins["pin_12"] = ({"name": "io14", "number": "12", "type": "signal"})
        pins["pin_13"] = ({"name": "io12", "number": "13", "type": "signal"})
        pins["pin_14"] = ({"name": "gnd", "number": "14", "type": "signal"})
        pins["pin_15"] = ({"name": "io13", "number": "15", "type": "signal"})
        pins["pin_16"] = ({"name": "d2", "number": "16", "type": "signal"})
        pins["pin_17"] = ({"name": "d3", "number": "17", "type": "power"})
        pins["pin_18"] = ({"name": "cmd", "number": "18", "type": "signal"})
        pins["pin_19"] = ({"name": "5v", "number": "19", "type": "signal"})
        pins["pin_20"] = ({"name": "clk", "number": "20", "type": "signal"})
        pins["pin_21"] = ({"name": "d0", "number": "21", "type": "signal"})
        pins["pin_22"] = ({"name": "d1", "number": "22", "type": "signal"})
        pins["pin_23"] = ({"name": "io15", "number": "23", "type": "signal"})
        pins["pin_24"] = ({"name": "io2", "number": "24", "type": "signal"})
        pins["pin_25"] = ({"name": "io0", "number": "25", "type": "signal"})
        pins["pin_26"] = ({"name": "io4", "number": "26", "type": "signal"})
        pins["pin_27"] = ({"name": "io16", "number": "27", "type": "power"})
        pins["pin_28"] = ({"name": "io17", "number": "28", "type": "signal"})
        pins["pin_29"] = ({"name": "io5", "number": "29", "type": "gnd"})
        pins["pin_30"] = ({"name": "io18", "number": "30", "type": "power"})
        pins["pin_31"] = ({"name": "io19", "number": "31", "type": "signal"})
        pins["pin_32"] = ({"name": "gnd", "number": "32", "type": "signal"})
        pins["pin_33"] = ({"name": "io21", "number": "33", "type": "signal"})
        pins["pin_34"] = ({"name": "rx", "number": "34", "type": "signal"})
        pins["pin_35"] = ({"name": "tx", "number": "35", "type": "signal"})
        pins["pin_36"] = ({"name": "io22", "number": "36", "type": "signal"})
        pins["pin_37"] = ({"name": "io23", "number": "37", "type": "signal"})
        pins["pin_38"] = ({"name": "gnd", "number": "38", "type": "signal"})
        part_details["pins"] = pins
        part_details["kicad_reference"] = "BB"
        part_details["notes"] = []
        parts.append(part_details)

    #      raspberry pi 2040
    #            pico
    if True:
        part_details = {}
        part_details["description"] = "The official Raspberry Pi breakout for the 2040" 
        part_details["classification"] = "electronic"
        part_details["type"] = "breakout_board"
        part_details["size"] = ["pico"]
        part_details["color"] = ["mcu"]
        part_details["description_main"] = "raspberry_pi_2040"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""
        pins = {}
        pins["pin_1"] = ({"name": "gp0", "number": "1", "type": "signal"})
        pins["pin_2"] = ({"name": "gp1", "number": "2", "type": "signal"})
        pins["pin_3"] = ({"name": "gnd", "number": "3", "type": "signal"})
        pins["pin_4"] = ({"name": "gp2", "number": "4", "type": "power"})
        pins["pin_5"] = ({"name": "gp3", "number": "5", "type": "signal"})
        pins["pin_6"] = ({"name": "gp4", "number": "6", "type": "signal"})
        pins["pin_7"] = ({"name": "gp5", "number": "7", "type": "signal"})
        pins["pin_8"] = ({"name": "gnd", "number": "8", "type": "signal"})
        pins["pin_9"] = ({"name": "gp6", "number": "9", "type": "signal"})
        pins["pin_10"] = ({"name": "gp7", "number": "10", "type": "signal"})
        pins["pin_11"] = ({"name": "gp8", "number": "11", "type": "signal"})
        pins["pin_12"] = ({"name": "gp9", "number": "12", "type": "signal"})
        pins["pin_13"] = ({"name": "gnd", "number": "13", "type": "signal"})
        pins["pin_14"] = ({"name": "gp10", "number": "14", "type": "signal"})
        pins["pin_15"] = ({"name": "gp11", "number": "15", "type": "signal"})
        pins["pin_16"] = ({"name": "gp12", "number": "16", "type": "signal"})
        pins["pin_17"] = ({"name": "gp13", "number": "17", "type": "power"})
        pins["pin_18"] = ({"name": "gnd", "number": "18", "type": "signal"})
        pins["pin_19"] = ({"name": "gp14", "number": "19", "type": "signal"})
        pins["pin_20"] = ({"name": "gp15", "number": "20", "type": "signal"})
        pins["pin_21"] = ({"name": "gp16", "number": "21", "type": "signal"})
        pins["pin_22"] = ({"name": "gp17", "number": "22", "type": "signal"})
        pins["pin_23"] = ({"name": "gnd", "number": "23", "type": "signal"})
        pins["pin_24"] = ({"name": "gp18", "number": "24", "type": "signal"})
        pins["pin_25"] = ({"name": "gp19", "number": "25", "type": "signal"})
        pins["pin_26"] = ({"name": "gp20", "number": "26", "type": "signal"})
        pins["pin_27"] = ({"name": "gp21", "number": "27", "type": "power"})
        pins["pin_28"] = ({"name": "gnd", "number": "28", "type": "signal"})
        pins["pin_29"] = ({"name": "gp22", "number": "29", "type": "gnd"})
        pins["pin_30"] = ({"name": "run", "number": "30", "type": "power"})
        pins["pin_31"] = ({"name": "a0", "number": "31", "type": "signal"})
        pins["pin_32"] = ({"name": "a1", "number": "32", "type": "signal"})
        pins["pin_33"] = ({"name": "gnd_adc", "number": "33", "type": "signal"})
        pins["pin_34"] = ({"name": "a2", "number": "34", "type": "signal"})
        pins["pin_35"] = ({"name": "vref", "number": "35", "type": "signal"})
        pins["pin_36"] = ({"name": "3v3_out", "number": "36", "type": "signal"})
        pins["pin_37"] = ({"name": "3v3_enable", "number": "37", "type": "signal"})
        pins["pin_38"] = ({"name": "gnd", "number": "38", "type": "signal"})
        pins["pin_39"] = ({"name": "vsys", "number": "39", "type": "signal"})
        pins["pin_40"] = ({"name": "vbus", "number": "40", "type": "signal"})
        part_details["pins"] = pins
        part_details["kicad_reference"] = "BB"
        part_details["notes"] = []
        parts.append(part_details)  

    # motor driver
    #      stepper motor
    # step stick
    if True:
        part_details = {}
        part_details["description"] = "A common breakout format for a stepper motor driver" 
        part_details["classification"] = "electronic"
        part_details["type"] = "breakout_board"
        part_details["size"] = ["step_stick"]
        part_details["color"] = ["motor_driver"]
        part_details["description_main"] = "stepper_motor"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""
        pins = {}
        pins["pin_1"] = ({"name": "en", "number": "1", "type": "signal"})
        pins["pin_2"] = ({"name": "ms1", "number": "2", "type": "signal"})
        pins["pin_3"] = ({"name": "ms2", "number": "3", "type": "signal"})
        pins["pin_4"] = ({"name": "ms3", "number": "4", "type": "power"})
        pins["pin_5"] = ({"name": "rst", "number": "5", "type": "signal"})
        pins["pin_6"] = ({"name": "slp", "number": "6", "type": "signal"})
        pins["pin_7"] = ({"name": "step", "number": "7", "type": "signal"})
        pins["pin_8"] = ({"name": "dir", "number": "8", "type": "signal"})
        pins["pin_9"] = ({"name": "gnd", "number": "9", "type": "signal"})
        pins["pin_10"] = ({"name": "vdd", "number": "10", "type": "signal"})
        pins["pin_11"] = ({"name": "1b", "number": "11", "type": "signal"})
        pins["pin_12"] = ({"name": "1a", "number": "12", "type": "signal"})
        pins["pin_13"] = ({"name": "2a", "number": "13", "type": "signal"})
        pins["pin_14"] = ({"name": "2b", "number": "14", "type": "signal"})
        pins["pin_15"] = ({"name": "gnd", "number": "15", "type": "signal"})
        pins["pin_16"] = ({"name": "vmot", "number": "16", "type": "signal"})
        part_details["pins"] = pins
        part_details["kicad_reference"] = "BB"
        part_details["notes"] = []
        parts.append(part_details)

    
    oomp.add_parts(parts, make_files=make_files)
    