import oomp

def get_distributors(**kwargs):
    kwargs = get_lcsc(**kwargs)
    kwargs = get_aliexpress(**kwargs)

    return kwargs

def get_lcsc(**kwargs):

    matches = []
    ###### matrix driver and assorte d ics
    matches.append({"id":"electronic_ic_sop_28_led_matrix_driver_16_x_8_wuxi_i_core_electronics_co_ltd_aip1640",
                  "part_number": "c82650"})

    # button
    matches.append({"id":"oomp_electronic_button_3_5_mm_x_6_mm_x_2_5_mm_surface_mount",
                  "part_number": "C2845294"})

    # capacitor
    part = "oomp_electronic_capacitor_0603_100_nano_farad"
    matches.append({"id":part, "part_number": "C14663"})
    matches.append({"id":part, "part_number": "C30926"})

    matches.append({"id":"oomp_electronic_capacitor_3216_avx_a_tantalum_4_7_micro_farad_16_volt",
                    "part_number": "C7187"})
    
    # ceramic resonator
    matches.append({"id":"oomp_electronic_ceramic_resonator_3213_3_pin_ground_pin_2_12_mega_hertz",
                    "part_number": "C341520"})
    matches.append({"id":"oomp_electronic_ceramic_resonator_3213_3_pin_ground_pin_2_16_mega_hertz",
                    "part_number": "C882605"})
    
    # diode
    matches.append({"id":"oomp_electronic_diode_schottky_sod_123_package_marking_b2_mbr0520",
                    "part_number": "C77335"})
    matches.append({"id":"oomp_electronic_diode_schottky_sod_123_package_marking_b2_mbr0520",
                    "part_number": "C475717"})

    # header
    matches.append({"id":"oomp_electronic_header_1d27_mm_6_pin",
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
    matches.append({"id":"oomp_electronic_ic_tqfp_32_mcu_atmega328_microchip_atmega328p_au",
                  "part_number": "C14877"})
    matches.append({"id":"oomp_electronic_ic_tqfp_32_mcu_atmega328_microchip_atmega328p_au",
                  "part_number": "C618816"})
    
    #      sensors
    matches.append({"id":"oomp_electronic_ic_lga_2_5_mm_x_2_5_mm_8_pin_sensor_pressure_temperature_bosch_bme280","part_number": "C92489"})

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
    matches.append({"id":"oomp_electronic_led_0603_red",
                  "part_number": "C965799"})
    matches.append({"id":"oomp_electronic_led_0603_green",
                  "part_number": "C965804"})
    matches.append({"id":"oomp_electronic_led_0603_blue",
                  "part_number": "C965807"})
    matches.append({"id":"oomp_electronic_led_0603_yellow",
                  "part_number": "C965802"})
    matches.append({"id":"oomp_electronic_led_0603_white",
                  "part_number": "C965808"})
    
    # pmic
    #      1117
    matches.append({"id":"oomp_electronic_pmic_sot_223_linear_1117_5_volt",
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
    #            mini
    matches.append({"id":"electronic_socket_usb_mini_surface_mount_only",
                  "part_number": "C91144"})
    
    ###### auto gen

    matches.append({"id":"electronic_capacitor_0603_22_pico_farad",
                  "part_number": "C2845294"})

    matches.append({"id":"electronic_capacitor_0603_22_pico_farad",
                  "part_number": "C105620"})

    matches.append({"id":"electronic_capacitor_0603_100_nano_farad",
                  "part_number": "C1591"})

    matches.append({"id":"electronic_capacitor_0603_100_nano_farad",
                  "part_number": "C14663"})

    matches.append({"id":"electronic_capacitor_0603_10_nano_farad",
                  "part_number": "C100042"})

    matches.append({"id":"electronic_capacitor_3216_avx_a_tantalum_4_7_micro_farad_16_volt",
                  "part_number": "C7187"})

    matches.append({"id":"electronic_ceramic_resonator_3213_3_pin_ground_pin_2_12_mega_hertz",
                  "part_number": "C341520"})

    matches.append({"id":"electronic_ceramic_resonator_3213_3_pin_ground_pin_2_16_mega_hertz",
                  "part_number": "C882605"})

    matches.append({"id":"electronic_diode_schottky_sod_123_package_marking_b2_mbr0520",
                  "part_number": "C77335"})

    matches.append({"id":"electronic_diode_schottky_sod_123_package_marking_b2_mbr0520",
                  "part_number": "C77335"})

    matches.append({"id":"electronic_diode_schottky_sod_123_package_marking_b2_mbr0520",
                  "part_number": "C165467"})

    matches.append({"id":"electronic_ic_tqfp_32_mcu_atmega328_microchip_atmega328p_au",
                  "part_number": "C14877"})

    matches.append({"id":"electronic_ic_tqfp_32_mcu_atmega328_microchip_atmega328p_au",
                  "part_number": "C618816"})

    matches.append({"id":"electronic_ic_lga_2_5_mm_x_2_5_mm_8_pin_sensor_pressure_temperature_bosch_bme280",
                  "part_number": "C92489"})

    matches.append({"id":"electronic_led_0603_red",
                  "part_number": "C965799"})

    matches.append({"id":"electronic_led_0603_green",
                  "part_number": "C965804"})

    matches.append({"id":"electronic_led_0603_blue",
                  "part_number": "C965807"})

    matches.append({"id":"electronic_led_0603_yellow",
                  "part_number": "C965802"})

    matches.append({"id":"electronic_pmic_sot_223_linear_1117_5_volt",
                  "part_number": "C6187"})

    matches.append({"id":"electronic_resistor_0201_10_ohm",
                  "part_number": "C2765872"})

    matches.append({"id":"electronic_resistor_0201_68_ohm",
                  "part_number": "C2779736"})

    matches.append({"id":"electronic_resistor_0201_100_ohm",
                  "part_number": "C965346"})

    matches.append({"id":"electronic_resistor_0201_270_ohm",
                  "part_number": "C2779729"})

    matches.append({"id":"electronic_resistor_0201_330_ohm",
                  "part_number": "C2779731"})

    matches.append({"id":"electronic_resistor_0201_390_ohm",
                  "part_number": "C2779732"})

    matches.append({"id":"electronic_resistor_0201_470_ohm",
                  "part_number": "C965312"})

    matches.append({"id":"electronic_resistor_0201_820_ohm",
                  "part_number": "C2779738"})

    matches.append({"id":"electronic_resistor_0201_1800_ohm",
                  "part_number": "C2779726"})

    matches.append({"id":"electronic_resistor_0201_3300_ohm",
                  "part_number": "C965317"})

    matches.append({"id":"electronic_resistor_0201_12000_ohm",
                  "part_number": "C2779724"})

    matches.append({"id":"electronic_resistor_0402_10_ohm",
                  "part_number": "C25139"})

    matches.append({"id":"electronic_resistor_0402_10_ohm",
                  "part_number": "C137925"})

    matches.append({"id":"electronic_resistor_0402_12_ohm",
                  "part_number": "C25141"})

    matches.append({"id":"electronic_resistor_0402_12_ohm",
                  "part_number": "C137921"})

    matches.append({"id":"electronic_resistor_0402_15_ohm",
                  "part_number": "C25144"})

    matches.append({"id":"electronic_resistor_0402_15_ohm",
                  "part_number": "C137916"})

    matches.append({"id":"electronic_resistor_0402_18_ohm",
                  "part_number": "C25146"})

    matches.append({"id":"electronic_resistor_0402_18_ohm",
                  "part_number": "C137911"})

    matches.append({"id":"electronic_resistor_0402_22_ohm",
                  "part_number": "C25152"})

    matches.append({"id":"electronic_resistor_0402_22_ohm",
                  "part_number": "C93929"})

    matches.append({"id":"electronic_resistor_0402_27_ohm",
                  "part_number": "C25156"})

    matches.append({"id":"electronic_resistor_0402_27_ohm",
                  "part_number": "C137890"})

    matches.append({"id":"electronic_resistor_0402_33_ohm",
                  "part_number": "C25161"})

    matches.append({"id":"electronic_resistor_0402_33_ohm",
                  "part_number": "C137880"})

    matches.append({"id":"electronic_resistor_0402_39_ohm",
                  "part_number": "C25164"})

    matches.append({"id":"electronic_resistor_0402_39_ohm",
                  "part_number": "C137875"})

    matches.append({"id":"electronic_resistor_0402_47_ohm",
                  "part_number": "C25168"})

    matches.append({"id":"electronic_resistor_0402_47_ohm",
                  "part_number": "C137864"})

    matches.append({"id":"electronic_resistor_0402_56_ohm",
                  "part_number": "C25173"})

    matches.append({"id":"electronic_resistor_0402_56_ohm",
                  "part_number": "C137857"})

    matches.append({"id":"electronic_resistor_0402_68_ohm",
                  "part_number": "C25178"})

    matches.append({"id":"electronic_resistor_0402_68_ohm",
                  "part_number": "C137848"})

    matches.append({"id":"electronic_resistor_0402_82_ohm",
                  "part_number": "C25181"})

    matches.append({"id":"electronic_resistor_0402_82_ohm",
                  "part_number": "C137835"})

    matches.append({"id":"electronic_resistor_0402_100_ohm",
                  "part_number": "C25138"})

    matches.append({"id":"electronic_resistor_0402_100_ohm",
                  "part_number": "C106233"})

    matches.append({"id":"electronic_resistor_0402_120_ohm",
                  "part_number": "C25140"})

    matches.append({"id":"electronic_resistor_0402_120_ohm",
                  "part_number": "C185384"})

    matches.append({"id":"electronic_resistor_0402_150_ohm",
                  "part_number": "C25143"})

    matches.append({"id":"electronic_resistor_0402_150_ohm",
                  "part_number": "C137918"})

    matches.append({"id":"electronic_resistor_0402_180_ohm",
                  "part_number": "C25145"})

    matches.append({"id":"electronic_resistor_0402_180_ohm",
                  "part_number": "C137913"})

    matches.append({"id":"electronic_resistor_0402_220_ohm",
                  "part_number": "C25151"})

    matches.append({"id":"electronic_resistor_0402_220_ohm",
                  "part_number": "C137899"})

    matches.append({"id":"electronic_resistor_0402_270_ohm",
                  "part_number": "C25155"})

    matches.append({"id":"electronic_resistor_0402_270_ohm",
                  "part_number": "C137892"})

    matches.append({"id":"electronic_resistor_0402_330_ohm",
                  "part_number": "C12246"})

    matches.append({"id":"electronic_resistor_0402_330_ohm",
                  "part_number": "C105876"})

    matches.append({"id":"electronic_resistor_0402_390_ohm",
                  "part_number": "C25163"})

    matches.append({"id":"electronic_resistor_0402_390_ohm",
                  "part_number": "C163442"})

    matches.append({"id":"electronic_resistor_0402_470_ohm",
                  "part_number": "C25167"})

    matches.append({"id":"electronic_resistor_0402_470_ohm",
                  "part_number": "C114949"})

    matches.append({"id":"electronic_resistor_0402_560_ohm",
                  "part_number": "C25172"})

    matches.append({"id":"electronic_resistor_0402_560_ohm",
                  "part_number": "C137858"})

    matches.append({"id":"electronic_resistor_0402_680_ohm",
                  "part_number": "C25177"})

    matches.append({"id":"electronic_resistor_0402_680_ohm",
                  "part_number": "C137849"})

    matches.append({"id":"electronic_resistor_0402_820_ohm",
                  "part_number": "C270398"})

    matches.append({"id":"electronic_resistor_0402_820_ohm",
                  "part_number": "C137837"})

    matches.append({"id":"electronic_resistor_0402_1000_ohm",
                  "part_number": "C25543"})

    matches.append({"id":"electronic_resistor_0402_1000_ohm",
                  "part_number": "C105637"})

    matches.append({"id":"electronic_resistor_0402_1200_ohm",
                  "part_number": "C25928"})

    matches.append({"id":"electronic_resistor_0402_1200_ohm",
                  "part_number": "C105637"})

    matches.append({"id":"electronic_resistor_0402_1500_ohm",
                  "part_number": "C25930"})

    matches.append({"id":"electronic_resistor_0402_1500_ohm",
                  "part_number": "C137887"})

    matches.append({"id":"electronic_resistor_0402_1800_ohm",
                  "part_number": "C25932"})

    matches.append({"id":"electronic_resistor_0402_1800_ohm",
                  "part_number": "C137887"})

    matches.append({"id":"electronic_resistor_0402_2200_ohm",
                  "part_number": "C25933"})

    matches.append({"id":"electronic_resistor_0402_2200_ohm",
                  "part_number": "C137887"})

    matches.append({"id":"electronic_resistor_0402_2700_ohm",
                  "part_number": "C25935"})

    matches.append({"id":"electronic_resistor_0402_2700_ohm",
                  "part_number": "C137872"})

    matches.append({"id":"electronic_resistor_0402_3300_ohm",
                  "part_number": "C25936"})

    matches.append({"id":"electronic_resistor_0402_3300_ohm",
                  "part_number": "C137872"})

    matches.append({"id":"electronic_resistor_0402_3900_ohm",
                  "part_number": "C11925"})

    matches.append({"id":"electronic_resistor_0402_4700_ohm",
                  "part_number": "C25940"})

    matches.append({"id":"electronic_resistor_0402_5600_ohm",
                  "part_number": "C25942"})

    matches.append({"id":"electronic_resistor_0402_6800_ohm",
                  "part_number": "C25944"})

    matches.append({"id":"electronic_resistor_0402_8200_ohm",
                  "part_number": "C25946"})

    matches.append({"id":"electronic_resistor_0402_10000_ohm",
                  "part_number": "C25531"})

    matches.append({"id":"electronic_resistor_0402_10000_ohm",
                  "part_number": "C60489"})

    matches.append({"id":"electronic_resistor_0402_12000_ohm",
                  "part_number": "C25535"})

    matches.append({"id":"electronic_resistor_0402_12000_ohm",
                  "part_number": "C137923"})

    matches.append({"id":"electronic_resistor_0402_15000_ohm",
                  "part_number": "C25539"})

    matches.append({"id":"electronic_resistor_0402_15000_ohm",
                  "part_number": "C137917"})

    matches.append({"id":"electronic_resistor_0402_18000_ohm",
                  "part_number": "C25542"})

    matches.append({"id":"electronic_resistor_0402_18000_ohm",
                  "part_number": "C137912"})

    matches.append({"id":"electronic_resistor_0402_22000_ohm",
                  "part_number": "C25547"})

    matches.append({"id":"electronic_resistor_0402_22000_ohm",
                  "part_number": "C137898"})

    matches.append({"id":"electronic_resistor_0402_27000_ohm",
                  "part_number": "C25551"})

    matches.append({"id":"electronic_resistor_0402_27000_ohm",
                  "part_number": "C137891"})

    matches.append({"id":"electronic_resistor_0402_33000_ohm",
                  "part_number": "C25555"})

    matches.append({"id":"electronic_resistor_0402_33000_ohm",
                  "part_number": "C137881"})

    matches.append({"id":"electronic_resistor_0402_39000_ohm",
                  "part_number": "C25558"})

    matches.append({"id":"electronic_resistor_0402_39000_ohm",
                  "part_number": "C137876"})

    matches.append({"id":"electronic_resistor_0402_47000_ohm",
                  "part_number": "C25563"})

    matches.append({"id":"electronic_resistor_0402_47000_ohm",
                  "part_number": "C163440"})

    matches.append({"id":"electronic_resistor_0402_56000_ohm",
                  "part_number": "C25567"})

    matches.append({"id":"electronic_resistor_0402_56000_ohm",
                  "part_number": "C163438"})

    matches.append({"id":"electronic_resistor_0402_68000_ohm",
                  "part_number": "C25569"})

    matches.append({"id":"electronic_resistor_0402_68000_ohm",
                  "part_number": "C163436"})

    matches.append({"id":"electronic_resistor_0402_82000_ohm",
                  "part_number": "C25571"})

    matches.append({"id":"electronic_resistor_0402_82000_ohm",
                  "part_number": "C137836"})

    matches.append({"id":"electronic_resistor_0603_10_ohm",
                  "part_number": "C25202"})

    matches.append({"id":"electronic_resistor_0603_10_ohm",
                  "part_number": "C109317"})

    matches.append({"id":"electronic_resistor_0603_12_ohm",
                  "part_number": "C25206"})

    matches.append({"id":"electronic_resistor_0603_12_ohm",
                  "part_number": "C246021"})

    matches.append({"id":"electronic_resistor_0603_15_ohm",
                  "part_number": "C25209"})

    matches.append({"id":"electronic_resistor_0603_15_ohm",
                  "part_number": "C137659"})

    matches.append({"id":"electronic_resistor_0603_18_ohm",
                  "part_number": "C25211"})

    matches.append({"id":"electronic_resistor_0603_18_ohm",
                  "part_number": "C137654"})

    matches.append({"id":"electronic_resistor_0603_22_ohm",
                  "part_number": "C1203"})

    matches.append({"id":"electronic_resistor_0603_22_ohm",
                  "part_number": "C108405"})

    matches.append({"id":"electronic_resistor_0603_27_ohm",
                  "part_number": "C25224"})

    matches.append({"id":"electronic_resistor_0603_27_ohm",
                  "part_number": "C137639"})

    matches.append({"id":"electronic_resistor_0603_33_ohm",
                  "part_number": "C25232"})

    matches.append({"id":"electronic_resistor_0603_33_ohm",
                  "part_number": "C108407"})

    matches.append({"id":"electronic_resistor_0603_39_ohm",
                  "part_number": "C25236"})

    matches.append({"id":"electronic_resistor_0603_39_ohm",
                  "part_number": "C137630"})

    matches.append({"id":"electronic_resistor_0603_47_ohm",
                  "part_number": "C1211"})

    matches.append({"id":"electronic_resistor_0603_47_ohm",
                  "part_number": "C114684"})

    matches.append({"id":"electronic_resistor_0603_56_ohm",
                  "part_number": "C25248"})

    matches.append({"id":"electronic_resistor_0603_56_ohm",
                  "part_number": "C127448"})

    matches.append({"id":"electronic_resistor_0603_68_ohm",
                  "part_number": "C25254"})

    matches.append({"id":"electronic_resistor_0603_68_ohm",
                  "part_number": "C163413"})

    matches.append({"id":"electronic_resistor_0603_82_ohm",
                  "part_number": "C25260"})

    matches.append({"id":"electronic_resistor_0603_82_ohm",
                  "part_number": "C137606"})

    matches.append({"id":"electronic_resistor_0603_100_ohm",
                  "part_number": "C25201"})

    matches.append({"id":"electronic_resistor_0603_100_ohm",
                  "part_number": "C110091"})

    matches.append({"id":"electronic_resistor_0603_120_ohm",
                  "part_number": "C25205"})

    matches.append({"id":"electronic_resistor_0603_120_ohm",
                  "part_number": "C114681"})

    matches.append({"id":"electronic_resistor_0603_150_ohm",
                  "part_number": "C25208"})

    matches.append({"id":"electronic_resistor_0603_150_ohm",
                  "part_number": "C126805"})

    matches.append({"id":"electronic_resistor_0603_180_ohm",
                  "part_number": "C25210"})

    matches.append({"id":"electronic_resistor_0603_180_ohm",
                  "part_number": "C137656"})

    matches.append({"id":"electronic_resistor_0603_220_ohm",
                  "part_number": "C1226"})

    matches.append({"id":"electronic_resistor_0603_220_ohm",
                  "part_number": "C114683"})

    matches.append({"id":"electronic_resistor_0603_270_ohm",
                  "part_number": "C25223"})

    matches.append({"id":"electronic_resistor_0603_270_ohm",
                  "part_number": "C137641"})

    matches.append({"id":"electronic_resistor_0603_330_ohm",
                  "part_number": "C25231"})

    matches.append({"id":"electronic_resistor_0603_330_ohm",
                  "part_number": "C105879"})

    matches.append({"id":"electronic_resistor_0603_390_ohm",
                  "part_number": "C25235"})

    matches.append({"id":"electronic_resistor_0603_390_ohm",
                  "part_number": "C137632"})

    matches.append({"id":"electronic_resistor_0603_470_ohm",
                  "part_number": "C25241"})

    matches.append({"id":"electronic_resistor_0603_470_ohm",
                  "part_number": "C114433"})

    matches.append({"id":"electronic_resistor_0603_560_ohm",
                  "part_number": "C25247"})

    matches.append({"id":"electronic_resistor_0603_560_ohm",
                  "part_number": "C137619"})

    matches.append({"id":"electronic_resistor_0603_680_ohm",
                  "part_number": "C25253"})

    matches.append({"id":"electronic_resistor_0603_680_ohm",
                  "part_number": "C115415"})

    matches.append({"id":"electronic_resistor_0603_820_ohm",
                  "part_number": "C25259"})

    matches.append({"id":"electronic_resistor_0603_820_ohm",
                  "part_number": "C137608"})

    matches.append({"id":"electronic_resistor_0603_1000_ohm",
                  "part_number": "C25585"})

    matches.append({"id":"electronic_resistor_0603_1000_ohm",
                  "part_number": "C14676"})

    matches.append({"id":"electronic_resistor_0603_1200_ohm",
                  "part_number": "C25987"})

    matches.append({"id":"electronic_resistor_0603_1200_ohm",
                  "part_number": "C14676"})

    matches.append({"id":"electronic_resistor_0603_1500_ohm",
                  "part_number": "C25989"})

    matches.append({"id":"electronic_resistor_0603_1500_ohm",
                  "part_number": "C105581"})

    matches.append({"id":"electronic_resistor_0603_1800_ohm",
                  "part_number": "C25991"})

    matches.append({"id":"electronic_resistor_0603_1800_ohm",
                  "part_number": "C105581"})

    matches.append({"id":"electronic_resistor_0603_2200_ohm",
                  "part_number": "C25992"})

    matches.append({"id":"electronic_resistor_0603_2200_ohm",
                  "part_number": "C105581"})

    matches.append({"id":"electronic_resistor_0603_2700_ohm",
                  "part_number": "C25994"})

    matches.append({"id":"electronic_resistor_0603_2700_ohm",
                  "part_number": "C137628"})

    matches.append({"id":"electronic_resistor_0603_3300_ohm",
                  "part_number": "C25995"})

    matches.append({"id":"electronic_resistor_0603_3300_ohm",
                  "part_number": "C137628"})

    matches.append({"id":"electronic_resistor_0603_3900_ohm",
                  "part_number": "C25997"})

    matches.append({"id":"electronic_resistor_0603_4700_ohm",
                  "part_number": "C25999"})

    matches.append({"id":"electronic_resistor_0603_5600_ohm",
                  "part_number": "C26001"})

    matches.append({"id":"electronic_resistor_0603_6800_ohm",
                  "part_number": "C26004"})

    matches.append({"id":"electronic_resistor_0603_8200_ohm",
                  "part_number": "C26007"})

    matches.append({"id":"electronic_resistor_0603_10000_ohm",
                  "part_number": "C15401"})

    matches.append({"id":"electronic_resistor_0603_10000_ohm",
                  "part_number": "C99198"})

    matches.append({"id":"electronic_resistor_0603_12000_ohm",
                  "part_number": "C25577"})

    matches.append({"id":"electronic_resistor_0603_12000_ohm",
                  "part_number": "C137662"})

    matches.append({"id":"electronic_resistor_0603_15000_ohm",
                  "part_number": "C25581"})

    matches.append({"id":"electronic_resistor_0603_15000_ohm",
                  "part_number": "C114682"})

    matches.append({"id":"electronic_resistor_0603_18000_ohm",
                  "part_number": "C25985"})

    matches.append({"id":"electronic_resistor_0603_18000_ohm",
                  "part_number": "C137655"})

    matches.append({"id":"electronic_resistor_0603_22000_ohm",
                  "part_number": "C23344"})

    matches.append({"id":"electronic_resistor_0603_22000_ohm",
                  "part_number": "C115416"})

    matches.append({"id":"electronic_resistor_0603_27000_ohm",
                  "part_number": "C25589"})

    matches.append({"id":"electronic_resistor_0603_27000_ohm",
                  "part_number": "C137640"})

    matches.append({"id":"electronic_resistor_0603_33000_ohm",
                  "part_number": "C25593"})

    matches.append({"id":"electronic_resistor_0603_33000_ohm",
                  "part_number": "C138564"})

    matches.append({"id":"electronic_resistor_0603_39000_ohm",
                  "part_number": "C25596"})

    matches.append({"id":"electronic_resistor_0603_39000_ohm",
                  "part_number": "C137631"})

    matches.append({"id":"electronic_resistor_0603_47000_ohm",
                  "part_number": "C25600"})

    matches.append({"id":"electronic_resistor_0603_47000_ohm",
                  "part_number": "C127447"})

    matches.append({"id":"electronic_resistor_0603_56000_ohm",
                  "part_number": "C25603"})

    matches.append({"id":"electronic_resistor_0603_56000_ohm",
                  "part_number": "C137618"})

    matches.append({"id":"electronic_resistor_0603_68000_ohm",
                  "part_number": "C25607"})

    matches.append({"id":"electronic_resistor_0603_68000_ohm",
                  "part_number": "C113301"})

    matches.append({"id":"electronic_resistor_0603_82000_ohm",
                  "part_number": "C1275"})

    matches.append({"id":"electronic_resistor_0603_82000_ohm",
                  "part_number": "C137607"})

    matches.append({"id":"electronic_resistor_0805_10_ohm",
                  "part_number": "C25278"})

    matches.append({"id":"electronic_resistor_0805_10_ohm",
                  "part_number": "C137478"})

    matches.append({"id":"electronic_resistor_0805_12_ohm",
                  "part_number": "C25281"})

    matches.append({"id":"electronic_resistor_0805_12_ohm",
                  "part_number": "C185280"})

    matches.append({"id":"electronic_resistor_0805_15_ohm",
                  "part_number": "C25284"})

    matches.append({"id":"electronic_resistor_0805_15_ohm",
                  "part_number": "C137471"})

    matches.append({"id":"electronic_resistor_0805_18_ohm",
                  "part_number": "C25287"})

    matches.append({"id":"electronic_resistor_0805_18_ohm",
                  "part_number": "C137467"})

    matches.append({"id":"electronic_resistor_0805_22_ohm",
                  "part_number": "C25295"})

    matches.append({"id":"electronic_resistor_0805_22_ohm",
                  "part_number": "C108406"})

    matches.append({"id":"electronic_resistor_0805_27_ohm",
                  "part_number": "C25299"})

    matches.append({"id":"electronic_resistor_0805_27_ohm",
                  "part_number": "C137455"})

    matches.append({"id":"electronic_resistor_0805_33_ohm",
                  "part_number": "C25307"})

    matches.append({"id":"electronic_resistor_0805_33_ohm",
                  "part_number": "C127988"})

    matches.append({"id":"electronic_resistor_0805_39_ohm",
                  "part_number": "C25311"})

    matches.append({"id":"electronic_resistor_0805_39_ohm",
                  "part_number": "C137439"})

    matches.append({"id":"electronic_resistor_0805_47_ohm",
                  "part_number": "C25315"})

    matches.append({"id":"electronic_resistor_0805_47_ohm",
                  "part_number": "C114743"})

    matches.append({"id":"electronic_resistor_0805_56_ohm",
                  "part_number": "C25320"})

    matches.append({"id":"electronic_resistor_0805_56_ohm",
                  "part_number": "C113305"})

    matches.append({"id":"electronic_resistor_0805_68_ohm",
                  "part_number": "C25325"})

    matches.append({"id":"electronic_resistor_0805_68_ohm",
                  "part_number": "C137411"})

    matches.append({"id":"electronic_resistor_0805_82_ohm",
                  "part_number": "C25329"})

    matches.append({"id":"electronic_resistor_0805_82_ohm",
                  "part_number": "C137400"})

    matches.append({"id":"electronic_resistor_0805_100_ohm",
                  "part_number": "C25277"})

    matches.append({"id":"electronic_resistor_0805_100_ohm",
                  "part_number": "C106949"})

    matches.append({"id":"electronic_resistor_0805_120_ohm",
                  "part_number": "C25280"})

    matches.append({"id":"electronic_resistor_0805_120_ohm",
                  "part_number": "C114244"})

    matches.append({"id":"electronic_resistor_0805_150_ohm",
                  "part_number": "C25283"})

    matches.append({"id":"electronic_resistor_0805_150_ohm",
                  "part_number": "C96210"})

    matches.append({"id":"electronic_resistor_0805_180_ohm",
                  "part_number": "C1339"})

    matches.append({"id":"electronic_resistor_0805_180_ohm",
                  "part_number": "C163397"})

    matches.append({"id":"electronic_resistor_0805_220_ohm",
                  "part_number": "C25294"})

    matches.append({"id":"electronic_resistor_0805_220_ohm",
                  "part_number": "C114742"})

    matches.append({"id":"electronic_resistor_0805_270_ohm",
                  "part_number": "C25298"})

    matches.append({"id":"electronic_resistor_0805_270_ohm",
                  "part_number": "C93657"})

    matches.append({"id":"electronic_resistor_0805_330_ohm",
                  "part_number": "C25306"})

    matches.append({"id":"electronic_resistor_0805_330_ohm",
                  "part_number": "C105877"})

    matches.append({"id":"electronic_resistor_0805_390_ohm",
                  "part_number": "C25310"})

    matches.append({"id":"electronic_resistor_0805_390_ohm",
                  "part_number": "C137441"})

    matches.append({"id":"electronic_resistor_0805_470_ohm",
                  "part_number": "C21266"})

    matches.append({"id":"electronic_resistor_0805_470_ohm",
                  "part_number": "C114747"})

    matches.append({"id":"electronic_resistor_0805_560_ohm",
                  "part_number": "C25319"})

    matches.append({"id":"electronic_resistor_0805_560_ohm",
                  "part_number": "C137421"})

    matches.append({"id":"electronic_resistor_0805_680_ohm",
                  "part_number": "C25324"})

    matches.append({"id":"electronic_resistor_0805_680_ohm",
                  "part_number": "C93658"})

    matches.append({"id":"electronic_resistor_0805_820_ohm",
                  "part_number": "C25328"})

    matches.append({"id":"electronic_resistor_0805_820_ohm",
                  "part_number": "C137402"})

    matches.append({"id":"electronic_resistor_0805_1000_ohm",
                  "part_number": "C25623"})

    matches.append({"id":"electronic_resistor_0805_1000_ohm",
                  "part_number": "C100046"})

    matches.append({"id":"electronic_resistor_0805_1200_ohm",
                  "part_number": "C26013"})

    matches.append({"id":"electronic_resistor_0805_1200_ohm",
                  "part_number": "C100046"})

    matches.append({"id":"electronic_resistor_0805_1500_ohm",
                  "part_number": "C26015"})

    matches.append({"id":"electronic_resistor_0805_1500_ohm",
                  "part_number": "C114748"})

    matches.append({"id":"electronic_resistor_0805_1800_ohm",
                  "part_number": "C26016"})

    matches.append({"id":"electronic_resistor_0805_1800_ohm",
                  "part_number": "C114748"})

    matches.append({"id":"electronic_resistor_0805_2200_ohm",
                  "part_number": "C26017"})

    matches.append({"id":"electronic_resistor_0805_2200_ohm",
                  "part_number": "C114748"})

    matches.append({"id":"electronic_resistor_0805_2700_ohm",
                  "part_number": "C26019"})

    matches.append({"id":"electronic_resistor_0805_2700_ohm",
                  "part_number": "C137437"})

    matches.append({"id":"electronic_resistor_0805_3300_ohm",
                  "part_number": "C26020"})

    matches.append({"id":"electronic_resistor_0805_3300_ohm",
                  "part_number": "C137437"})

    matches.append({"id":"electronic_resistor_0805_3900_ohm",
                  "part_number": "C26021"})

    matches.append({"id":"electronic_resistor_0805_4700_ohm",
                  "part_number": "C26022"})

    matches.append({"id":"electronic_resistor_0805_5600_ohm",
                  "part_number": "C26024"})

    matches.append({"id":"electronic_resistor_0805_6800_ohm",
                  "part_number": "C26026"})

    matches.append({"id":"electronic_resistor_0805_8200_ohm",
                  "part_number": "C26028"})

    matches.append({"id":"electronic_resistor_0805_10000_ohm",
                  "part_number": "C25612"})

    matches.append({"id":"electronic_resistor_0805_10000_ohm",
                  "part_number": "C100047"})

    matches.append({"id":"electronic_resistor_0805_12000_ohm",
                  "part_number": "C25616"})

    matches.append({"id":"electronic_resistor_0805_12000_ohm",
                  "part_number": "C114241"})

    matches.append({"id":"electronic_resistor_0805_15000_ohm",
                  "part_number": "C25620"})

    matches.append({"id":"electronic_resistor_0805_15000_ohm",
                  "part_number": "C114740"})

    matches.append({"id":"electronic_resistor_0805_18000_ohm",
                  "part_number": "C25622"})

    matches.append({"id":"electronic_resistor_0805_18000_ohm",
                  "part_number": "C137468"})

    matches.append({"id":"electronic_resistor_0805_22000_ohm",
                  "part_number": "C25626"})

    matches.append({"id":"electronic_resistor_0805_22000_ohm",
                  "part_number": "C114231"})

    matches.append({"id":"electronic_resistor_0805_27000_ohm",
                  "part_number": "C25627"})

    matches.append({"id":"electronic_resistor_0805_27000_ohm",
                  "part_number": "C137456"})

    matches.append({"id":"electronic_resistor_0805_33000_ohm",
                  "part_number": "C25630"})

    matches.append({"id":"electronic_resistor_0805_33000_ohm",
                  "part_number": "C137446"})

    matches.append({"id":"electronic_resistor_0805_39000_ohm",
                  "part_number": "C25632"})

    matches.append({"id":"electronic_resistor_0805_39000_ohm",
                  "part_number": "C137440"})

    matches.append({"id":"electronic_resistor_0805_47000_ohm",
                  "part_number": "C29252"})

    matches.append({"id":"electronic_resistor_0805_47000_ohm",
                  "part_number": "C131051"})

    matches.append({"id":"electronic_resistor_0805_56000_ohm",
                  "part_number": "C25638"})

    matches.append({"id":"electronic_resistor_0805_56000_ohm",
                  "part_number": "C137420"})

    matches.append({"id":"electronic_resistor_0805_68000_ohm",
                  "part_number": "C25641"})

    matches.append({"id":"electronic_resistor_0805_68000_ohm",
                  "part_number": "C137412"})

    matches.append({"id":"electronic_resistor_0805_82000_ohm",
                  "part_number": "C25645"})

    matches.append({"id":"electronic_resistor_0805_82000_ohm",
                  "part_number": "C137401"})

    matches.append({"id":"electronic_resistor_1206_10_ohm",
                  "part_number": "C25349"})

    matches.append({"id":"electronic_resistor_1206_10_ohm",
                  "part_number": "C137208"})

    matches.append({"id":"electronic_resistor_1206_12_ohm",
                  "part_number": "C25352"})

    matches.append({"id":"electronic_resistor_1206_12_ohm",
                  "part_number": "C137202"})

    matches.append({"id":"electronic_resistor_1206_15_ohm",
                  "part_number": "C25354"})

    matches.append({"id":"electronic_resistor_1206_15_ohm",
                  "part_number": "C137198"})

    matches.append({"id":"electronic_resistor_1206_18_ohm",
                  "part_number": "C247146"})

    matches.append({"id":"electronic_resistor_1206_18_ohm",
                  "part_number": "C137192"})

    matches.append({"id":"electronic_resistor_1206_22_ohm",
                  "part_number": "C25364"})

    matches.append({"id":"electronic_resistor_1206_22_ohm",
                  "part_number": "C114950"})

    matches.append({"id":"electronic_resistor_1206_27_ohm",
                  "part_number": "C25367"})

    matches.append({"id":"electronic_resistor_1206_27_ohm",
                  "part_number": "C137168"})

    matches.append({"id":"electronic_resistor_1206_33_ohm",
                  "part_number": "C25375"})

    matches.append({"id":"electronic_resistor_1206_33_ohm",
                  "part_number": "C137151"})

    matches.append({"id":"electronic_resistor_1206_39_ohm",
                  "part_number": "C25379"})

    matches.append({"id":"electronic_resistor_1206_39_ohm",
                  "part_number": "C137146"})

    matches.append({"id":"electronic_resistor_1206_47_ohm",
                  "part_number": "C25384"})

    matches.append({"id":"electronic_resistor_1206_47_ohm",
                  "part_number": "C137138"})

    matches.append({"id":"electronic_resistor_1206_56_ohm",
                  "part_number": "C25389"})

    matches.append({"id":"electronic_resistor_1206_56_ohm",
                  "part_number": "C134080"})

    matches.append({"id":"electronic_resistor_1206_68_ohm",
                  "part_number": "C25393"})

    matches.append({"id":"electronic_resistor_1206_68_ohm",
                  "part_number": "C137122"})

    matches.append({"id":"electronic_resistor_1206_82_ohm",
                  "part_number": "C270896"})

    matches.append({"id":"electronic_resistor_1206_82_ohm",
                  "part_number": "C137110"})

    matches.append({"id":"electronic_resistor_1206_100_ohm",
                  "part_number": "C25348"})

    matches.append({"id":"electronic_resistor_1206_100_ohm",
                  "part_number": "C113307"})

    matches.append({"id":"electronic_resistor_1206_120_ohm",
                  "part_number": "C25351"})

    matches.append({"id":"electronic_resistor_1206_120_ohm",
                  "part_number": "C137204"})

    matches.append({"id":"electronic_resistor_1206_150_ohm",
                  "part_number": "C25353"})

    matches.append({"id":"electronic_resistor_1206_150_ohm",
                  "part_number": "C137200"})

    matches.append({"id":"electronic_resistor_1206_180_ohm",
                  "part_number": "C25356"})

    matches.append({"id":"electronic_resistor_1206_180_ohm",
                  "part_number": "C137193"})

    matches.append({"id":"electronic_resistor_1206_220_ohm",
                  "part_number": "C25363"})

    matches.append({"id":"electronic_resistor_1206_220_ohm",
                  "part_number": "C137176"})

    matches.append({"id":"electronic_resistor_1206_270_ohm",
                  "part_number": "C25366"})

    matches.append({"id":"electronic_resistor_1206_270_ohm",
                  "part_number": "C137170"})

    matches.append({"id":"electronic_resistor_1206_330_ohm",
                  "part_number": "C25374"})

    matches.append({"id":"electronic_resistor_1206_330_ohm",
                  "part_number": "C137152"})

    matches.append({"id":"electronic_resistor_1206_390_ohm",
                  "part_number": "C25378"})

    matches.append({"id":"electronic_resistor_1206_390_ohm",
                  "part_number": "C137148"})

    matches.append({"id":"electronic_resistor_1206_470_ohm",
                  "part_number": "C25383"})

    matches.append({"id":"electronic_resistor_1206_470_ohm",
                  "part_number": "C114948"})

    matches.append({"id":"electronic_resistor_1206_560_ohm",
                  "part_number": "C25388"})

    matches.append({"id":"electronic_resistor_1206_560_ohm",
                  "part_number": "C163358"})

    matches.append({"id":"electronic_resistor_1206_680_ohm",
                  "part_number": "C25392"})

    matches.append({"id":"electronic_resistor_1206_680_ohm",
                  "part_number": "C137124"})

    matches.append({"id":"electronic_resistor_1206_820_ohm",
                  "part_number": "C25396"})

    matches.append({"id":"electronic_resistor_1206_820_ohm",
                  "part_number": "C137112"})

    matches.append({"id":"electronic_resistor_1206_1000_ohm",
                  "part_number": "C1469"})

    matches.append({"id":"electronic_resistor_1206_1000_ohm",
                  "part_number": "C112223"})

    matches.append({"id":"electronic_resistor_1206_1200_ohm",
                  "part_number": "C26035"})

    matches.append({"id":"electronic_resistor_1206_1200_ohm",
                  "part_number": "C112223"})

    matches.append({"id":"electronic_resistor_1206_1500_ohm",
                  "part_number": "C26036"})

    matches.append({"id":"electronic_resistor_1206_1500_ohm",
                  "part_number": "C136404"})

    matches.append({"id":"electronic_resistor_1206_1800_ohm",
                  "part_number": "C26037"})

    matches.append({"id":"electronic_resistor_1206_1800_ohm",
                  "part_number": "C136404"})

    matches.append({"id":"electronic_resistor_1206_2200_ohm",
                  "part_number": "C26038"})

    matches.append({"id":"electronic_resistor_1206_2200_ohm",
                  "part_number": "C136404"})

    matches.append({"id":"electronic_resistor_1206_2700_ohm",
                  "part_number": "C26040"})

    matches.append({"id":"electronic_resistor_1206_2700_ohm",
                  "part_number": "C136407"})

    matches.append({"id":"electronic_resistor_1206_3300_ohm",
                  "part_number": "C26041"})

    matches.append({"id":"electronic_resistor_1206_3300_ohm",
                  "part_number": "C136407"})

    matches.append({"id":"electronic_resistor_1206_3900_ohm",
                  "part_number": "C26042"})

    matches.append({"id":"electronic_resistor_1206_4700_ohm",
                  "part_number": "C26043"})

    matches.append({"id":"electronic_resistor_1206_5600_ohm",
                  "part_number": "C26045"})

    matches.append({"id":"electronic_resistor_1206_6800_ohm",
                  "part_number": "C26046"})

    matches.append({"id":"electronic_resistor_1206_8200_ohm",
                  "part_number": "C26048"})

    matches.append({"id":"electronic_resistor_1206_10000_ohm",
                  "part_number": "C1489"})

    matches.append({"id":"electronic_resistor_1206_10000_ohm",
                  "part_number": "C136460"})

    matches.append({"id":"electronic_resistor_1206_12000_ohm",
                  "part_number": "C1491"})

    matches.append({"id":"electronic_resistor_1206_12000_ohm",
                  "part_number": "C137203"})

    matches.append({"id":"electronic_resistor_1206_15000_ohm",
                  "part_number": "C1493"})

    matches.append({"id":"electronic_resistor_1206_15000_ohm",
                  "part_number": "C137199"})

    matches.append({"id":"electronic_resistor_1206_18000_ohm",
                  "part_number": "C51545"})

    matches.append({"id":"electronic_resistor_1206_18000_ohm",
                  "part_number": "C246063"})

    matches.append({"id":"electronic_resistor_1206_22000_ohm",
                  "part_number": "C25654"})

    matches.append({"id":"electronic_resistor_1206_22000_ohm",
                  "part_number": "C136461"})

    matches.append({"id":"electronic_resistor_1206_27000_ohm",
                  "part_number": "C25656"})

    matches.append({"id":"electronic_resistor_1206_27000_ohm",
                  "part_number": "C137169"})

    matches.append({"id":"electronic_resistor_1206_33000_ohm",
                  "part_number": "C25660"})

    matches.append({"id":"electronic_resistor_1206_33000_ohm",
                  "part_number": "C136468"})

    matches.append({"id":"electronic_resistor_1206_39000_ohm",
                  "part_number": "C270897"})

    matches.append({"id":"electronic_resistor_1206_39000_ohm",
                  "part_number": "C137147"})

    matches.append({"id":"electronic_resistor_1206_47000_ohm",
                  "part_number": "C25664"})

    matches.append({"id":"electronic_resistor_1206_47000_ohm",
                  "part_number": "C136469"})

    matches.append({"id":"electronic_resistor_1206_56000_ohm",
                  "part_number": "C25667"})

    matches.append({"id":"electronic_resistor_1206_56000_ohm",
                  "part_number": "C137131"})

    matches.append({"id":"electronic_resistor_1206_68000_ohm",
                  "part_number": "C25668"})

    matches.append({"id":"electronic_resistor_1206_68000_ohm",
                  "part_number": "C137123"})

    matches.append({"id":"electronic_resistor_1206_82000_ohm",
                  "part_number": "C25670"})

    matches.append({"id":"electronic_resistor_1206_82000_ohm",
                  "part_number": "C137111"})

    matches.append({"id":"electronic_socket_usb_mini_surface_mount_only",
                  "part_number": "C91144"})

    #########

    #remove duplicates from matches
    matches = [dict(t) for t in {tuple(d.items()) for d in matches}]

    distributors = []
    for match in matches:
        #jus check th id
        if match["id"].replace("oomp_","") in kwargs["id"]:
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
        if match["id"].replace("oomp_","") in kwargs["id"]:
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