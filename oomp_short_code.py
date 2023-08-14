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
    replace_dict["type"]["button"] = "b"
    replace_dict["type"]["capacitor"] = "c"
    replace_dict["type"]["crystal"] = "x"
    replace_dict["type"]["diode_schottky"] = "ds"
    replace_dict["type"]["diode"] = "d"    
    replace_dict["type"]["ic"] = "i"
    replace_dict["type"]["mounting_hole"] = "mh"
    replace_dict["type"]["socket"] = "sc"
    replace_dict["type"]["pmic"] = "pm"
    replace_dict["type"]["header"] = "h"
    replace_dict["type"]["breakout_board"] = "bb"

    replace_dict["size"] = {}
    #loop for all mm sizes
    for mm in range(1, 100):
        replace_dict["size"][f"{mm}_mm"] = f"{mm}"
    replace_dict["size"][f"2d54_mm"] = f"i1"
    #loop for m1 to m10
    for m in range(1, 10):
        replace_dict["size"][f"m{m}"] = f"m{m}"
    
    replace_dict["size"]["0402"] = "4"

    replace_dict["size"]["0603"] = "6"
    replace_dict["size"]["0805"] = "8"
    replace_dict["size"]["1206"] = "12"
    replace_dict["size"]["3215"] = "3215"
    replace_dict["size"]["3213"] = "3213"
    replace_dict["size"]["3216_avx_a"] = "a"
    replace_dict["size"]["soic_28_wide"] = "soic28w"
    replace_dict["size"]["sod_123"] = "sod123"
    
    replace_dict["size"]["usb_mini"] = "umn"
    replace_dict["size"]["usb_micro"] = "umc"
    replace_dict["size"]["usb_c"] = "uc"

    for i in range(4, 28, 2):
        replace_dict["size"][f"soic_{i}"] = f"so{i}"
        replace_dict["size"][f"sop_{i}"] = f"sp{i}"
       
    ###### size ics
    ic_strings = []
    ic_strings.append(["dip","d"])
    ic_strings.append(["qfn","q"])
    ic_strings.append(["vqfn","vq"])
    ic_strings.append(["mlf","mlf"])
    ic_strings.append(["tqfp","tq"])
    for ic_string in ic_strings:
        for pin_count in range(2, 40,2):
            replace_dict["size"][f"{ic_string[0]}_{pin_count}"] = f"{ic_string[1]}{pin_count}"

    #pmic and transistorsizes
    replace_dict["size"]["to_252"] = "t252"
    replace_dict["size"]["sot_223"] = "s223"

    ##### dimension sizes
    replace_dict["size"]["3_5_mm_x_6_mm_x_2_5_mm"] = "3560"

    #### jst sizes
    replace_dict["size"]["_jst_ph"] = "jph"
    replace_dict["size"]["_jst_xh"] = "jxh"
    replace_dict["size"]["_jst_sh"] = "jsh"


    replace_dict["color"] = {}
    replace_dict["color"]["red"] = "r"
    replace_dict["color"]["green"] = "g"
    replace_dict["color"]["surface_mount"] = "s"
    replace_dict["color"]["tantalum"] = "t"

    replace_dict["description_main"] = {}
    replace_dict["description_main"][""] = ""
    replace_dict["description_main"]["tinted"] = "t"
    replace_dict["description_main"]["1117"] = "1117"

    replace_dict["description_main"]["surface_mount_only"] = "smo"

    #add for _pin 1-40
    for pin_count in range(1, 41):
        replace_dict["description_main"][f"{pin_count}_pin"] = f"{pin_count}p"
    
    #frequenzy
    frequencys = []
    frequencys.append(["hertz","hz"])
    frequencys.append(["kilo_hertz","khz"])
    frequencys.append(["mega_hertz","mhz"])
    for frequency in frequencys:
        for value in range(1, 100):
            replace_dict["description_main"][f"{value}_{frequency[0]}"] = f"{frequency[1]}{value}"

    #for capcitance farads
    capacitance_pairs = []
    capacitance_pairs.append(["nano_farad","nf"])
    capacitance_pairs.append(["micro_farad","uf"])
    capacitance_pairs.append(["pico_farad","pf"])
    for pair in capacitance_pairs:
        for value in range(1, 1000):
            replace_dict["description_main"][f"{value}_{pair[0]}"] = f"{pair[1]}{value}"

    replace_dict["description_main"][f"4_7_micro_farad"] = f"uf4d7"
    pass
    #loop for ohms resistors
    for num_zeros in range(0, 10):
        for start_digits in range(10, 100):
            ohms = start_digits * (10 ** num_zeros)
            code = f'{start_digits}{num_zeros}'
            replace_dict["description_main"][f"{ohms}_ohm"] = f"o{code}"

    ###### ics

        ###### atmega
    replace_dict["description_main"]["atmega328"] = "at328"

    replace_dict["description_extra"] = {}
    replace_dict["description_extra"][""] = ""

    #package_marking
    #needs to be in the loop

    replace_dict["description_extra"]["1_5v"] = "1d5v"
    replace_dict["description_extra"]["1_8v"] = "1d8v"
    replace_dict["description_extra"]["2_5v"] = "2d5v"
    replace_dict["description_extra"]["2_85v"] = "2d85v"
    replace_dict["description_extra"]["3_3v"] = "3d3v"

    ## header ones
    replace_dict["description_extra"]["right_angle"] = "ra"
    replace_dict["description_extra"]["surface_mount"] = "sm"
    replace_dict["description_extra"]["surface_mount_right_angle"] = "smra"

    replace_dict["manufacturer"] = {}
    replace_dict["manufacturer"][""] = ""

    replace_dict["part_number"] = {}
    replace_dict["part_number"]["aip1640"] = "aip1640"
    replace_dict["part_number"]["ch340c"] = "ch340c"

    #make a copy of kwargs
    kwargs_copy = kwargs.copy()
    #make the short code by taking the values keys from names of main elements and replacing them with the values from the replace dict to create the string short_code
    short_code = ""
    for name in oomp.names_of_main_elements:
        #get the value from the replace dict
        try:            
            if name == "description_extra":
                if "package_marking" in kwargs_copy[name]:
                    replace_value = f'pm{kwargs_copy["description_extra"].replace("package_marking_","")}'    
                    pass 
                else:
                    replace_value = replace_dict[name][kwargs_copy[name]]                   
            else:
                replace_value = replace_dict[name][kwargs_copy[name]]
            #add the replace value to the short code            
            short_code += replace_value
        except:
            pass
            #skip if not in a match array
    #try to replace_package_marking
    


    return short_code
