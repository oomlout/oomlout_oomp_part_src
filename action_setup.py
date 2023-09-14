import oomp
import oom_git

def main():
    #oomp.clone_data_files()
    #filter = "electronic_resistor_0603_1000_ohm"
    filter = ""
    oomp.load_parts(from_yaml=False, make_files=True, filter=filter)
    oomp.save_parts()

    #oom_git.push_to_git(comment=comment)

if __name__ == "__main__":
    main()