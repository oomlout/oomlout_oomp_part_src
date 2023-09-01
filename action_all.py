import oomp
import oom_git

def main():    
    import action_setup
    print("Setting up")
    action_setup.main()

    import action_generate_image_resolutions
    print("Generating image resolutions")
    action_generate_image_resolutions.main()
    import action_generate_readme
    print("Generating readme")
    action_generate_readme.main()
    import action_generate_readme_index
    print("Generating readme index")
    action_generate_readme_index.main()    
    

    comment = "added auto index generation"
    oom_git.push_to_git(comment=comment)

if __name__ == "__main__":
    main()