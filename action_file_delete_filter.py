import os
import glob

def main(**kwargs):
    pass
    filter_part = kwargs.get("filter_part", "")
    if filter_part == "":
        i = input("WARNING no filter part, press enter if this is okay")        
    filter_file = kwargs.get("filter_file", "")
    if filter_file == "":
        i = input("WARNING no filter file, press enter if this is okay")
    directory = "parts"
    files_all = glob.glob(f"{directory}/*/*/*")
    files_to_delete = []
    parts_affected = []
    for file in files_all:
        file = file
        directory = os.path.dirname(file)
        file_name = os.path.basename(file)
        if filter_part in directory:            
            if filter_file in file_name:
                #print(f"deleting {file}")
                files_to_delete.append(file)
                if directory not in parts_affected:
                    parts_affected.append(directory)
            else:
                pass
                #print(f"keeping {file}")
        else:
            pass
            #print(f"keeping {file}")

    #print number of files being deleted and first 5
    print(f"deleting {len(files_to_delete)} files")
    print(f"parts affected {len(parts_affected)}")
    print(f"first 5 files to delete")
    for file in files_to_delete[:5]:
        print(file)
    #confirm deletion
    i = input("confirm deletion y/n")
    if i == "y":
        for file in files_to_delete:
            print(f"deleting {file}")
            os.remove(file)
    else:
        print("not deleting")





if __name__ == "__main__":
    filter_part = ""
    filter_file = "working_label"
    kwargs = {}
    kwargs["filter_file"] = filter_file
    main(**kwargs)