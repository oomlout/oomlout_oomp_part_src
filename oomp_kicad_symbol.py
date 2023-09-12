import oomp

github_symbol_base = "https://github.com/oomlout/oomlout_oomp_symbol_bot/tree/main/symbols"
directory_symbol_base = "oomlout_oomp_symbol_bot/symbols"
directory_symbol_end = "/working/working.kicad_sym"

def get_symbols(**kwargs):

    matches = []

    #make a pattern match dict for the part, take each element on oomp.names_of_main_elements if the part matches all the items then add the footprint to kwargs

    # breakout_boards
    match = {}
    match["description_main"] = "atmega328"
    match["description_extra"] = "shennie"
    match["symbol_name"] = f"kicad_mcu_module_arduino_nano_v2_x"
    matches.append(match)

    # button and switch
    match = {}
    match["type"] = "button"
    match["symbol_name"] = f"kicad_switch_sw_push"
    matches.append(match)

    match = {}
    match["type"] = "switch_slide"
    match["description_main"] = "single_pole_single_throw"
    match["symbol_name"] = f"kicad_switch_sw_spst"
    matches.append(match)
    
    match = {}
    match["type"] = "switch_slide"
    match["description_main"] = "single_pole_double_throw"
    match["symbol_name"] = f"kicad_switch_sw_spdt"
    matches.append(match)

    # capacitor

    
    match = {}
    match["type"] = "capacitor"
    match["color"] = ""
    match["symbol_name"] = f"kicad_device_c"
    matches.append(match)
    match = {}
    match["type"] = "capacitor"
    match["color"] = "tantalum"
    match["symbol_name"] = f"kicad_device_c_polarized"
    matches.append(match)

    # crystal
    match = {}
    match["type"] = "crystal"
    match["color"] = "2_pin"
    match["symbol_name"] = f"kicad_device_crystal"
    matches.append(match)    
    
    match = {}
    match["type"] = "crystal"
    match["color"] = "3_pin_ground_pin_2"
    match["symbol_name"] = f"kicad_device_crystal_gnd2"
    matches.append(match)
    
    match = {}
    match["type"] = "ceramic_resonator"
    match["color"] = "3_pin_ground_pin_2"
    match["symbol_name"] = f"kicad_device_crystal_gnd2"
    matches.append(match)

    # diode
    match = {}
    match["type"] = "diode"
    match["symbol_name"] = f"kicad_device_d"
    matches.append(match)

    match = {}
    match["type"] = "diode_schottky"
    match["symbol_name"] = f"kicad_device_d_schottky"
    matches.append(match)

    # header
    
    #      loops
    #             single row
    for pin_count in range(1, 41):
        pin_s = str(pin_count).zfill(2)
        match = {}
        match["classification"] = "electronic"
        match["type"] = "header"
        match["description_main"] = f"{pin_count}_pin"
        match["symbol_name"]  = f"kicad_connector_conn_01x{pin_s}_pin"
        matches.append(match)

    #             dual row
    for pin_count in range(2, 40, 2):
        pin_s = str(pin_count).zfill(2)
        pin_sx2 = str(int(pin_count/2)).zfill(2)
        
        match = {}
        match["classification"] = "electronic"
        match["type"] = "header"
        match["description_main"] = f"2x{int(pin_count/2)}_dual_row_{pin_count}_pin"
        match["symbol_name"]  = f"kicad_connector_generic_conn_02x{pin_sx2}_odd_even"
        matches.append(match)


    # ic
    #      atmega328
    match = {}
    match["part_number"] = "atmega328p_pu"
    match["symbol_name"] = f"kicad_mcu_microchip_atmega_atmega328p_p"
    matches.append(match)
    
    match = {}
    match["part_number"] = "atmega328p_mn"
    match["symbol_name"] = f"kicad_mcu_microchip_atmega_atmega328_p"
    matches.append(match)
    
    match = {}
    match["part_number"] = "atmega328p_mmh"
    match["symbol_name"] = f"kicad_mcu_microchip_atmega_atmega328_mm"
    matches.append(match)
    
    match = {}
    match["part_number"] = "atmega328p_au"
    match["symbol_name"] = f"kicad_mcu_microchip_atmega_atmega328_a"
    matches.append(match)
    
    match = {}
    match["part_number"] = "atmega328p_mu"
    match["symbol_name"] = f"kicad_mcu_microchip_atmega_atmega328_m"
    matches.append(match)
    
    #      bme280
    match = {}
    match["part_number"] = "bme280"
    match["symbol_name"] = f"kicad_sensor_bme280"
    matches.append(match)

    #      ch340
    models = ["c","g","t","e","x"] ###### no k,b symbol yet
    for model in models:
        match = {}
        match["part_number"] = f"ch340{model}"
        match["symbol_name"] = f"kicad_interface_usb_ch340{model}"
        matches.append(match)
    
    # led
    match = {}    
    match["type"] = "led"
    match["symbol_name"] = f"kicad_device_led"
    matches.append(match)
    
    match = {}    
    match["type"] = "led"
    match["description_main"] = "ws2812b"
    match["symbol_name"] = f"kicad_led_ws2812b"
    matches.append(match)

    # mounting_hole
    match = {}
    match["classification"] = "electronic"
    match["type"] = "mounting_hole"
    match["symbol_name"] = f"kicad_mechanical_mountinghole"
    matches.append(match)

    # nettie
    nets = ["2","3","4"] 
    for net in nets:
        match = {}    
        match["type"] = "nettie"
        match["size"] = f"{net}_nets"
        match["symbol_name"] = f"kicad_device_nettie_{net}"
        matches.append(match)
    

    # pmic
    
    #      loops
    voltage_pairs = []
    voltage_pairs.append(["1_5_volt","15"])
    voltage_pairs.append(["1_8_volt","18"])
    voltage_pairs.append(["2_5_volt","25"])
    voltage_pairs.append(["3_3_volt","33"])
    voltage_pairs.append(["5_volt","50"])
    voltage_pairs.append(["adj","adj"])
    
    #            1117
    for pair in voltage_pairs:
        match = {}
        match["type"] = "pmic"
        match["description_main"] = "1117"    
        match["description_extra"] = pair[0]
        value = pair[1]
        match["symbol_name"] = f"kicad_regulator_linear_ap1117_{value}"
        matches.append(match)
    pass

    # resistor
    match = {}
    match["type"] = "resistor"
    match["symbol_name"] = f"kicad_device_r"
    matches.append(match)

    # socket
    match = {}
    match["type"] = "socket"
    match["size"] = "usb_a"
    match["description_main"] = "through_hole"
    match["symbol_name"] = f"kicad_connector_usb_a"
    matches.append(match)  
    
    match = {}
    match["type"] = "socket"
    match["size"] = "usb_micro"
    match["description_main"] = "surface_mount"
    match["symbol_name"] = f"kicad_connector_usb_b_micro"
    matches.append(match) 
    
    match = {}
    match["type"] = "socket"
    match["size"] = "usb_mini"
    match["description_main"] = "surface_mount_only"
    match["symbol_name"] = f"kicad_connector_usb_b_mini"
    matches.append(match)   



    ############################################### processing

    symbols = []
    #go through the keys in oomp.names_of_main_elements if all the values in match match (ignore non mentioned keys) then add it to symbols
    if kwargs["type"] == "resistor":
        pass
    for match in matches:
        if match.get("type","")   == "resistor":
            pass
        if "symbol_name" in match:
            symbol_name = match["symbol_name"]
            match["symbol"] = []        
            match["symbol"].append({"link": f"{github_symbol_base}/{symbol_name}", 
                                "oomp_key": f"oomp_{symbol_name}",                                 
                                "directory": f"{directory_symbol_base}/{symbol_name}/{directory_symbol_end}"})
            #remove symbol_name
            del match["symbol_name"]
        else:
            pass
        match_count = 0
        # get a list with oomp.names_of_main_elements and "id"
        elements_to_check = oomp.names_of_main_elements.copy()
        elements_to_check.append("id")
        for name in elements_to_check:
            try:
                if match[name] == kwargs[name]:
                    match_count += 1
            except:
                pass
                #value not in match check
        if match_count == len(match)-1:
            symbols.extend(match["symbol"])
        #if match.get("type","")   == "resistor":
        #    pass

    if len(symbols) > 0:
        kwargs["symbol"] = symbols
    return kwargs