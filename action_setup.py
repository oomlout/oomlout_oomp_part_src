import oomp
import oom_git

def main():
    #oomp.clone_data_files()
    #filter = "electronic_ic_lga_12_pin_2_mm_x_2_mm_sensor_accelerometer_sensortek_stk8321"
    #filter = "electronic_capacitor_0603_100_nano_farad"
    #filter = "electronic_led_0603_yellow"
    #filter = "resistor"
    filter = ""
    oomp.load_parts(from_yaml=False, make_files=True, filter=filter)
    oomp.save_parts()

    #oom_git.push_to_git(comment=comment)

if __name__ == "__main__":
    main()