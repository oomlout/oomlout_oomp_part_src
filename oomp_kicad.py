import oomp

import os

from kiutils.footprint import Footprint
from kiutils.symbol import SymbolLib, Symbol

def create_footprint_library():
    print("creating footprint library")
    #footprint_directory = rf'kicad\footprints\oomlout_oomp_kicad_footprints.pretty'
    #make if it doesn't exist
    footprint_directory = "c:/gh/oomlout_oomp_part_kicad_footprints/oomlout_oomp_part_footprints.pretty"
    if not os.path.exists(footprint_directory):
        os.makedirs(footprint_directory)
    #delete all the files in the directory
    for root, dirs, files in os.walk(footprint_directory):
        for file in files:
            os.remove(os.path.join(root, file))
    src_footprints_base = rf'tmp'
    
    # go thrpough each part in oomp.parts
    for part in oomp.parts:
        #if they have a footprint
        part = oomp.parts[part]
        if "footprint" in part:
            #go through each footprint
            extra = 0
            for footprint in part["footprint"]:
                extra_string = ""
                if extra != 0:
                    extra_string = f'_{str(extra)}'
                #make footprint_name
                footprint_name = f'{part["short_code"]}_{part["id"]}'
                footprint_filename = f'{footprint_directory}\{footprint_name}{extra_string}.kicad_mod'
                directory = footprint["directory"]
                filename = rf'{src_footprints_base}\{directory}'
                #convert \\ to /
                filename = filename.replace("\\", "/")
                #rmove doubles
                filename = filename.replace("//", "/")
                #if the footprint file exists
                if os.path.isfile(filename):
                    #create a footprint object
                    filename = filename.replace("/", "\\")
                    footprint_object = Footprint.from_file(filename)
                    #add the footprint to the footprint library
                    footprint_object.to_file(footprint_filename)
                    #print a dot
                    print(".", end="", flush=True)
                else:
                    print(f'footprint file not found: {filename}')
                extra += 1


def create_symbol_library():
    print("creating symbol library")
    symbol_file_source = rf'templates\template_oomlout_oomp_kicad_symbols.kicad_sym'
    #symbol_file =  rf'kicad\symbols\oomlout_oomp_kicad_symbols.kicad_sym' 
    symbol_file = "c:/gh/oomlout_oomp_part_kicad_symbols/oomlout_oomp_part_symbols.kicad_sym"
    #if the directory doesn't exist make it
    if not os.path.exists(os.path.dirname(symbol_file)):
        os.makedirs(os.path.dirname(symbol_file))
    #delete the file if it exists
    if os.path.isfile(symbol_file):
        os.remove(symbol_file)
    oomlout_oomp_symbol_bot = rf'tmp/oomlout_oomp_symbol_bot/symbols'
    symbol_library = SymbolLib.from_file(symbol_file_source)
    for part_id in oomp.parts:
        part = oomp.parts[part_id]  
        symbol_output_name = f'{part["short_code"]}_{part["id"]}'
        
        symbol = None
        if "symbol" in part:
            #if there's a symbol copy it across
            #symbol_source = oomlout_v2_eda_base + "/" + part["symbol"][0]["directory"] + "symbol.kicad_sym"
            symbol_source = rf'tmp/{part["symbol"][0]["directory"]}'
            #convert \\ to /
            symbol_source = symbol_source.replace("\\", "/")
            #rmove doubles
            symbol_source = symbol_source.replace("//", "/")
            if os.path.isfile(symbol_source):                
                symbol = SymbolLib.from_file(symbol_source).symbols[0]
                pass
            else:
                #raise exception that file doesn't exist
                #raise Exception(f'file not found: {symbol_source}')
                print(f'symbol file not found: {symbol_source}')
                pass
        elif "pins" in part:
            # make it from the base symbol
            number_of_pins = str(len(part["pins"])).zfill(2)
            symbol_source = rf'{oomlout_oomp_symbol_bot}/kicad_connector_conn_01x{number_of_pins}_pin/working/working.kicad_sym'
            symbol_source
            symbol = SymbolLib.from_file(symbol_source).symbols[0]
            for sym in symbol.units:            
                pins = sym.pins
                for pin in pins:
                    index = pin.name.replace("Pin_", "")
                    pin.name = "   " + part["pins"][index]["name"]
        if symbol != None:
            #change the name
            symbol.pinNamesHide = False
            name = symbol_output_name   
            #name = 'Conn_01x28'   
            try:
                name_old = symbol.id
            except:
                #some have an entry name instead of an id
                name_old = symbol.entryName
            symbol.id = name
            symbol.entryName = name
            #yaml dump symbol to a file called test.yaml using yaml library
            #import yaml
            #with open("test.yaml", "w") as outfile:
            #    yaml.dump(symbol, outfile, indent=4)

            
            for sym in symbol.units:    
                try:        
                    unit_name_old = sym.id
                except:
                    #some have an entry name instead of an id
                    unit_name_old = sym.entryName
                sym.id = unit_name_old.replace(name_old, name)    
                sym.entryName = unit_name_old.replace(name_old, name)        
            for property in symbol.properties:
                if property.key == "Value":
                    pass
                    property.value = f'{symbol_output_name}'
                if property.key == "Datasheet":
                    pass
                    property.value = f'https://github.com/oomlout/oomlout_oomp_v3/parts/{part["id"]}/datasheet.pdf'
                if property.key == "Footprint":
                    pass
                    property.value = f"oomlout_oomp_part_footprints:{symbol_output_name}"
                if property.key == "Reference":
                    pass
                    property.value = part.get("kicad_reference", "J")
            #print(f'adding symbol {symbol_output_name} to library')
            # print a dot
            print(".", end="", flush=True)
            symbol_library.symbols.append(symbol)
        else:
            print(f'no symbol for {symbol_output_name}')
    #if symbol_file exists delete it
    if os.path.isfile(symbol_file):
        os.remove(symbol_file)
    symbol_library.to_file(symbol_file)


