import oomp

import oomp

def get_extra_details(**kwargs):
    matches = []

    ###### 
    # screw
    #      flat_head    
    match = {}
    match["id"] = "hardware_screw_flat_head_2_5_mm_black_4_mm_phillips"
    match["extra_data"] = {}
    match["extra_data"].update({"weight": 3.38/20})
    matches.append(match)

    # standoff
    #      nut_and_nut
    match = {}
    match["id"] = "hardware_standoff_2_5_mm_black_10_mm_nut_and_nut"
    match["extra_data"] = {}
    match["extra_data"].update({"weight": 11.54/10})
    matches.append(match)

    #      screw_and_nut
    match = {}
    match["id"] = "hardware_standoff_2_5_mm_black_12_mm_screw_and_nut"
    match["extra_data"] = {}
    match["extra_data"].update({"weight": 15.89/10})
    matches.append(match)

    
    
    

     #go through the keys in oomp.names_of_main_elements if all the values in match match (ignore non mentioned keys) then add it to footprints
    for match in matches:
        match_count = 0
        # get a list with oomp.names_of_main_elements and "id"
        elements_to_check = oomp.names_of_main_elements.copy()
        elements_to_check.append("id")
        for name in elements_to_check:
            try:
                if match[name] == kwargs[name]:
                    match_count += 1
                    print("match")
            except:
                pass
                #value not in match check
        if match_count == len(match)-1:
            kwargs.update(match["extra_data"])

    return kwargs