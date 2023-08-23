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
    
    for part_id in oomp.parts:
        part = oomp.parts[part_id]
        part_directory = part.get("directory", "")
        if "footprint" in part:
            footprint = part.get("footprint", [])
            #if footprint is an array take element 0
            if isinstance(footprint, list):
                footprint = footprint[0]
            #if length is 3 or greater
            if len(footprint) >= 3:
                footprint_id = footprint["oomp_key"]
                footprint_id = footprint_id.replace("oomp_", "")
            pins = part.get("pins", {})
            #if more than one element in pins
            if len(pins) > 1:
                pinout_file = f"{directory_footprint_bot}/{footprint_id}/working/working_pinout.svg"
                if os.path.exists(pinout_file):
                    #part has a footprint, pins, and a pinout file
                    svg_infile = pinout_file
                    svg_outfile = f"{part_directory}/working/working_pinout.svg"
                    svg_dict = part
                    oom_svg.svg_dict_replace(svg_infile=svg_infile,svg_outfile=svg_outfile,svg_dict=svg_dict)
                    file_in = svg_outfile
                    oom_svg.svg_make_pdf(file_in=file_in)
                    oom_svg.svg_make_png(file_in=file_in, export_dpi=2400)
                    pass
                else:
                    x=2
                    pass
                x=3
                pass



if __name__ == "__main__":
    main()