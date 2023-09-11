import oom_base
import oom_yaml
import oom_markdown
import oom_office
import os

def main(**kwargs):
    
    count = 1   
    count2 = 1
    directory = "order"
    for root, dirs, files in os.walk(directory):
        #for each directory
            for file in files:   
                filename = os.path.join(root, file )
                directory = os.path.dirname(filename)
                #yaml_fuile is folder plus working .yaml
                yaml_file = os.path.join(directory, "working.yaml")
                convert_ods_to_csv(file=file, root=root, yaml_file=yaml_file)
                copy_labels(file=file, root=root, yaml_file=yaml_file)  
                make_readme(file=file, root=root, yaml_file=yaml_file)           
                            
                        
def convert_ods_to_csv(**kwargs):
    file = kwargs.get('file', "")
    root = kwargs.get('root', "")
    #create csv
    
    if file.endswith(".ods"):                    
        filename = os.path.join(root, file )
        print(f"converting {filename}")
        #make filename absolute
        filename = os.path.abspath(filename)
        oom_office.generate_outputs(filename=filename, overwrite=True)
    
def copy_labels(**kwargs):
    file = kwargs.get('file', "")
    root = kwargs.get('root', "")
    yaml_file = kwargs.get('yaml_file', "")
    parts_ordered_oomp = []
    if file == "working.ods":  
        
        #get the parts orderd
        file_csv = file.replace(".ods", ".csv")
        filename = os.path.join(root, file_csv )
        print(f"copying labels for {filename}")      
        #load csv
        parts_ordered_oomp = oom_office.load_csv_to_dict(filename=filename)
        #add to yaml
        import oom_yaml    
        detail = ["parts_ordered_oomp", parts_ordered_oomp]
        oom_yaml.add_detail(yaml_file=yaml_file, detail=detail, add_markdown=True, oomp_replace=True)
        
    #copy labels
    if parts_ordered_oomp != []:
        dst_directory = os.path.dirname(filename)
        #make a labels directory
        dst_directory = os.path.join(dst_directory, "label")
        if not os.path.exists(dst_directory):
            os.makedirs(dst_directory)
        for row in parts_ordered_oomp:
            part_id = row["oomp_id"]
            part_id = part_id.replace("oomp_", "")
            #copy label
            src_dir = f"C:/GH/oomlout_oomp_part_src/parts/{part_id}/working"                        
            
            label_copy_deets = []
            src_extra = "working_label_76_2_mm_50_8_mm.pdf"                        
            dst_extra = f"full/{src_extra.replace('working_label',part_id)}"
            label_copy_deets.append([src_extra, dst_extra])

            src_extra = "working_label_15_mm_30_mm.pdf"                        
            dst_extra = f"niimbot/{src_extra.replace('working_label',part_id)}"
            label_copy_deets.append([src_extra, dst_extra])    
            
            for label_copy_deet in label_copy_deets:
                src =f"{src_dir}/{label_copy_deet[0]}"
                dst = f"{dst_directory}/{label_copy_deet[1]}"
                import shutil
                try:
                    #make dst directory if it doesn't exist
                    dst_dir = os.path.dirname(dst)
                    if not os.path.exists(dst_dir):
                        os.makedirs(dst_dir)
                    shutil.copyfile(src, dst)
                except Exception as e:
                    print(f"error copying {src} to {dst}")
                    print(e)
                    pass

def make_readme(**kwargs):
    file = kwargs.get('file', "")
    root = kwargs.get('root', "")
    yaml_file = kwargs.get('yaml_file', "")
    parts_ordered_oomp = []
    if file == "working.ods": 
        print(f"making readme for {root}")
        directory = os.path.dirname(yaml_file)
        dict_data = oom_yaml.load_yaml_directory(directory=directory)
        file_template = "templates/order_readme_template.md.j2"
        file_output = f"{directory}/readme.md"
        dict_data = dict_data
        files = []
        #get a list of recursive files
        import glob
        files = glob.glob(f"{directory}/**/*.*", recursive=True)
        #replace all \\ with /
        for i in range(len(files)):
            files[i] = files[i].replace("\\","/")
            #remove the directory from the file name
            files[i] = files[i].replace(f"{directory}/","")
        import copy
        files2 = copy.deepcopy(files)
        dict_data["files"] = files2
        oom_markdown.get_jinja2_template(file_template=file_template, file_output=file_output, dict_data=dict_data)


            


if __name__ == "__main__":
    main()