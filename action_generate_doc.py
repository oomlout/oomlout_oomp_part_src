import os
import oom_yaml


file_list = []
file_list.append(f"working.yaml")
file_list.append(f"readme.md")
file_list.append(f"working_600.jpg")
file_list.append(f"working_pinout_600.png")
for i in range(0, 5):
    file_list.append(f"symbol/{i}/working/working_600.png")
    file_list.append(f"footprint/{i}/working/working_600.png")



dir_doc_base = "C:/GH/oomlout_oomp_part_doc_v_2/parts"

def main(**kwargs):
    global file_list
    #iterate through all the directories in projects
    directory = "parts"    
    directories = [os.path.join(directory, d) for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]
    for dir in directories:
        dir_src = f"{dir}/working"
        print(f"Generating docs for {dir_src}")
        yaml_dict = oom_yaml.load_yaml_directory(directory=f"{dir_src}")        
        pass
        classification = yaml_dict.get('classification', "")
        typ = yaml_dict.get('type', "")
        size = yaml_dict.get('size', "")
        color = yaml_dict.get('color', "")
        description_main = yaml_dict.get('description_main', "")
        description_extra = yaml_dict.get('description_extra', "")
        manufacturer = yaml_dict.get('manufacturer', "")
        part_number = yaml_dict.get('part_number', "")
        # traditional way
        #order = [classification, typ, size, color, description_main, description_extra, manufacturer, part_number]
        #if typ == "ic" or typ == "capacitor":
        #    order = [classification, typ, color, description_main, description_extra, size, manufacturer, part_number]
        # try at better oflder structure
        order = [classification, typ, description_main,size, description_extra,   color, manufacturer, part_number]
        dir_level = ""
        for level in range(len(order)):
            #last_level test, see if the remaining levels are all empty
            level_value = order[level]
            last_level = True
            for level2 in range(level+1, len(order)):
                if order[level2] != "":
                    last_level = False
                    break
            if level_value == "":
                level_value = "blank"
            dir_level += f"/{level_value}"
            if last_level:
                break

        dir_dst = f"{dir_doc_base}/{dir_level}/a"

        for filename in file_list:
            #copy files across
            src = f"{dir_src}/{filename}"
            dst = f"{dir_dst}/{filename}"
            print(f"Copying {src} to {dst}")
            import shutil
            #if dst directory doesn't exist create it
            
            #if src exists
            if os.path.exists(src):   
                if not os.path.exists(os.path.dirname(dst)):
                    os.makedirs(os.path.dirname(dst))             
                shutil.copyfile(src, dst)
            else:
                pass
                #print(f"Warning: {src} doesn't exist")
        pass
    import oom_git
    oom_git.push(repo_directory = "c:/gh/oomlout_oomp_part_doc_v_2")






if __name__ == '__main__':
    main()