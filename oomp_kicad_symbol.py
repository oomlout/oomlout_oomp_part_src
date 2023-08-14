import oomp

github_symbol_base = "https://github.com/oomlout/oomlout_oomp_symbol_bot/tree/main/symbols"
directory_symbol_base = "oomlout_oomp_symbol_bot/symbols"
directory_symbol_end = "/working/working.kicad_sym"

def get_symbols(**kwargs):

    matches = []

    #make a pattern match dict for the part, take each element on oomp.names_of_main_elements if the part matches all the items then add the footprint to kwargs

    ###### breakout_boards
    match = {}
    match["description_main"] = "atmega328"
    match["description_extra"] = "shennie"
    match["symbol_name"] = f"kicad_mcu_module_arduino_nano_v2_x"
    matches.append(match)

    ###### button
    match = {}
    match["type"] = "button"
    match["symbol_name"] = f"kicad_switch_sw_push"
    matches.append(match)

    ###### capacitor
    
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

    ###### crystal
    match = {}
    match["type"] = "crystal"
    match["color"] = ["2_pin"]
    match["symbol_name"] = f"kicad_device_crystal"
    matches.append(match)
    match = {}
    match["type"] = "crystal"
    match["color"] = ["3_pin"]
    match["symbol_name"] = f"kicad_device_crystal_gnd2"
    matches.append(match)

    match = {}
    match["type"] = "crystal"
    match["color"] = ["3_pin_ground_pin_2"]
    match["symbol_name"] = f"kicad_device_crystal_gnd2"
    matches.append(match)

    ###### diode
    match = {}
    match["type"] = "diode"
    match["symbol_name"] = f"kicad_device_d"
    matches.append(match)

    match = {}
    match["type"] = "diode_schottky"
    match["symbol_name"] = f"kicad_device_d_schottky"
    matches.append(match)

    ###### header
    
    # for pin 1-40
    for pin_count in range(1, 41):
        pin_s = str(pin_count).zfill(2)
        match = {}
        match["classification"] = "electronic"
        match["type"] = "header"
        match["description_main"] = f"{pin_count}_pin"
        match["symbol_name"]  = f"kicad_connector_conn_01x{pin_s}_pin"
        matches.append(match)

    ###### ic
    match = {}
    match["part_number"] = "atmega328p_pu"
    match["symbol_name"] = f"kicad_mcu_microchip_atmega_atmega328p_p"
    matches.append(match)
    match = {}
    match["part_number"] = "atmega328p_mn"
    match["symbol_name"] = f"kicad_mcu_microchip_atmega_atmega328_p"
    matches.append(match)
    match = {}
    match["part_number"] = "atmega328p_mmhr"
    match["symbol_name"] = f"kicad_mcu_microchip_atmega_atmega328_mm"
    matches.append(match)
    match = {}
    match["part_number"] = "atmega328p_aur"
    match["symbol_name"] = f"kicad_mcu_microchip_atmega_atmega328_a"
    matches.append(match)
    match = {}
    match["part_number"] = "atmega328p_mur"
    match["symbol_name"] = f"kicad_mcu_microchip_atmega_atmega328_m"
    matches.append(match)
    
    match = {}
    match["part_number"] = "ch340c"
    match["symbol_name"] = f"kicad_interface_usb_ch340c"
    matches.append(match)
    


    ###### led

    match = {}
    match["classification"] = "electronic"
    match["type"] = "led"
    match["symbol_name"] = f"kicad_device_led"
    matches.append(match)

    ###### pmic
    
    voltage_pairs = []
    voltage_pairs.append(["1_5v","15"])
    voltage_pairs.append(["1_8v","18"])
    voltage_pairs.append(["2_5v","25"])
    voltage_pairs.append(["3_3v","33"])
    voltage_pairs.append(["5v","50"])
    voltage_pairs.append(["adj","adj"])
    for pair in voltage_pairs:
        match = {}
        match["type"] = "pmic"
        match["description_main"] = "1117"    
        match["description_extra"] = pair[0]
        value = pair[1]
        match["symbol_name"] = f"kicad_regulator_linear_ap1117_{value}"
        matches.append(match)
    pass
    ###### resistor
    match = {}
    match["type"] = "resistor"
    match["symbol_name"] = f"kicad_device_r"
    matches.append(match)

    ###### socket
    match = {}
    match["type"] = "socket"
    match["size"] = "usb_mini"
    match["description_main"] = "surface_mount_only"
    match["symbol_name"] = f"kicad_connector_usb_b_mini"
    matches.append(match)   


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