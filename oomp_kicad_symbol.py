import oomp

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
        match["symbol"].append({"link": f"https://github.com/oomlout/oomlout_OOMP_eda_V2/tree/main/SYMBOL/kicad/kicad-symbols/Connector/Conn_01x{pin_s}_Male", 
                                "name": f"Connector : Conn_01x{pin_s}_Male", 
                                "id":f"SYMBOL-kicad-kicad-symbols-Connector-Conn_01x{pin_s}_Male",
                                "directory": f"SYMBOL/kicad/kicad-symbols/Connector/Conn_01x{pin_s}_Male/"})
        matches.append(match)

    ###### led

    match = {}
    match["classification"] = "electronic"
    match["type"] = "led"
    match["symbol"] = []
    match["symbol"].append({"link": f"https://github.com/oomlout/oomlout_OOMP_eda_V2/tree/main/SYMBOL/kicad/kicad-symbols/Device/LED", 
                               "name": "Device : LED", 
                               "id":"SYMBOL-kicad-kicad-symbols-Device-LED",
                               "directory": "SYMBOL/kicad/kicad-symbols/Device/LED/"})
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