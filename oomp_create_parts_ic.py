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


    # microchip

    #      pic32mk051024gpk100
    #      electronic_ic_tqfp_100_mcu_pic32_microchip_pic32mk1024gpk100
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "ic"
    part_details["size"] = ["tqfp_100"]
    part_details["color"] = ["mcu"]
    part_details["description_main"] = "pic32"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "microchip"
    part_details["part_number"] = "pic32mk1024gpk100"
    part_details["short_name"] = "pic32mk1024gpk100 "    
    pins = {
    "pin_1": {"name": "AN23_CVD23_PMA23_RG15".lower(), "number": "1", "type": "general"},
    "pin_2": {"name": "VDD".lower(), "number": "2", "type": "power"},
    "pin_3": {"name": "TCK_RPA7_PMD5_RA7".lower(), "number": "3", "type": "general"},
    "pin_4": {"name": "RPB14_VBUSON1_PMD6_RB14".lower(), "number": "4", "type": "general"},
    "pin_5": {"name": "RPB15_PMD7_RB15".lower(), "number": "5", "type": "general"},
    "pin_6": {"name": "RD1".lower(), "number": "6", "type": "general"},
    "pin_7": {"name": "RD2".lower(), "number": "7", "type": "general"},
    "pin_8": {"name": "RPD3_RD3".lower(), "number": "8", "type": "general"},
    "pin_9": {"name": "RPD4_RD4".lower(), "number": "9", "type": "general"},
    "pin_10": {"name": "AN19_CVD19_RPG6_VBUSON2_PMA5_RG6".lower(), "number": "10", "type": "general"},
    "pin_11": {"name": "AN18_CVD18_RPG7_SCL1_PMA4_RG7".lower(), "number": "11", "type": "general"},
    "pin_12": {"name": "AN17_CVD17_RPG8_SDA1_PMA3_RG8".lower(), "number": "12", "type": "general"},
    "pin_13": {"name": "MCLR_hash".lower(), "number": "13", "type": "general"},
    "pin_14": {"name": "AN16_CVD16_RPG9_PMA2_RG9".lower(), "number": "14", "type": "general"},
    "pin_15": {"name": "VSS", "number": "15", "type".lower(): "power"},
    "pin_16": {"name": "VDD", "number": "16", "type".lower(): "power"},
    "pin_17": {"name": "AN22_CVD22_RG10".lower(), "number": "17", "type": "general"},
    "pin_18": {"name": "AN21_CVD21_RE8".lower(), "number": "18", "type": "general"},
    "pin_19": {"name": "AN20_CVD20_RE9".lower(), "number": "19", "type": "general"},
    "pin_20": {"name": "AN10_CVD10_RPA12_RA12".lower(), "number": "20", "type": "general"},
    "pin_21": {"name": "AN9_CVD9_RPA11_RA11".lower(), "number": "21", "type": "general"},
    "pin_22": {"name": "OA2OUT_AN0_C2IN4_negative_C4IN3_negative_RPA0_RA0".lower(), "number": "22", "type": "general"},
    "pin_23": {"name": "OA2IN_positive_AN1_C2IN1_positive_RPA1_RA1".lower(), "number": "23", "type": "general"},
    "pin_24": {"name": "PGD3_OA2IN_negative_AN2_C2IN1_negative_RPB0_CTED2_RB0".lower(), "number": "24", "type": "general"},
    "pin_25": {"name": "PGC3_OA1OUT_AN3_C1IN4_negative_C4IN2_negative_RPB1_CTED1_RB1".lower(), "number": "25", "type": "general"},
    "pin_26": {"name": "PGC1_OA1IN_positive_AN4_C1IN1_positive_C1IN3_negative_C2IN3_negative_RPB2_RB2".lower(), "number": "26", "type": "general"},
    "pin_27": {"name": "PGD1_OA1IN_negative_AN5_CTCMP_C1IN1_negative_RTCC_RPB3_RB3".lower(), "number": "27", "type": "general"},
    "pin_28": {"name": "VREF_negative_AN33_CVD33_PMA7_RF9".lower(), "number": "28", "type": "general"},
    "pin_29": {"name": "VREF_positive_AN34_CVD34_PMA6_RF10".lower(), "number": "29", "type": "general"},
    "pin_30": {"name": "AVDD".lower(), "number": "30", "type": "power"},
    "pin_31": {"name": "AVSS".lower(), "number": "31", "type": "power"},
    "pin_32": {"name": "OA3OUT_AN6_CVD6_C3IN4_negative_C4IN1_positive_C4IN4_negative_RPC0_RC0".lower(), "number": "32", "type": "general"},
    "pin_33": {"name": "OA3IN_negative_AN7_CVD7_C3IN1_negative_C4IN1_negative_RPC1_RC1".lower(), "number": "33", "type": "general"},
    "pin_34": {"name": "OA3IN_positive_AN8_CVD8_C3IN1_positive_C3IN3_negative_RPC2_PMA13_RC2".lower(), "number": "34", "type": "general"},
    "pin_35": {"name": "AN11_CVD11_C1IN2_negative_PMA12_RC11".lower(), "number": "35", "type": "general"},
    "pin_36": {"name": "VSS".lower(), "number": "36", "type": "power"},
    "pin_37": {"name": "VDD".lower(), "number": "37", "type": "power"},
    "pin_38": {"name": "AN35_CVD35_RG11".lower(), "number": "38", "type": "general"},
    "pin_39": {"name": "AN36_CVD36_RF13".lower(), "number": "39", "type": "general"},
    "pin_40": {"name": "AN37_CVD37_RF12".lower(), "number": "40", "type": "general"},
    "pin_41": {"name": "AN12_CVD12_C2IN2_negative_C5IN2_negative_SDA4_PMA11_RE12".lower(), "number": "41", "type": "general"},
    "pin_42": {"name": "AN13_CVD13_C3IN2_negative_SCL4_PMA10_RE13".lower(), "number": "42", "type": "general"},
    "pin_43": {"name": "AN14_CVD14_RPE14_PMA1_RE14".lower(), "number": "43", "type": "general"},
    "pin_44": {"name": "AN15_CVD15_RPE15_PMA0_RE15".lower(), "number": "44", "type": "general"},
    "pin_45": {"name": "VSS".lower(), "number": "45", "type": "power"},
    "pin_46": {"name": "VDD".lower(), "number": "46", "type": "power"},
    "pin_47": {"name": "AN38_CVD38_RD14".lower(), "number": "47", "type": "general"},
    "pin_48": {"name": "AN39_CVD39_RD15".lower(), "number": "48", "type": "general"},
    "pin_49": {"name": "TDI_DAC3_AN26_CVD26_RPA8_SDA2_PMA9_RA8".lower(), "number": "49", "type": "general"},
    "pin_50": {"name": "RPB4_SCL2_PMA8_RB4".lower(), "number": "50", "type": "general"},
    "pin_51": {"name": "OA5IN_positive_DAC1_AN24_CVD24_C5IN1_positive_C5IN3_negative_RPA4_RA4".lower(), "number": "51", "type": "general"},
    "pin_52": {"name": "AN40_CVD40_RPE0_RE0".lower(), "number": "52", "type": "general"},
    "pin_53": {"name": "AN41_CVD41_RPE1_RE1".lower(), "number": "53", "type": "general"},
    "pin_54": {"name": "VBUS1".lower(), "number": "54", "type": "power"},
    "pin_55": {"name": "VUSB3V3".lower(), "number": "55", "type": "power"},
    "pin_56": {"name": "D1_negative".lower(), "number": "56", "type": "general"},
    "pin_57": {"name": "D1_positive".lower(), "number": "57", "type": "general"},
    "pin_58": {"name": "VBUS2".lower(), "number": "58", "type": "power"},
    "pin_59": {"name": "D2_negative".lower(), "number": "59", "type": "general"},
    "pin_60": {"name": "D2_positive".lower(), "number": "60", "type": "general"},
    "pin_61": {"name": "AN45_CVD45_RF5".lower(), "number": "61", "type": "general"},
    "pin_62": {"name": "VDD".lower(), "number": "62", "type": "power"},
    "pin_63": {"name": "OSCI_CLKI_AN49_CVD49_RPC12_RC12".lower(), "number": "63", "type": "general"},
    "pin_64": {"name": "OSCO_CLKO_RPC15_RC15".lower(), "number": "64", "type": "general"},
    "pin_65": {"name": "VSS".lower(), "number": "65", "type": "power"},
    "pin_66": {"name": "AN46_CVD46_RPA14_RA14".lower(), "number": "66", "type": "general"},
    "pin_67": {"name": "AN47_CVD47_RPA15_RA15".lower(), "number": "67", "type": "general"},
    "pin_68": {"name": "RD8".lower(), "number": "68", "type": "general"},
    "pin_69": {"name": "PGD2_RPB5_SDA3_USBID1_RB5".lower(), "number": "69", "type": "general"},
    "pin_70": {"name": "PGC2_RPB6_SCL3_SCK2_PMA15_RB6".lower(), "number": "70", "type": "general"},
    "pin_71": {"name": "DAC2_AN48_CVD48_RPC10_PMA14_PMCS_RC10".lower(), "number": "71", "type": "general"},
    "pin_72": {"name": "OA5OUT_AN25_CVD25_C5IN4_negative_RPB7_SCK1_INT0_RB7".lower(), "number": "72", "type": "general"},
    "pin_73": {"name": "SOSCI_RPC13_4_RC13_4".lower(), "number": "73", "type": "general"},
    "pin_74": {"name": "SOSCO_RPB8_4_T1CK_RB8_4".lower(), "number": "74", "type": "general"},
    "pin_75": {"name": "VSS".lower(), "number": "75", "type": "power"},
    "pin_76": {"name": "TMS_OA5IN_negative_AN27_CVD27_LVDIN_C5IN1_negative_RPB9_RB9".lower(), "number": "76", "type": "general"},
    "pin_77": {"name": "RPC6_USBID2_PMA16_RC6".lower(), "number": "77", "type": "general"},
    "pin_78": {"name": "RPC7_PMA17_RC7".lower(), "number": "78", "type": "general"},
    "pin_79": {"name": "PMD12_RD12".lower(), "number": "79", "type": "general"},
    "pin_80": {"name": "PMD13_RD13".lower(), "number": "80", "type": "general"},
    "pin_81": {"name": "RPC8_PMWR_RC8".lower(), "number": "81", "type": "general"},
    "pin_82": {"name": "RPD5_PMRD_RD5".lower(), "number": "82", "type": "general"},
    "pin_83": {"name": "RPD6_PMD14_RD6".lower(), "number": "83", "type": "general"},
    "pin_84": {"name": "RPC9_PMD15_RC9".lower(), "number": "84", "type": "general"},
    "pin_85": {"name": "VSS".lower(), "number": "85", "type": "power"},
    "pin_86": {"name": "TDO_PMD4_RA10".lower(), "number": "86", "type": "general"},
    "pin_87": {"name": "Reserved".lower(), "number": "87", "type": "reserved"},
    "pin_88": {"name": "RPF0_PMD11_RF0".lower(), "number": "88", "type": "general"},
    "pin_89": {"name": "RPF1_PMD10_RF1".lower(), "number": "89", "type": "general"},
    "pin_90": {"name": "RPG0_PMD8_RG0".lower(), "number": "90", "type": "general"},
    "pin_91": {"name": "TRCLK_PMA18_RF6".lower(), "number": "91", "type": "general"},
    "pin_92": {"name": "TRD3_PMA19_RF7".lower(), "number": "92", "type": "general"},
    "pin_93": {"name": "RPB10_PMD0_RB10".lower(), "number": "93", "type": "general"},
    "pin_94": {"name": "RPB11_PMD1_RB11".lower(), "number": "94", "type": "general"},
    "pin_95": {"name": "TRD2_PMA20_RG14".lower(), "number": "95", "type": "general"},
    "pin_96": {"name": "TRD1_RPG12_PMA21_RG12".lower(), "number": "96", "type": "general"},
    "pin_97": {"name": "TRD0_PMA22_RG13".lower(), "number": "97", "type": "general"},
    "pin_98": {"name": "RPB12_PMD2_RB12".lower(), "number": "98", "type": "general"},
    "pin_99": {"name": "RPB13_CTPLS_PMD3_RB13".lower(), "number": "99", "type": "general"},
    "pin_100": {"name": "TDO_PMD4_RA10".lower(), "number": "100", "type": "general"}
    }
    parts.append(part_details) 


    # sensors
    #  bosch
    #   bme280
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "ic"
    part_details["size"] = ["lga_8_pin_2_5_mm_x_2_5_mm"]
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
    part_details["size"] = ["lga_12_pin_2_mm_x_2_mm"]
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

    ###### usb 
    #       multiplexer
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
    pins["pin_1"] = ({"name": "v_positive", "number": "1", "type": "signal"})
    pins["pin_2"] = ({"name": "s", "number": "2", "type": "signal"})
    pins["pin_3"] = ({"name": "d_positive", "number": "3", "type": "signal"})
    pins["pin_4"] = ({"name": "d_negative", "number": "4", "type": "signal"})
    pins["pin_5"] = ({"name": "gnd", "number": "5", "type": "signal"})
    pins["pin_6"] = ({"name": "hsd1_negative", "number": "6", "type": "gnd"})
    pins["pin_7"] = ({"name": "hsd1_positive", "number": "7", "type": "signal"})
    pins["pin_8"] = ({"name": "hsd2_negative", "number": "8", "type": "signal"})
    pins["pin_9"] = ({"name": "hsd2_positive", "number": "9", "type": "signal"})
    pins["pin_10"] = ({"name": "oe", "number": "10", "type": "signal"})
    part_details["pins"] = pins
    part_details["kicad_reference"] = "U"
    part_details["notes"] = []
    parts.append(part_details) 

    #      power mux
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "ic"
    part_details["size"] = ["tssop_8"]
    part_details["color"] = ["multiplexer"]
    part_details["description_main"] = "power_multiplexer"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "texas_instruments"
    part_details["part_number"] = "tps2113apw"
    part_details["short_name"] = "autoswitching power mux (tps2113apw)"
    pins = {}
    pins["pin_1"] = ({"name": "stat", "number": "1", "type": "signal"})
    pins["pin_2"] = ({"name": "en", "number": "2", "type": "signal"})
    pins["pin_3"] = ({"name": "vsns", "number": "3", "type": "signal"})
    pins["pin_4"] = ({"name": "ilim", "number": "4", "type": "signal"})
    pins["pin_5"] = ({"name": "gnd", "number": "5", "type": "signal"})
    pins["pin_6"] = ({"name": "in2", "number": "6", "type": "power"})
    pins["pin_7"] = ({"name": "out", "number": "7", "type": "power"})
    pins["pin_8"] = ({"name": "in1", "number": "8", "type": "power"})
    part_details["pins"] = pins
    part_details["kicad_reference"] = "IC"
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
    pins["pin_5"] = ({"name": "ud_positive", "number": "5", "type": "signal"})
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
    pins["pin_6"] = ({"name": "ud_positive", "number": "6", "type": "gnd"})
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
    pins["pin_2"] = ({"name": "ud_positive", "number": "2", "type": "signal"})
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
    pins["pin_1"] = ({"name": "ud_positive", "number": "1", "type": "signal"})
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
    pins["pin_1"] = ({"name": "ud_positive", "number": "1", "type": "signal"})
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
    