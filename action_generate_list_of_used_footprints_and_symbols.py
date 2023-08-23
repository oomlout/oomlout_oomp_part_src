import oomp



def main(**kwargs):
    oomp.load_parts(from_pickle = True)
    list_symbol = []
    list_footprint = []
    for part_id in oomp.parts:        
        part = oomp.parts[part_id]
        footprints = part.get("footprint", [])
        for footprint in footprints:
            footprint_id = footprint.get("oomp_key", "")
            if footprint_id != "":
                list_footprint.append(footprint_id)
        symbols = part.get("symbol", [])
        for symbol in symbols:
            symbol_id = symbol.get("oomp_key", "")
            if symbol_id != "":
                list_symbol.append(symbol_id)
    #remove duplicates
    list_symbol = list(set(list_symbol))
    list_footprint = list(set(list_footprint))
    # sort alphabetically
    list_symbol.sort()
    list_footprint.sort()

    file_footprint = "used_footprints.yaml"
    file_symbol = "used_symbols.yaml"
    import yaml
    with open(file_footprint, "w") as outfile:
        yaml.dump(list_footprint, outfile)
    with open(file_symbol, "w") as outfile:
        yaml.dump(list_symbol, outfile)



if __name__ == "__main__":
    main()