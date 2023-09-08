import oomp
import oom_git

def main():  

    fast = True
    fast = False

    
    import action_setup
    print("Setting up")
    action_setup.main()
    

    import action_copy_footprints_and_symbols
    print("Copying footprints and symbols")
    action_copy_footprints_and_symbols.main()

    if not fast:
        import action_copy_src_to_directories
        print("Copying src to directories")
        action_copy_src_to_directories.main()


    if not fast:
        import action_generate_pinouts
        print("Generating pinouts")
        action_generate_pinouts.main()
    
    if not fast:
        import action_generate_labels
        print("Generating labelss")
        action_generate_labels.main()
    

    if not fast:
        import action_generate_image_resolutions
        print("Generating image resolutions")
        action_generate_image_resolutions.main()

    import action_generate_csv
    print("Generating csv")
    action_generate_csv.main()
    
    import action_generate_readme
    print("Generating readme")
    action_generate_readme.main()
    import action_generate_readme_index
    print("Generating readme index")
    action_generate_readme_index.main()    
    
    if True:
    #if not fast:
        import action_generate_outputs
        print("Generating outputs")
        action_generate_outputs.main()


    comment = "added auto index generation"
    #oom_git.push_to_git(comment=comment)

if __name__ == "__main__":
    main()