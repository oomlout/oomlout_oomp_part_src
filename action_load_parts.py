import oomp
import oom_git

def main():
    #oomp.clone_data_files()
    #filter = "mounting_hole"
    #filter = ""
    oomp.load_parts(from_yaml=True, make_files=False, filter=filter)
    oomp.save_parts()

    #oom_git.push_to_git(comment=comment)

if __name__ == "__main__":
    main()