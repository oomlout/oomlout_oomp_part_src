import oomp




def main():
    oomp.clone_data_files()
    filter = "resistor"
    filter = ""
    oomp.load_parts(from_yaml=False, make_files=True, filter=filter)
    oomp.save_parts()




if __name__ == "__main__":
    main()