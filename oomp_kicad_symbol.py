import oomp

github_symbol_base = "https://github.com/oomlout/oomlout_oomp_symbol_bot/tree/main/symbols"
directory_symbol_base = "oomlout_oomp_symbol_bot/symbols"
directory_symbol_end = "/working/working.kicad_sym"

def get_symbols(**kwargs):

    matches = []

    #make a pattern match dict for the part, take each element on oomp.names_of_main_elements if the part matches all the items then add the footprint to kwargs


    ###### header
    
    # for pin 1-40
    for pin_count in range(1, 41):
        pin_s = str(pin_count).zfill(2)
        match = {}
        match["classification"] = "electronic"
        match["type"] = "header"
        match["description_main"] = f"{pin_count}_pin"
        match["symbol"] = []
        symbol_name = f"kicad_connector_conn_01x{pin_s}_pin"
        match["symbol"].append({"link": f"{github_symbol_base}/{symbol_name}", 
                                "oomp_key": f"oomp_{symbol_name}",                                 
                                "directory": f"{directory_symbol_base}/{symbol_name}/{directory_symbol_end}"})
        matches.append(match)

    ###### ic
    match = {}
    match["part_number"] = "atmega328p_pu"
    match["symbol"] = []
    symbol_name = f"kicad_mcu_microchip_atmega_atmega328p_p"
    match["symbol"].append({"link": f"{github_symbol_base}/{symbol_name}", 
                            "oomp_key": f"oomp_{symbol_name}",                                 
                            "directory": f"{directory_symbol_base}/{symbol_name}/{directory_symbol_end}"})
    matches.append(match)
    match = {}
    match["part_number"] = "atmega328p_mn"
    match["symbol"] = []
    symbol_name = f"kicad_mcu_microchip_atmega_atmega328_p"
    match["symbol"].append({"link": f"{github_symbol_base}/{symbol_name}", 
                            "oomp_key": f"oomp_{symbol_name}",                                 
                            "directory": f"{directory_symbol_base}/{symbol_name}/{directory_symbol_end}"})
    matches.append(match)


    ###### led

    match = {}
    match["classification"] = "electronic"
    match["type"] = "led"
    match["symbol"] = []
    symbol_name = f"kicad_device_led"
    match["symbol"].append({"link": f"{github_symbol_base}/{symbol_name}", 
                            "oomp_key": f"oomp_{symbol_name}",                                 
                            "directory": f"{directory_symbol_base}/{symbol_name}/{directory_symbol_end}"})
    matches.append(match)

    ###### resistor

    match = {}
    match["classification"] = "electronic"
    match["type"] = "resistor"
    match["symbol"] = []
    symbol_name = f"kicad_device_r"
    match["symbol"].append({"link": f"{github_symbol_base}/{symbol_name}", 
                            "oomp_key": f"oomp_{symbol_name}",                                 
                            "directory": f"{directory_symbol_base}/{symbol_name}/{directory_symbol_end}"})
    matches.append(match)




    symbols = []
    #go through the keys in oomp.names_of_main_elements if all the values in match match (ignore non mentioned keys) then add it to symbols
    for match in matches:
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

    if len(symbols) > 0:
        kwargs["symbol"] = symbols
    return kwargs