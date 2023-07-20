import oomp

def load_parts():
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    mounting_hole_symbol = {"link": "https://github.com/oomlout/oomlout_OOMP_eda_V2/tree/main/SYMBOL/kicad/kicad-symbols/Mechanical/MountingHole", 
                               "name": "Mechanical : MountingHole", 
                               "id":"SYMBOL-kicad-kicad-symbols-Mechanical-MountingHole",
                               "directory": "SYMBOL/kicad/kicad-symbols/Mechanical/MountingHole/"}
    

    #define a part 
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "mounting_hole"
    part_details["size"] = ["m3"]
    part_details["color"] = [""]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "H"
    part_details["notes"] = []
    part_details["footprint"] = []
    part_details["footprint"].append({"link": "https://github.com/oomlout/oomlout_OOMP_eda_V2/tree/main/FOOTPRINT/kicad/kicad-footprints/MountingHole/MountingHole_3.2mm_M3", 
                               "name": "MountingHole : MountingHole_3.2mm_M3", 
                               "id":"FOOTPRINT-kicad-kicad-footprints-MountingHole-MountingHole_3.2mm_M3",
                               "directory": "FOOTPRINT/kicad/kicad-footprints/MountingHole/MountingHole_3.2mm_M3/"})
    part_details["symbol"] = [] 
    part_details["symbol"].append(mounting_hole_symbol)
    #add the part to the list of parts
    parts.append(part_details)


    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "mounting_hole"
    part_details["size"] = ["m6"]
    part_details["color"] = [""]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "H"
    part_details["notes"] = []
    part_details["footprint"] = []
    part_details["footprint"].append({"link": "https://github.com/oomlout/oomlout_OOMP_eda_V2/tree/main/FOOTPRINT/kicad/kicad-footprints/MountingHole/MountingHole_6.4mm_M6", 
                               "name": "MountingHole : MountingHole_6.4mm_M6", 
                               "id":"FOOTPRINT-kicad-kicad-footprints-MountingHole-MountingHole_6.4mm_M6",
                               "directory": "FOOTPRINT/kicad/kicad-footprints/MountingHole/MountingHole_6.4mm_M6/"})
   
    part_details["symbol"] = [] 
    part_details["symbol"].append(mounting_hole_symbol)
    #add the part to the list of parts
    parts.append(part_details)

    
    oomp.add_parts(parts)
    