import oomp


import oom_kicad    

def main():
    #oomp.clone_data_files()
    filter = "resistor"
    filter = ""
    oomp.load_parts(from_yaml=False, make_files=True, filter=filter)
    oomp.save_parts()

    oom_kicad.push_to_git()


if __name__ == "__main__":
    main()