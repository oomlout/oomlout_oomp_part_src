import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 

    ## color used for chip type

    

    
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "button"
    part_details["size"] = ["3_5_mm_x_6_mm_x_2_5_mm"]
    part_details["color"] = ["surface_mount"]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = ""  
    part_details["distributors"] = []
    parts.append(part_details)

    #switches
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "slide_switch"
    part_details["size"] = ["2_8_mm_x_8_mm_x_1_4_mm","2d54_header"]
    part_details["color"] = ["surface_mount"]
    part_details["description_main"] = "single_pole_double_throw"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = ""  
    part_details["distributors"] = []
    parts.append(part_details)
    

    
    oomp.add_parts(parts, make_files=make_files)
    