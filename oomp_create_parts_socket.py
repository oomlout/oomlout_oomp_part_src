import oomp
import copy 

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    # variables
    pins = {}
    pins["pin_1"] = ({"name": "vbus", "number": "1", "type": "power"})
    pins["pin_2"] = ({"name": "usb_negative", "number": "2", "type": "signal"})
    pins["pin_3"] = ({"name": "usb_positive", "number": "3", "type": "signal"})
    pins["pin_4"] = ({"name": "gnd", "number": "4", "type": "signal"})
    pins["pin_5"] = ({"name": "shield", "number": "6", "type": "signal"})    
    pins_usb_a = copy.deepcopy(pins)

    pins = {}
    pins["pin_1"] = ({"name": "vbus", "number": "1", "type": "power"})
    pins["pin_2"] = ({"name": "usb_negative", "number": "2", "type": "signal"})
    pins["pin_3"] = ({"name": "usb_positive", "number": "3", "type": "signal"})
    pins["pin_4"] = ({"name": "id", "number": "4", "type": "signal"})
    pins["pin_5"] = ({"name": "gnd", "number": "5", "type": "power"})
    pins["pin_6"] = ({"name": "shield", "number": "6", "type": "signal"})
    pins_usb_micro = copy.deepcopy(pins)
    pins_usb_mini = copy.deepcopy(pins)

    #define a part 


    # usb

    #      type a
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "socket"
    part_details["size"] = ["usb_a"]
    part_details["color"] = [""]
    part_details["description_main"] = "through_hole"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = ""    
    parts.append(part_details)
    
    pins = copy.deepcopy(pins_usb_a)
    part_details["pins"] = pins
    
    #      type c
    ## omers on oshcamp badge #lcsc C165948

    #      micro
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "socket"
    part_details["size"] = ["usb_micro"]
    part_details["color"] = [""]
    part_details["description_main"] = "surface_mount"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = ""    
    parts.append(part_details)

    pins = copy.deepcopy(pins_usb_micro)
    part_details["pins"] = pins
    

    #      mini
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "socket"
    part_details["size"] = ["usb_mini"]
    part_details["color"] = [""]
    part_details["description_main"] = "surface_mount_only"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = ""    
    parts.append(part_details)
    
    pins = copy.deepcopy(pins_usb_mini)
    part_details["pins"] = pins   

    
    
    oomp.add_parts(parts, make_files=make_files)
    