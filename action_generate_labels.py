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

def main():

    oomp.load_parts(from_pickle=True)   
    
    filter = "electronic_ic_lga_12_pin_2_mm_x_2_mm_sensor_accelerometer_sensortek_stk8321"
    filter = ""

    for part_id in oomp.parts:
        if filter in part_id:
            part = oomp.parts[part_id]
            part_directory = part.get("directory", "")        
            file_templates = []
            file_templates.append(f"templates/template_label_15_mm_30_mm.svg")
            file_templates.append(f"templates/template_label_76_2_mm_50_8_mm.svg")

            for file_template in file_templates:
                file_extra = file_template.replace("template_","").replace("templates/","").replace(".svg","")
                file_label = f"{part_directory}/working/working_{file_extra}.svg"
            
                svg_infile = file_template
                svg_outfile = file_label
                svg_dict = part
                oom_svg.svg_dict_replace(svg_infile=svg_infile,svg_outfile=svg_outfile,svg_dict=svg_dict)
                file_in = svg_outfile
                oom_svg.svg_make_pdf(file_in=file_in)
                oom_svg.svg_make_png(file_in=file_in, export_dpi=300)
                pass
            



if __name__ == "__main__":
    main()