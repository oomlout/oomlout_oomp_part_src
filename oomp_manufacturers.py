import oomp

def get_manufacturers(**kwargs):
    kwargs = get_jst(**kwargs)   
    kwargs = get_kyocera(**kwargs)       
    kwargs = get_lcsc(**kwargs)

    kwargs = get_microchip(**kwargs)
    kwargs = get_murata(**kwargs)
    kwargs = get_samsung(**kwargs)
    kwargs = get_uniroyal(**kwargs)
    kwargs = get_yageo(**kwargs)


    return kwargs

def get_jst(**kwargs):
    matches = []
    for pins in range(2, 11):
        pins_s = str(pins).zfill(2)
        matches.append({"id":f"electronic_header_1_mm_jst_sh_{pins}_pin_surface_mount",
                  "part_number": f"BM{pins_s}B-SRSS-TB"})
        matches.append({"id":f"electronic_header_1_mm_jst_sh_{pins}_pin_surface_mount_right_angle",
                  "part_number": f"SM{pins_s}B-SRSS-TB"})
    

    manufacturers = []
    for match in matches:
        #jus check th id
        if match["id"].replace("oomp_","") in kwargs["id"]:

            manufacturer_match = {}
            manufacturer_match["name"] = "JST"
            manufacturer_match["part_number"] = match["part_number"]
            if "1_mm_jst_sh" in match["id"]:
                manufacturer_match["link"] = f"https://www.jst-mfg.com/product/index.php?series=231"
            else:
                manufacturer_match["link"] = f"https://www.jst.com/?s={match['part_number']}"
            manufacturer_match["id"] = "manufacturer_jst"            
            manufacturers.append(manufacturer_match)
    
    #if there are no kwargs[distributers]
    if "manufacturers" not in kwargs:
        kwargs["manufacturers"] = []
        
    #add the manufacturers to kwargs[manufacturers]
    kwargs["manufacturers"].extend(manufacturers)

    return kwargs

def get_kyocera(**kwargs):
    matches = []
    matches.append({"id":"oomp_electronic_capacitor_3216_avx_a_tantalum_4_7_micro_farad_16_volt",
                  "part_number": "TAJA475K016RNJ"})
    

    manufacturers = []
    for match in matches:
        #jus check th id
        if match["id"].replace("oomp_","") in kwargs["id"]:
            manufacturer_match = {}
            manufacturer_match["name"] = "Kyocera"
            manufacturer_match["part_number"] = match["part_number"]
            manufacturer_match["link"] = f"https://search.kyocera-avx.com/search/{match['part_number']}"
            manufacturer_match["id"] = "manufacturer_kyocera"            
            manufacturers.append(manufacturer_match)
    
    #if there are no kwargs[distributers]
    if "manufacturers" not in kwargs:
        kwargs["manufacturers"] = []
        
    #add the manufacturers to kwargs[manufacturers]
    kwargs["manufacturers"].extend(manufacturers)

    return kwargs

