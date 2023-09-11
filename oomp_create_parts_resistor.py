import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    
    #e12 array
    base_values = [10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 75, 82]

    # Number of decades you want to cover (e.g., from ohm to megaohm would be 7 decades: 10^0 to 10^6)
    num_decades = 6

    resistor_values = []
    for i in range(num_decades):
        for base in base_values:
            value = base * (10 ** i)
            resistor_string = f"{value}_ohm"
            
            resistor_values.append(resistor_string)
    resistor_values.append("10000000_ohm")
    resistor_values.append("1000000_ohm")
    resistor_values.append("100000_ohm")


    #define a part 
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "resistor"
    part_details["size"] = ["quarter_watt_through_hole","0201","0402","0603","0805","1206"]
    part_details["color"] = [""]
    #part_details["description_main"] = ["220_ohm","330_ohm","560_ohm","1000_ohm","2200_ohm","10000_ohm"]
    #e12 values
    part_details["description_main"] = resistor_values
    
    part_details["description_extra"] = [""]
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "R"

    #add the part to the list of parts
    parts.append(part_details)

    
    oomp.add_parts(parts, **kwargs)
    