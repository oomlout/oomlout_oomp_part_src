import oomp

def get_distributors(**kwargs):
    kwargs = get_lcsc(**kwargs)
    kwargs = get_aliexpress(**kwargs)

    return kwargs

def get_lcsc(**kwargs):

    matches = []
    matches.append({"id":"electronic_ic_sop_28_led_matrix_driver_16_x_8_wuxi_i_core_electronics_co_ltd_aip1640",
                  "part_number": "c82650"})
    matches.append({"id":"converter_usb_to_serial_converter_wch_ch340c",
                  "part_number": "c7464026"})
    matches.append({"id":"converter_usb_to_serial_converter_wch_ch340g",
                  "part_number": "c14267"})
    matches.append({"id":"converter_usb_to_serial_converter_wch_ch340e",
                  "part_number": "c99652"})
    matches.append({"id":"econverter_usb_to_serial_converter_wch_ch340x",
                  "part_number": "c3035748"})
    matches.append({"id":"converter_usb_to_serial_converter_wch_ch340t",
                  "part_number": "c8689"})
    matches.append({"id":"converter_usb_to_serial_converter_wch_ch340n",
                  "part_number": "c2977777"})
    matches.append({"id":"converter_usb_to_serial_converter_wch_ch340k",
                  "part_number": "c968586"})
    matches.append({"id":"converter_usb_to_serial_converter_wch_ch340b",
                  "part_number": "c81010"})

    distributors = []
    for match in matches:
        #jus check th id
        if match["id"] in kwargs["id"]:
            distributor_match = {}
            distributor_match["name"] = "LCSC"
            distributor_match["part_number"] = match["part_number"]
            distributor_match["link"] = "https://lcsc.com/product-detail/LED-Drivers_AIP1640_C82650.html"
            distributor_match["id"] = "distributor_lcsc"            
            distributors.append(distributor_match)
    
    #if there are no kwargs[distributers]
    if "distributors" not in kwargs:
        kwargs["distributors"] = []
        
    #add the distributors to kwargs[distributors]
    kwargs["distributors"].extend(distributors)



    
    return kwargs

def get_aliexpress(**kwargs):
    matches = []
    matches.append({"id":"electronic_ic_sop_28_led_matrix_driver_16_x_8_wuxi_i_core_electronics_co_ltd_aip1640",
                  "part_number": "aip1640"})
    

    distributors = []
    for match in matches:
        #jus check th id
        if match["id"] == kwargs["id"]:
            distributor_match = {}
            distributor_match["name"] = "AliExpress"
            distributor_match["part_number"] = f'search: {match["part_number"]}'
            distributor_match["link"] = f"https://www.aliexpress.com/w/wholesale-aip1640.htmlSearchText={match['part_number']}"            
            distributor_match["id"] = "distributor_aliexpress"            
            distributors.append(distributor_match)

    #if there are no kwargs[distributers]
    if "distributors" not in kwargs:
        kwargs["distributors"] = []
        
    #add the distributors to kwargs[distributors]
    kwargs["distributors"].extend(distributors)

    return kwargs