def get_lcsc(**kwargs):
    matches = []
    matches.append({"id":"oomp_electronic_capacitor_0603_22_pico_farad",
                    "name":"HCTL",
                    "part_number": "TC-3601L-2.5-260G",
                    "link": "",
                    "manufacturer_id": "manufacturer_hctl"
                    })
    
    matches.append({"id":"oomp_electronic_pmic_sot_223_linear_1117_5_volt",
                    "name":"UMW(Youtai Semiconductor Co., Ltd.)",
                    "part_number": "AMS1117-5.0",
                    "link": "",
                    "manufacturer_id": "manufacturer_umw_youtai_semiconductor_co_ltd"
                    })
    # led 0603
    matches.append({"id":"oomp_electronic_led_0603_red",
                    "name":"XINGLIGHT",
                    "part_number": "XL-1608SURC-06",
                    "link": "",
                    "manufacturer_id": "manufacturer_xinglight"
                    })
    matches.append({"id":"oomp_electronic_led_0603_green",
                    "name":"XINGLIGHT",
                    "part_number": "XL-1608UGC-04",
                    "link": "",
                    "manufacturer_id": "manufacturer_xinglight"
                    })
    matches.append({"id":"oomp_electronic_led_0603_blue",
                    "name":"XINGLIGHT",
                    "part_number": "XL-1608UBC-04",
                    "link": "",
                    "manufacturer_id": "manufacturer_xinglight"
                    })
    matches.append({"id":"oomp_electronic_led_0603_yellow",
                    "name":"XINGLIGHT",
                    "part_number": "XL-1608UYC-06",
                    "link": "",
                    "manufacturer_id": "manufacturer_xinglight"
                    })
    
    matches.append({"id":"oomp_electronic_led_0603_white",
                    "name":"XINGLIGHT",
                    "part_number": "XL-1608UWC-04",
                    "link": "",
                    "manufacturer_id": "manufacturer_xinglight"
                    })
    
    matches.append({"id":"oomp_electronic_diode_schottky_sod_123_package_marking_b2_mbr0520",
                    "name":"Jiangsu Changjing Electronics Technology Co., Ltd.",
                    "part_number": "MBR0520",
                    "link": "",
                    "manufacturer_id": "manufacturer_jiangsu_changjing_electronics_technology_co_ltd"
                    })
    matches.append({"id":"oomp_electronic_diode_schottky_sod_123_package_marking_b2_mbr0520",
                    "name":"Shikues",
                    "part_number": "MBR0520",
                    "link": "",
                    "manufacturer_id": "manufacturer_shikues"
                    })
    matches.append({"id":"oomp_electronic_diode_schottky_sod_123_package_marking_b2_mbr0520",
                    "name":"onsemi",
                    "part_number": "MBR0520LT3G",
                    "link": "",
                    "manufacturer_id": "manufacturer_onsemi"
                    })
    matches.append({"id":"oomp_electronic_ic_lga_2_5_mm_x_2_5_mm_8_pin_sensor_pressure_temperature_bosch_bme280",
                    "name":"Bosch",
                    "part_number": "BME280",
                    "link": "https://www.bosch-sensortec.com/products/environmental-sensors/humidity-sensors-bme280/",
                    "manufacturer_id": "manufacturer_bosch"
                    })

    ##### socket
    #      usb
    #            mini
    matches.append({"id":"oomp_electronic_socket_usb_mini_surface_mount_only",
                    "name":"Korean Hroparts Elec",
                    "part_number": "U-M-M5SS-W-2",
                    "link": "",
                    "manufacturer_id": "manufacturer_korean_hroparts_elec"
                    })


    manufacturers = []
    for match in matches:
        #jus check th id
        if match["id"].replace("oomp_","") in kwargs["id"]:
            manufacturer_match = {}
            manufacturer_match["name"] = match["name"]
            manufacturer_match["part_number"] = match["part_number"]
            manufacturer_match["link"] = match["link"]
            manufacturer_match["id"] = match["manufacturer_id"]
            manufacturers.append(manufacturer_match)

    #if there are no kwargs[distributers]
    if "manufacturers" not in kwargs:
        kwargs["manufacturers"] = []
    
    #add the manufacturers to kwargs[manufacturers]
    kwargs["manufacturers"].extend(manufacturers)

    return kwargs

def get_microchip(**kwargs):
    matches = []

    part = "oomp_electronic_ic_tqfp_32_mcu_atmega328_microchip_atmega328p_au"
    matches.append({"id":part,"part_number": "ATMEGA328P-AU"})
    matches.append({"id":part,"part_number": "ATMEGA328P-AUR"})
    

    
    manufacturers = []
    for match in matches:
        #jus check th id
        if match["id"].replace("oomp_","") in kwargs["id"]:
            manufacturer_match = {}
            manufacturer_match["name"] = "Microchip"
            manufacturer_match["part_number"] = match["part_number"]
            manufacturer_match["link"] = f"https://www.microchip.com/wwwproducts/en/{match['part_number']}"
            manufacturer_match["id"] = "manufacturer_microchip"            
            manufacturers.append(manufacturer_match)

    #if there are no kwargs[manufacturers]
    if "manufacturers" not in kwargs:
        kwargs["manufacturers"] = []
    
    #add the manufacturers to kwargs[manufacturers]
    kwargs["manufacturers"].extend(manufacturers)

    return kwargs


