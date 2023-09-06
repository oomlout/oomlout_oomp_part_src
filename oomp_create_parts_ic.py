import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 

    ## color used for chip type

    ##### atmega

    ##### atmega328
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "ic"
    part_details["size"] = ["dip_28"]
    part_details["color"] = ["mcu"]
    part_details["description_main"] = "atmega328"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "microchip"
    part_details["part_number"] = "atmega328p_pu"
    part_details["short_name"] = "atmega328 28 pin dip"    
    parts.append(part_details)

    import copy
    part_details = copy.deepcopy(part_details)
    part_details["size"] = ["qfn_28"]
    part_details["part_number"] = "atmega328p_mn"
    part_details["short_name"] = "atmega328 28 pin qfn"
    parts.append(part_details)    
    
    part_details = copy.deepcopy(part_details)
    part_details["size"] = ["vqfn_28"]
    part_details["part_number"] = "atmega328p_mmh"
    part_details["short_name"] = "atmega328 28 pin vqfn"
    parts.append(part_details) 
    
    part_details = copy.deepcopy(part_details)
    part_details["size"] = ["mlf_32"]
    part_details["part_number"] = "atmega328p_mu"
    part_details["short_name"] = "atmega328 32 pin mlf"
    parts.append(part_details)    
    
    part_details = copy.deepcopy(part_details)
    part_details["size"] = ["tqfp_32"]
    part_details["part_number"] = "atmega328p_au"
    part_details["short_name"] = "atmega328 32 pin tqfp"
    parts.append(part_details) 

    # sensors
    #  bosch
    #   bme280
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "ic"
    part_details["size"] = ["lga_2_5_mm_x_2_5_mm_8_pin"]
    part_details["color"] = ["sensor"]
    part_details["description_main"] = "pressure_temperature"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "bosch"
    part_details["part_number"] = "bme280"
    part_details["short_name"] = "bosch sensortec bme280 pressure and temperature sensor"    
    pins = {}
    pins["pin_1"] = ({"name": "gnd", "number": "1", "type": "power"})
    pins["pin_2"] = ({"name": "csb", "number": "2", "type": "signal"})
    pins["pin_3"] = ({"name": "sdi", "number": "3", "type": "signal"})
    pins["pin_4"] = ({"name": "sck", "number": "4", "type": "signal"})
    pins["pin_5"] = ({"name": "sdo", "number": "5", "type": "signal"})
    pins["pin_6"] = ({"name": "vddio", "number": "6", "type": "power"})
    pins["pin_7"] = ({"name": "gnd", "number": "7", "type": "power"})
    pins["pin_8"] = ({"name": "vdd", "number": "8", "type": "power"})
    part_details["pins"] = pins

    parts.append(part_details)

    #   STK8321
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "ic"
    part_details["size"] = ["lga_2_mm_x_2_mm_12_pin"]
    part_details["color"] = ["sensor"]
    part_details["description_main"] = "accelerometer"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "sensortek"
    part_details["part_number"] = "stk8321"
    part_details["short_name"] = "bosch sensortec bme280 pressure and temperature sensor"    
    pins = {}
    pins["pin_1"] = ({"name": "sa0_sdo", "number": "1", "type": "power"})
    pins["pin_2"] = ({"name": "sda_sdi_sdio", "number": "2", "type": "signal"})
    pins["pin_3"] = ({"name": "vddio", "number": "3", "type": "signal"})
    pins["pin_4"] = ({"name": "res", "number": "4", "type": "signal"})
    pins["pin_5"] = ({"name": "int1", "number": "5", "type": "signal"})
    pins["pin_6"] = ({"name": "int2", "number": "6", "type": "power"})
    pins["pin_7"] = ({"name": "vs", "number": "7", "type": "power"})
    pins["pin_8"] = ({"name": "gndio", "number": "8", "type": "power"})
    pins["pin_9"] = ({"name": "gnd", "number": "9", "type": "power"})
    pins["pin_10"] = ({"name": "cs", "number": "10", "type": "power"})
    pins["pin_11"] = ({"name": "nc", "number": "11", "type": "power"})
    pins["pin_12"] = ({"name": "scl_sck", "number": "12", "type": "power"})
    part_details["pins"] = pins

    parts.append(part_details)

    
    #   ALS-PT19-315C/L177/TR8
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "ic"
    part_details["size"] = ["0603"]
    part_details["color"] = ["sensor"]
    part_details["description_main"] = "light"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "everlight_elec"
    part_details["part_number"] = "als_pt19"
    part_details["short_name"] = "Everlight Elec ALS_PT19_315C_L177_TR8".lower()
    pins = {}
    pins["pin_1"] = ({"name": "collector", "number": "1", "type": "signal"})
    pins["pin_2"] = ({"name": "emitter", "number": "2", "type": "signal"})
    part_details["pins"] = pins

    parts.append(part_details)

    ###### usb multiplexer
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "ic"
    part_details["size"] = ["msop_10"]
    part_details["color"] = ["multiplexer"]
    part_details["description_main"] = "usb_multiplexer"
    part_details["description_extra"] = "two_to_one"
    part_details["manufacturer"] = "jiangsu_runic_tech"
    part_details["part_number"] = "rs2227xn"
    part_details["short_name"] = "usb multiplexer 2 to 1 (rs2227xn)"
    pins = {}
    pins["pin_1"] = ({"name": "v_plus", "number": "1", "type": "signal"})
    pins["pin_2"] = ({"name": "s", "number": "2", "type": "signal"})
    pins["pin_3"] = ({"name": "d_plus", "number": "3", "type": "signal"})
    pins["pin_4"] = ({"name": "d_minus", "number": "4", "type": "signal"})
    pins["pin_5"] = ({"name": "gnd", "number": "5", "type": "signal"})
    pins["pin_6"] = ({"name": "hsd1_minus", "number": "6", "type": "gnd"})
    pins["pin_7"] = ({"name": "hsd1_plus", "number": "7", "type": "signal"})
    pins["pin_8"] = ({"name": "hsd2_minus", "number": "8", "type": "signal"})
    pins["pin_9"] = ({"name": "hsd2_plus", "number": "9", "type": "signal"})
    pins["pin_10"] = ({"name": "oe", "number": "10", "type": "signal"})
    part_details["pins"] = pins
    part_details["kicad_reference"] = "U"
    part_details["notes"] = []
    parts.append(part_details) 


    ###### usb to serial bridge
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "ic"
    part_details["size"] = ["sop_16"]
    part_details["color"] = ["converter"]
    part_details["description_main"] = "usb_to_serial_converter"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "wch"
    part_details["part_number"] = "ch340c"
    part_details["short_name"] = "usb to serial converter (ch340c)"
    pins = {}
    pins["pin_1"] = ({"name": "gnd", "number": "1", "type": "signal"})
    pins["pin_2"] = ({"name": "txd", "number": "2", "type": "signal"})
    pins["pin_3"] = ({"name": "rxd", "number": "3", "type": "signal"})
    pins["pin_4"] = ({"name": "v3", "number": "4", "type": "signal"})
    pins["pin_5"] = ({"name": "ud_plus", "number": "5", "type": "signal"})
    pins["pin_6"] = ({"name": "ud_negative", "number": "6", "type": "gnd"})
    pins["pin_7"] = ({"name": "not_connected", "number": "7", "type": "signal"})
    pins["pin_8"] = ({"name": "out", "number": "8", "type": "signal"})
    pins["pin_9"] = ({"name": "cts", "number": "9", "type": "signal"})
    pins["pin_10"] = ({"name": "dsr", "number": "10", "type": "signal"})
    pins["pin_11"] = ({"name": "ri", "number": "11", "type": "signal"})
    pins["pin_12"] = ({"name": "dcd", "number": "12", "type": "signal"})
    pins["pin_13"] = ({"name": "dtr", "number": "13", "type": "signal"})
    pins["pin_14"] = ({"name": "rts", "number": "14", "type": "signal"})
    pins["pin_15"] = ({"name": "rs232", "number": "15", "type": "signal"})
    pins["pin_16"] = ({"name": "vcc", "number": "16", "type": "signal"})
    part_details["pins"] = pins
    part_details["kicad_reference"] = "U"
    part_details["notes"] = []
    parts.append(part_details) 

    ic_340c = part_details
    import copy
    part_details = copy.deepcopy(ic_340c)
    part_details["size"] = ["sop_16"]
    part_details["part_number"] = "ch340g"
    part_details["short_name"] = "usb to serial converter (ch340g)"
    pins = part_details["pins"]
    pins["pin_7"] = ({"name": "xi", "number": "7", "type": "signal"})
    pins["pin_8"] = ({"name": "xo", "number": "8", "type": "signal"})
    part_details["pins"] = pins
    part_details["kicad_reference"] = "U"
    part_details["notes"] = []
    parts.append(part_details) 

    
    part_details = copy.deepcopy(ic_340c)
    part_details["size"] = ["sop_16"]
    part_details["part_number"] = "ch340b"
    part_details["short_name"] = "usb to serial converter (ch340b)"
    pins = part_details["pins"]
    pins["pin_7"] = ({"name": "rst", "number": "7", "type": "signal"})
    pins["pin_8"] = ({"name": "nc", "number": "8", "type": "signal"})
    pins["pin_15"] = ({"name": "tnow", "number": "15", "type": "signal"})
    part_details["pins"] = pins
    part_details["kicad_reference"] = "U"
    part_details["notes"] = []
    parts.append(part_details) 


    part_details = copy.deepcopy(ic_340c)
    part_details["size"] = ["ssop_20"]
    part_details["part_number"] = "ch340t"
    part_details["short_name"] = "usb to serial converter (ch340t)"
    pins = {}
    pins["pin_1"] = ({"name": "cko", "number": "1", "type": "signal"})
    pins["pin_2"] = ({"name": "act", "number": "2", "type": "signal"})
    pins["pin_3"] = ({"name": "txd", "number": "3", "type": "signal"})
    pins["pin_4"] = ({"name": "rxd", "number": "4", "type": "signal"})
    pins["pin_5"] = ({"name": "v3", "number": "5", "type": "signal"})
    pins["pin_6"] = ({"name": "ud_plus", "number": "6", "type": "gnd"})
    pins["pin_7"] = ({"name": "ud_negative", "number": "7", "type": "signal"})
    pins["pin_8"] = ({"name": "gnd", "number": "8", "type": "signal"})
    pins["pin_9"] = ({"name": "xi", "number": "9", "type": "signal"})
    pins["pin_10"] = ({"name": "xo", "number": "10", "type": "signal"})
    pins["pin_11"] = ({"name": "cts", "number": "11", "type": "signal"})
    pins["pin_12"] = ({"name": "dsr", "number": "12", "type": "signal"})
    pins["pin_13"] = ({"name": "ri", "number": "13", "type": "signal"})
    pins["pin_14"] = ({"name": "dcd", "number": "14", "type": "signal"})
    pins["pin_15"] = ({"name": "dtr", "number": "15", "type": "signal"})
    pins["pin_16"] = ({"name": "rts", "number": "16", "type": "signal"})
    pins["pin_17"] = ({"name": "tnow", "number": "16", "type": "signal"})
    pins["pin_18"] = ({"name": "r232", "number": "16", "type": "signal"})
    pins["pin_19"] = ({"name": "vcc", "number": "16", "type": "signal"})
    pins["pin_20"] = ({"name": "nos", "number": "16", "type": "signal"})
    part_details["pins"] = pins
    part_details["kicad_reference"] = "U"
    part_details["notes"] = []
    parts.append(part_details) 

    part_details = copy.deepcopy(ic_340c)
    part_details["size"] = ["essop_10"]
    part_details["part_number"] = "ch340k"
    part_details["short_name"] = "usb to serial converter (ch340k)"
    pins = {}
    pins["pin_1"] = ({"name": "gnd", "number": "1", "type": "signal"})
    pins["pin_2"] = ({"name": "ud_plus", "number": "2", "type": "signal"})
    pins["pin_3"] = ({"name": "ud_negative", "number": "3", "type": "signal"})
    pins["pin_4"] = ({"name": "gnd", "number": "4", "type": "signal"})
    pins["pin_5"] = ({"name": "cts", "number": "5", "type": "signal"})
    pins["pin_6"] = ({"name": "rts", "number": "6", "type": "gnd"})
    pins["pin_7"] = ({"name": "vcc", "number": "7", "type": "signal"})
    pins["pin_8"] = ({"name": "txd", "number": "8", "type": "signal"})
    pins["pin_9"] = ({"name": "rxd", "number": "9", "type": "signal"})
    pins["pin_10"] = ({"name": "v3", "number": "10", "type": "signal"})
    part_details["pins"] = pins
    part_details["kicad_reference"] = "U"
    part_details["notes"] = []
    parts.append(part_details)

    
    part_details = copy.deepcopy(ic_340c)
    part_details["size"] = ["msop_10"]
    part_details["part_number"] = "ch340e"
    part_details["short_name"] = "usb to serial converter (ch340e)"
    pins = {}
    pins["pin_1"] = ({"name": "ud_plus", "number": "1", "type": "signal"})
    pins["pin_2"] = ({"name": "ud_negative", "number": "2", "type": "signal"})
    pins["pin_3"] = ({"name": "gnd", "number": "3", "type": "signal"})
    pins["pin_4"] = ({"name": "rts", "number": "4", "type": "signal"})
    pins["pin_5"] = ({"name": "cts", "number": "5", "type": "signal"})
    pins["pin_6"] = ({"name": "tnow", "number": "6", "type": "gnd"})
    pins["pin_7"] = ({"name": "vcc", "number": "7", "type": "signal"})
    pins["pin_8"] = ({"name": "rxd", "number": "8", "type": "signal"})
    pins["pin_9"] = ({"name": "txd", "number": "9", "type": "signal"})
    pins["pin_10"] = ({"name": "v3", "number": "10", "type": "signal"})
    part_details["pins"] = pins
    part_details["kicad_reference"] = "U"
    part_details["notes"] = []
    parts.append(part_details) 
    
    ic_340e = part_details
    
    part_details = copy.deepcopy(ic_340e)
    part_details["size"] = ["msop_10"]
    part_details["part_number"] = "ch340x"
    part_details["short_name"] = "usb to serial converter (ch340x)"
    pins = part_details["pins"]
    pins["pin_6"] = ({"name": "tnow_dtr", "number": "6", "type": "gnd"})
    part_details["pins"] = pins
    part_details["kicad_reference"] = "U"
    part_details["notes"] = []
    parts.append(part_details) 
    
    part_details = copy.deepcopy(ic_340c)
    part_details["size"] = ["sop_8"]
    part_details["part_number"] = "ch340n"
    part_details["short_name"] = "usb to serial converter (ch340n)"
    pins = {}
    pins["pin_1"] = ({"name": "ud_plus", "number": "1", "type": "signal"})
    pins["pin_2"] = ({"name": "ud_negative", "number": "2", "type": "signal"})
    pins["pin_3"] = ({"name": "gnd", "number": "3", "type": "signal"})
    pins["pin_4"] = ({"name": "rts", "number": "4", "type": "signal"})
    pins["pin_5"] = ({"name": "vcc", "number": "5", "type": "signal"})
    pins["pin_6"] = ({"name": "txd", "number": "6", "type": "gnd"})
    pins["pin_7"] = ({"name": "rxd", "number": "7", "type": "signal"})
    pins["pin_8"] = ({"name": "v3", "number": "8", "type": "signal"})
    part_details["pins"] = pins
    part_details["kicad_reference"] = "U"
    part_details["notes"] = []
    parts.append(part_details) 
    



    ##### led drivers
    ##### aip1640 led matrix driver
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "ic"
    part_details["size"] = ["soic_28_wide"]
    part_details["color"] = ["led_driver"]
    part_details["description_main"] = "led_matrix_driver_16_x_8"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "wuxi_i_core_electronics_co_ltd"
    part_details["part_number"] = "aip1640"
    part_details["short_name"] = "16x8 led matrix driver (aip1640)"
    pins = {}
    pins["pin_1"] = ({"name": "grid12", "number": "1", "type": "signal"})
    pins["pin_2"] = ({"name": "grid13", "number": "2", "type": "signal"})
    pins["pin_3"] = ({"name": "grid14", "number": "3", "type": "signal"})
    pins["pin_4"] = ({"name": "grid15", "number": "4", "type": "signal"})
    pins["pin_5"] = ({"name": "grid16", "number": "5", "type": "signal"})
    pins["pin_6"] = ({"name": "vss", "number": "6", "type": "gnd"})
    pins["pin_7"] = ({"name": "din", "number": "7", "type": "signal"})
    pins["pin_8"] = ({"name": "sclk", "number": "8", "type": "signal"})
    pins["pin_9"] = ({"name": "seg1", "number": "9", "type": "signal"})
    pins["pin_10"] = ({"name": "seg2", "number": "10", "type": "signal"})
    pins["pin_11"] = ({"name": "seg3", "number": "11", "type": "signal"})
    pins["pin_12"] = ({"name": "seg4", "number": "12", "type": "signal"})
    pins["pin_13"] = ({"name": "seg5", "number": "13", "type": "signal"})
    pins["pin_14"] = ({"name": "seg6", "number": "14", "type": "signal"})
    pins["pin_15"] = ({"name": "seg7", "number": "15", "type": "signal"})
    pins["pin_16"] = ({"name": "seg8", "number": "16", "type": "signal"})
    pins["pin_17"] = ({"name": "vdd", "number": "17", "type": "power"})
    pins["pin_18"] = ({"name": "grid1", "number": "18", "type": "signal"})
    pins["pin_19"] = ({"name": "grid2", "number": "19", "type": "signal"})
    pins["pin_20"] = ({"name": "grid3", "number": "20", "type": "signal"})
    pins["pin_21"] = ({"name": "grid4", "number": "21", "type": "signal"})
    pins["pin_22"] = ({"name": "grid5", "number": "22", "type": "signal"})
    pins["pin_23"] = ({"name": "grid6", "number": "23", "type": "signal"})
    pins["pin_24"] = ({"name": "grid7", "number": "24", "type": "signal"})
    pins["pin_25"] = ({"name": "grid8", "number": "25", "type": "signal"})
    pins["pin_26"] = ({"name": "grid9", "number": "26", "type": "signal"})
    pins["pin_27"] = ({"name": "grid10", "number": "27", "type": "signal"})
    pins["pin_28"] = ({"name": "grid11", "number": "28", "type": "signal"})
    part_details["pins"] = pins
    part_details["kicad_reference"] = "U"
    part_details["notes"] = []
    

    

    #add the part to the list of parts
    parts.append(part_details)

    
    oomp.add_parts(parts, make_files=make_files)
    