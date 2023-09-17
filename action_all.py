import oomp
import oom_git

def main():  

    
    fast = False
    #fast = True

    label=True
    label=False 

    doc = True
    #doc = False

    all= True
    all= False
    if all:
        fast = False
        #label = True #makes new pdfs which are messy in git
        doc = True

    
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
    
    if label:
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

    if doc:
        import action_generate_doc
        print("Generating doc")
        action_generate_doc.main()
        oom_git.push(repo_directory = "c:/gh/oomlout_oomp_part_doc_v_2")

    import action_generate_orders
    print("Generating orders")
    action_generate_orders.main()

    comment = "added auto index generation"
    oom_git.push_to_git(comment=comment)

if __name__ == "__main__":
    main()