def get_murata(**kwargs):
    matches = []

    part = "oomp_electronic_ceramic_resonator_3213_3_pin_ground_pin_2_12_mega_hertz"
    matches.append({"id":part,"part_number": "CSTNE12M0G550000R0"})
    part = "oomp_electronic_ceramic_resonator_3213_3_pin_ground_pin_2_16_mega_hertz"
    matches.append({"id":part,"part_number": "CSTNE16M0VH3C000R0"})
    

    
    manufacturers = []
    for match in matches:
        #jus check th id
        if match["id"].replace("oomp_","") in kwargs["id"]:
            manufacturer_match = {}
            manufacturer_match["name"] = "Murata"
            manufacturer_match["part_number"] = match["part_number"]
            manufacturer_match["link"] = f"https://www.murata.com/en-eu/products/productdetail?cate=cgsubResonators&partno={match['part_number']}"
            manufacturer_match["id"] = "manufacturer_murata"            
            manufacturers.append(manufacturer_match)

    #if there are no kwargs[manufacturers]
    if "manufacturers" not in kwargs:
        kwargs["manufacturers"] = []
    
    #add the manufacturers to kwargs[manufacturers]
    kwargs["manufacturers"].extend(manufacturers)

    return kwargs

def get_samsung(**kwargs):
    matches = []
    # capacitors
    matches.append({"id":"oomp_electronic_capacitor_0603_100_nano_farad",
                  "part_number": "CL10B104KB8NNNC"})
    
    manufacturers = []
    for match in matches:
        #jus check th id
        if match["id"].replace("oomp_","") in kwargs["id"]:
            manufacturer_match = {}
            manufacturer_match["name"] = "Samsung"
            manufacturer_match["part_number"] = match["part_number"]
            link_num = match["part_number"][0:-1]
            manufacturer_match["link"] = f"https://product.samsungsem.com/mlcc/{link_num}.do"
            manufacturer_match["id"] = "manufacturer_samsung"            
            manufacturers.append(manufacturer_match)
    
    #if there are no kwargs[distributers]
    if "manufacturers" not in kwargs:
        kwargs["manufacturers"] = []
        
    #add the manufacturers to kwargs[manufacturers]
    kwargs["manufacturers"].extend(manufacturers)

    return kwargs

def get_uniroyal(**kwargs):
    matches = []

    sizes = ["0201", "0402", "0603", "0805", "1206"]
    base_values = [10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82]
    # size text    
    st = {}
    st["0201"] = "NQ01"
    st["0402"] = "0402"
    st["0603"] = "0603"
    st["0805"] = "0805"
    st["1206"] = "1206"
    # first letters
    fl = {}
    fl["0201"] = "WMJ"
    fl["0402"] = "WGJ"
    fl["0603"] = "WAJ"
    fl["0805"] = "W8J"
    fl["1206"] = "W4J"
    #second letters
    sl = {}
    sl["0201"] = "TEE"
    sl["0402"] = "TCE"
    sl["0603"] = "T5E"
    sl["0805"] = "T5E"
    sl["1206"] = "T5E"
    #matches.append({"id":"oomp_electronic_resistor_0603_1000_ohm",
    #              "part_number": "0603WAF1001T5E"})
    #matches.append({"id":"oomp_electronic_resistor_0603_10000_ohm",
    #              "part_number": "0603WAF1002T5E"})
    
    #### pattern matching attempt
    num_decades = 4
    resistor_values = []
    for size in sizes:
        for i in range(num_decades):
            for base in base_values:
                value = base * (10 ** i)
                resistor_string = f"{value}_ohm"
                id = f"oomp_electronic_resistor_{size}_{resistor_string}"
                first_three_digits = str(value)[0:2].zfill(3)
                number_of_trailing_zeros = len(str(value)) - 2
                part_number = f'{st[size]}{fl[size]}{first_three_digits}{number_of_trailing_zeros}{sl[size]}'
                matches.append({"id":id,
                                "part_number": part_number})

    manufacturers = []
    for match in matches:
        #jus check th id
        if match["id"].replace("oomp_","") in kwargs["id"]:
            manufacturer_match = {}
            manufacturer_match["name"] = "Uniroyal"
            manufacturer_match["part_number"] = match["part_number"]
            manufacturer_match["link"] = f""
            manufacturer_match["id"] = "manufacturer_uniroyal"            
            manufacturers.append(manufacturer_match)
    
    #if there are no kwargs[distributers]
    if "manufacturers" not in kwargs:
        kwargs["manufacturers"] = []
        
    #add the manufacturers to kwargs[manufacturers]
    kwargs["manufacturers"].extend(manufacturers)

    return kwargs


