import oomp

def get_short_code(**kwargs):
    replace_dict = {}
    #add a dict replace for each of the calues in but dont use a loop
    replace_dict["classification"] = {}
    replace_dict["classification"]["electronic"] = ""
    replace_dict["classification"]["mechanical"] = ""
    replace_dict["classification"]["optical"] = ""
    

    replace_dict["type"] = {}
    replace_dict["type"]["led"] = "l"
    replace_dict["type"]["resistor"] = "r"
    replace_dict["type"]["capacitor"] = "c"
    replace_dict["type"]["ic"] = "i"
    replace_dict["type"]["mounting_hole"] = "mh"
    replace_dict["type"]["header"] = "h"
    replace_dict["type"]["breakout_board"] = "b"

    replace_dict["size"] = {}
    #loop for all mm sizes
    for mm in range(1, 100):
        replace_dict["size"][f"{mm}_mm"] = f"{mm}"
    replace_dict["size"][f"2d54_mm"] = f"i1"
    #loop for m1 to m10
    for m in range(1, 10):
        replace_dict["size"][f"m{m}"] = f"m{m}"
    
    replace_dict["size"]["0402"] = "6"
    replace_dict["size"]["0603"] = "6"
    replace_dict["size"]["0805"] = "8"
    replace_dict["size"]["1206"] = "12"
    replace_dict["size"]["soic_28_wide"] = "soic28w"
    

    #### jst sizes
    replace_dict["size"]["_jst_ph"] = "jph"
    replace_dict["size"]["_jst_xh"] = "jxh"
    replace_dict["size"]["_jst_sh"] = "jsh"


    replace_dict["color"] = {}
    replace_dict["color"]["red"] = "r"
    replace_dict["color"]["green"] = "g"

    replace_dict["description_main"] = {}
    replace_dict["description_main"][""] = ""
    replace_dict["description_main"]["tinted"] = "t"
    #add for _pin 1-40
    for pin_count in range(1, 41):
        replace_dict["description_main"][f"{pin_count}_pin"] = f"{pin_count}p"
    #loop for ohms
    for num_zeros in range(0, 10):
        for start_digits in range(10, 100):
            ohms = start_digits * (10 ** num_zeros)
            code = f'{start_digits}{num_zeros}'
            replace_dict["description_main"][f"{ohms}_ohm"] = f"o{code}"


    replace_dict["description_extra"] = {}
    replace_dict["description_extra"][""] = ""

    ## header ones
    replace_dict["description_extra"]["right_angle"] = "ra"
    replace_dict["description_extra"]["surface_mount"] = "sm"
    replace_dict["description_extra"]["surface_mount_right_angle"] = "smra"

    replace_dict["manufacturer"] = {}
    replace_dict["manufacturer"][""] = ""

    replace_dict["part_number"] = {}
    replace_dict["part_number"]["aip1640"] = "aip1640"

    #make a copy of kwargs
    kwargs_copy = kwargs.copy()
    #make the short code by taking the values keys from names of main elements and replacing them with the values from the replace dict to create the string short_code
    short_code = ""
    for name in oomp.names_of_main_elements:
        #get the value from the replace dict
        try:
            replace_value = replace_dict[name][kwargs_copy[name]]
            #add the replace value to the short code
            short_code += replace_value
        except:
            pass
            #skip if not in a match array


    return short_code
