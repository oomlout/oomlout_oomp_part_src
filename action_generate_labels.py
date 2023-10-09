import oomp
import os
import oomp_kicad
import oom_kicad

####### action_generate_pinouts.py -- check all footprints for parts, if the part has a footprint, check if it has a pinout svg, if it does if it has pin names replace them and create.

###### process
#
# load parts
# loop through parts
# if part has footprint
#   if part has pinout svg
#       replace pin names
#       create pdf
#
# open inkscape 
# import footprint working.pdf
# save as working_pinout.svg
# grab the template 
#   templates/working_pinout_template.svg
# add the pin names
# 
# todo
#  work on style
#  maybe put pin name inside


#directory_footprint_bot = "C:/GH/oomlout_oomp_footprint_bot/footprints"
directory_footprint_bot = "tmp/oomlout_oomp_footprint_bot/footprints"

import oom_svg

#label sizes
# main 76 x 50
# tiny 02_02 smd 8 x 12
# normal smd_magazine 8 x 25
# full size smd 15 x 30
def main(**kwargs):

    oomp.load_parts(from_pickle=True)   
    overwrite = kwargs.get("overwrite", False)
    #filter = "electronic_ic_lga_12_pin_2_mm_x_2_mm_sensor_accelerometer_sensortek_stk8321"
    #filter =  "electronic_resistor_0603_10000_ohm"
    #filter = "electronic_led_0603_yellow"    
    #filter = "electronic_capacitor_0603_100_nano_farad"
    filter = ""

    for part_id in oomp.parts:
        if filter in part_id:
            part = oomp.parts[part_id]
            part_directory = part.get("directory", "")        
            file_templates = []
            file_templates.append(f"templates/template_label_76_2_mm_50_8_mm_multi.svg")
            #file_templates.append(f"templates/template_label_15_mm_30_mm.svg")
            file_templates.append(f"templates/template_label_76_2_mm_50_8_mm.svg")

            for file_template in file_templates:
                file_extra = file_template.replace("template_","").replace("templates/","").replace(".svg","")
                file_label = f"{part_directory}/working/working_{file_extra}.svg"
            
                svg_infile = file_template
                svg_outfile = file_label
                svg_dict = part
                #if svg_outfile doesn't exist or overwrite
                if not os.path.exists(svg_outfile) or overwrite:                    
                    print(f"creating {svg_outfile}")
                    oom_svg.svg_dict_replace(svg_infile=svg_infile,svg_outfile=svg_outfile,svg_dict=svg_dict)
                    file_in = svg_outfile
                    oom_svg.svg_make_pdf(file_in=file_in)
                    oom_svg.svg_make_png(file_in=file_in, export_dpi=300)
                    pass
                else:
                    print(f"skipping {svg_outfile}")

def copy_labels_to_directory(**kwargs):

    if oomp.parts == {}:
        oomp.load_parts(from_pickle=True) 

    print("copying labels to directory")
    filter = kwargs.get("filter", "")
    
    file_templates = []
    file_templates.append(f"templates/template_label_76_2_mm_50_8_mm_multi.svg")
    #file_templates.append(f"templates/template_label_15_mm_30_mm.svg")
    file_templates.append(f"templates/template_label_76_2_mm_50_8_mm.svg")

    for part_id in oomp.parts:
        part = oomp.parts[part_id]
        short_code = part.get("short_code", "")
        if filter in part_id:
            for template in file_templates:
                directory_source = "parts/" + part_id + "/working"
                file_name = template.replace("template_","working_").replace("templates/","").replace(".svg",".pdf")
                file_source = f"{directory_source}/{file_name}"
                directory_output = f"tmp/labels/{file_name.replace('.pdf','')}"
                directory_code_output = f"tmp/labels/{file_name.replace('.pdf','')}/000_code"
                file_output = f"{directory_output}/{part_id}.pdf"
                file_output_code = f"{directory_code_output}/{short_code}_code.pdf"
                import shutil
                #creater directory if it doesn't exist                
                os.makedirs(directory_output, exist_ok=True)
                os.makedirs(directory_code_output, exist_ok=True)

            
                
                try:
                    shutil.copyfile(file_source, file_output)
                    shutil.copyfile(file_source, file_output_code)
                except Exception as e:
                    print(f"error {e}")
                    pass




if __name__ == "__main__":
    main()
    copy_labels_to_directory()