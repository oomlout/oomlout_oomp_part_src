import oomp
import oomp_kicad_symbol

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    
    #define a part 
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "mounting_hole"
    part_details["size"] = ["m3","m6"]
    part_details["color"] = [""]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "H"
    part_details["notes"] = []
    #add the part to the list of parts
    parts.append(part_details)

    
    oomp.add_parts(parts, make_files=make_files)
    