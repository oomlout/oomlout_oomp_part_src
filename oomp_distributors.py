import oomp

def get_distributors(**kwargs):
    kwargs = get_lcsc(**kwargs)
    kwargs = get_aliexpress(**kwargs)

    return kwargs

matches = []

def get_matches(**kwargs):
    global matches
    ###### matrix driver and assorte d ics
    matches.append({"id":"electronic_ic_sop_28_led_matrix_driver_16_x_8_wuxi_i_core_electronics_co_ltd_aip1640",
                  "part_number": "c82650"})

    # button
    matches.append({"id":"electronic_button_3_5_mm_x_6_mm_x_2_5_mm_surface_mount",
                  "part_number": "C2845294"})

    # capacitor
    part = "electronic_capacitor_0603_100_nano_farad"
    matches.append({"id":part, "part_number": "C14663"})
    matches.append({"id":part, "part_number": "C30926"})

    matches.append({"id":"electronic_capacitor_3216_avx_a_tantalum_4_7_micro_farad_16_volt",
                    "part_number": "C7187"})
    
    # ceramic resonator
    matches.append({"id":"electronic_ceramic_resonator_3213_3_pin_ground_pin_2_12_mega_hertz",
                    "part_number": "C341520"})
    matches.append({"id":"electronic_ceramic_resonator_3213_3_pin_ground_pin_2_16_mega_hertz",
                    "part_number": "C882605"})
    
    # diode
    matches.append({"id":"electronic_diode_schottky_sod_123_package_marking_b2_mbr0520",
                    "part_number": "C77335"})
    matches.append({"id":"electronic_diode_schottky_sod_123_package_marking_b2_mbr0520",
                    "part_number": "C475717"})
    matches.append({"id":"electronic_diode_sod_123_package_marking_t4_1n4148w",
                    "part_number": "C2099"})
    matches.append({"id":"electronic_diode_sod_123_package_marking_t4_1n4148w",
                    "part_number": "C444720"})
    

    # header
    matches.append({"id":"electronic_header_1d27_mm_6_pin",
                    "part_number": "C2935946"})

    #       jst
    #            sh
    matches.append({"id":"lectronic_header_1_mm_jst_sh_4_pin_surface_mount_right_angle",
                    "part_number": "C145956"})
    #matches.append({"id":"lectronic_header_1_mm_jst_sh_4_pin_surface_mount_right_angle",
    #                "part_number": "C160404"})
    matches.append({"id":"lectronic_header_1_mm_jst_sh_4_pin_surface_mount_right_angle",
                    "part_number": "C2906270"})



    # ic
    #      atmega328
    matches.append({"id":"electronic_ic_tqfp_32_mcu_atmega328_microchip_atmega328p_au",
                  "part_number": "C14877"})
    matches.append({"id":"electronic_ic_tqfp_32_mcu_atmega328_microchip_atmega328p_au",
                  "part_number": "C618816"})
    matches.append({"id":"electronic_ic_0603_sensor_light_everlight_elec_als_pt19",
                  "part_number": "C146233"})
    
    #      sensors
    matches.append({"id":"electronic_ic_lga_2_5_mm_x_2_5_mm_8_pin_sensor_pressure_temperature_bosch_bme280","part_number": "C92489"})
    matches.append({"id":"electronic_ic_lga_2_mm_x_2_mm_12_pin_sensor_accelerometer_sensortek_stk8321","part_number": "C966924"})

    #      rs2227 multiplexer
    matches.append({"id":"converter_usb_to_serial_converter_wch_ch340c",
                  "part_number": "C255478"})
    

    #      ch340
    matches.append({"id":"converter_usb_to_serial_converter_wch_ch340c",
                  "part_number": "C7464026"})
    matches.append({"id":"converter_usb_to_serial_converter_wch_ch340g",
                  "part_number": "C14267"})
    matches.append({"id":"converter_usb_to_serial_converter_wch_ch340e",
                  "part_number": "C99652"})
    matches.append({"id":"converter_usb_to_serial_converter_wch_ch340x",
                  "part_number": "C3035748"})
    matches.append({"id":"converter_usb_to_serial_converter_wch_ch340t",
                  "part_number": "C8689"})
    matches.append({"id":"converter_usb_to_serial_converter_wch_ch340n",
                  "part_number": "C2977777"})
    matches.append({"id":"converter_usb_to_serial_converter_wch_ch340k",
                  "part_number": "C968586"})
    matches.append({"id":"converter_usb_to_serial_converter_wch_ch340b",
                  "part_number": "C81010"})
    
    # led
    matches.append({"id":"electronic_led_0603_red",
                  "part_number": "C965799"})
    matches.append({"id":"electronic_led_0603_green",
                  "part_number": "C965804"})
    matches.append({"id":"electronic_led_0603_blue",
                  "part_number": "C965807"})
    matches.append({"id":"electronic_led_0603_yellow",
                  "part_number": "C965802"})
    matches.append({"id":"electronic_led_0603_white",
                  "part_number": "C965808"})
    matches.append({"id":"electronic_led_5050_rgb_ws2812b_worldsemi_ws2812b_b_w",
                  "part_number": "C114586"})
    
    matches.append({"id":"electronic_led_0603_white",
                  "part_number": "C965808"})

    # pmic
    #      1117
    matches.append({"id":"electronic_pmic_sot_223_linear_1117_5_volt",
                    "part_number": "C347223"})

    # resistors
    matches.append({"id":"resistor_0603_1000_ohm",
                  "part_number": "C21190"})
    matches.append({"id":"resistor_0603_1000_ohm",
                  "part_number": "C22548"})
    matches.append({"id":"resistor_0603_10000_ohm",
                  "part_number": "C98220"})
    matches.append({"id":"resistor_0603_10000_ohm",
                  "part_number": "C25804"})
    
    # sockets
    #      usb
    #            type_a
    matches.append({"id":"electronic_socket_usb_mini_surface_mount_only",
                  "part_number": "C2345"})
    #            mini
    matches.append({"id":"electronic_socket_usb_mini_surface_mount_only",
                  "part_number": "C91144"})
    

    lcsc_file = "src/distributor_matches_lcsc.yml"
    import yaml
    with open(lcsc_file, 'r') as file:
        lcsc_matches = yaml.load(file, Loader=yaml.FullLoader)
        matches.extend(lcsc_matches)

    #########



    #remove duplicates from matches where the id and part number are the same
    old_matches = matches.copy()
    new_matches = []    
    for match in old_matches:
        if match not in new_matches:
            new_matches.append(match)
    matches = new_matches


def get_lcsc(**kwargs):
    global matches

    if matches == []:
        get_matches(**kwargs)

    distributors = []
    for match in matches:
        #jus check th id
        if match["id"].replace("","") in kwargs["id"]:
            distributor_match = {}
            distributor_match["name"] = "LCSC"
            distributor_match["part_number"] = match["part_number"]
            distributor_match["link"] = f"https://lcsc.com/product-detail/{match['part_number']}.html"
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
        if match["id"].replace("","") in kwargs["id"]:
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