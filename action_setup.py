import oomp
import oom_git

def main():
    #oomp.clone_data_files(a)
    #filter = "electronic_ic_lga_12_pin_2_mm_x_2_mm_sensor_accelerometer_sensortek_stk8321"
    #filter = "electronic_capacitor_0603_100_nano_farad"
    #filter = "electronic_led_0603_yellow"
    #filter = "resistor"


    repos = []
    repos.append(["https://github.com/oomlout/oomlout_oomp_footprint_bot","tmp/"])
    repos.append(["https://github.com/oomlout/oomlout_oomp_project_bot","tmp/"])
    repos.append(["https://github.com/oomlout/oomlout_oomp_symbol_bot","tmp/"])

    repos.append(["https://github.com/oomlout/oomlout_oomp_symbol_all_the_kicad_symbols","c:/gh/"])
    repos.append(["https://github.com/oomlout/oomlout_oomp_footprint_all_the_kicad_footprints","c:/gh/"])


    for repo in repos:
        directory = repo[1]
        #oom_git.clone(repo=repo[0], directory=directory)


    #filter is the type to import
    filter = ""
    #filter = "ic"
    oomp.load_parts(from_yaml=False, make_files=True, filter=filter)
    oomp.save_parts()



    #oom_git.push_to_git(comment=comment)

if __name__ == "__main__":
    main()