def get_yageo(**kwargs):
    matches = []
    # capacitors
    matches.append({"id":"oomp_electronic_capacitor_0603_22_pico_farad",
                  "part_number": "CC0603JRNPO9BN220"})
    matches.append({"id":"oomp_electronic_capacitor_0603_100_nano_farad",
                  "part_number": "CC0603KRX7R9BB104"})
    matches.append({"id":"oomp_electronic_capacitor_0603_10_nano_farad",
                  "part_number": "CC0603KRX7R9BB103"})
    #resistors
    #matches.append({"id":"oomp_electronic_resistor_0603_1000_ohm",
    #                "part_number": "RC0603FR-071KL"})
    #matches.append({"id":"oomp_electronic_resistor_0603_10000_ohm",
    #                "part_number": "RC0603FR-0710KL"})
    
    sizes = ["0402", "0603", "0805", "1206"]
    base_values = [10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82]
    # size text    
    st = {}
    st["0201"] = "0201"
    st["0402"] = "0402"
    st["0603"] = "0603"
    st["0805"] = "0805"
    st["1206"] = "1206"
    # first letters
    fl = {}
    fl["0201"] = "RC"
    fl["0402"] = "RC"
    fl["0603"] = "RC"
    fl["0805"] = "RC"
    fl["1206"] = "RC"
    #second letters
    sl = {}
    sl["0201"] = "JR-07"
    sl["0402"] = "JR-07"
    sl["0603"] = "JR-07"
    sl["0805"] = "JR-07"
    sl["1206"] = "JR-07"
    #### when coming to do 1% I think just change JR to FR
    
    #### pattern matching attempt
    num_decades = 4
    resistor_values = []
    for size in sizes:
        for i in range(num_decades):
            for base in base_values:
                value = base * (10 ** i)
                resistor_string = f"{value}_ohm"
                id = f"oomp_electronic_resistor_{size}_{resistor_string}"
                if value < 1000:
                    value_string = f"{value}R"
                elif value < 1000000:
                    v = value/1000
                    #round to nearest whole number
                    v = round(v)
                    value_string = f"{v}K"
                else:
                    v = value/1000000
                    #round to nearest whole number
                    v = round(v)
                    value_string = f"{v}M"
                part_number = f'{fl[size]}{st[size]}{sl[size]}{value_string}L'
                matches.append({"id":id,
                                "part_number": part_number})


    manufacturers = []
    for match in matches:
        #jus check th id
        if match["id"].replace("oomp_","") in kwargs["id"]:
            manufacturer_match = {}
            manufacturer_match["name"] = "Yageo"
            manufacturer_match["part_number"] = match["part_number"]
            manufacturer_match["link"] = f"https://www.yageo.com/en/Chart/Download/pdf/{match['part_number']}"
            manufacturer_match["id"] = "manufacturer_yageo"            
            manufacturers.append(manufacturer_match)
    
    #if there are no kwargs[distributers]
    if "manufacturers" not in kwargs:
        kwargs["manufacturers"] = []
        
    #add the manufacturers to kwargs[manufacturers]
    kwargs["manufacturers"].extend(manufacturers)

    return kwargs
