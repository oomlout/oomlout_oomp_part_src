import oomp

def get_manufacturers(**kwargs):
    kwargs = get_kyocera(**kwargs)   
    kwargs = get_lcsc(**kwargs)
    kwargs = get_microchip(**kwargs)
    kwargs = get_murata(**kwargs)
    kwargs = get_samsung(**kwargs)
    kwargs = get_uniroyal(**kwargs)
    kwargs = get_yageo(**kwargs)


    return kwargs

def get_kyocera(**kwargs):
    matches = []
    matches.append({"id":"oomp_electronic_capacitor_3216_avx_a_tantalum_4_7_micro_farad_16_volt",
                  "part_number": "TAJA475K016RNJ"})
    

    manufacturers = []
    for match in matches:
        #jus check th id
        if match["id"] in kwargs["id"]:
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
    matches.append({"id":"oomp_electronic_led_0603_red",
                    "name":"XINGLIGHT",
                    "part_number": "XL-1608SURC-06",
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



    manufacturers = []
    for match in matches:
        #jus check th id
        if match["id"] in kwargs["id"]:
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
        if match["id"] in kwargs["id"]:
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
        if match["id"] in kwargs["id"]:
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
        if match["id"] in kwargs["id"]:
            manufacturer_match = {}
            manufacturer_match["name"] = "Samsung"
            manufacturer_match["part_number"] = match["part_number"]
            manufacturer_match["link"] = f"https://product.samsungsem.com/mlcc/{match['part_number']}"
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
    matches.append({"id":"oomp_electronic_resistor_0603_1000_ohm",
                  "part_number": "0603WAF1001T5E"})
    

    manufacturers = []
    for match in matches:
        #jus check th id
        if match["id"] in kwargs["id"]:
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
    matches.append({"id":"oomp_electronic_resistor_0603_1000_ohm",
                    "part_number": "RC0603FR-071KL"})
    
    manufacturers = []
    for match in matches:
        #jus check th id
        if match["id"] in kwargs["id"]:
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
