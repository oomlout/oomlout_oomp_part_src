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

    replace_dict["size"] = {}
    replace_dict["size"]["5_mm"] = "5"
    replace_dict["size"]["10_mm"] = "10"
    replace_dict["size"]["0603"] = "63"
    replace_dict["size"]["sop_28"] = "sop28"

    replace_dict["color"] = {}
    replace_dict["color"]["red"] = "r"
    replace_dict["color"]["green"] = "g"

    replace_dict["description_main"] = {}
    replace_dict["description_main"][""] = ""
    replace_dict["description_main"]["tinted"] = "t"

    replace_dict["description_extra"] = {}
    replace_dict["description_extra"][""] = ""

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
