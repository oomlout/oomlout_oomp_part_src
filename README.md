# oomlout_oomp_v3
oopen organization method for parts take three

## parts
current parts list [parts_readme.md](readme_parts.md)

## files

### summary

* base/
  * oomp.py -- the main hold everything together file imports everything needed and holds the dictionary
  * oomp_create_parts.py -- where the parts are created 
    * oomp_create_parts_led.py -- led part details
  * oomp_kicad.py -- where all the kicad stuff is sorted,
   *  oomp_kicad_footprint.py -- footprint matching is done
  * oomp_working.py -- where things are tested
* base/kicad
  * base/kicad/footprints -- location of footprint libraries
  * base/kicad/symbols -- location of symbols
* base/src
  * files
    * put the item that you want copied to the correct directory filename format (id)_(type)
      * id can be full name or hash
      * types can be
        * _datasheet.pdf
        * _image.jpg



## name

### composition

This is composed of up to eight parts. Not all parts are neccesary and are in full text, all special charachters and spaces are replaced with _

1. classification -- the class of item (electronic, mechanical, fastener)
1. type -- the type of part (led)
2. size -- the defining size (5_mm, 0603_smd)
3. color -- a color or defining visual characteristic or material (red, metal, nylon)
4. description_main -- the main defining parameter (standard, tinted, 60_microfarads, 560_ohms
5. description_extra -- an extra defining charachteristic (right_angle, surface_mount)
6. manufacturer -- the name of the manufacturer
7. part_number -- the part number of the item

## actions

* action_setup.py -- gets everything setup
* action_all.py -- runs through everything, creates parts, makes readmes makes readme index, does image reolutions, copies files
* action_copy_src_to_directories.py -- copy the details from the src directory to the various directories
* action_generate_outputs -- generates symbol library and footprint library and readmes
* action_generate_pinouts.py -- check all footprints for parts, if the part has a footprint, check if it has a pinout svg, if it does if it has pin names replace them and create.
* action_find_linked_projects.py -- add all the projects that use each part to the yaml
* action_generate_readme.py -- generate the readmes using pelican
* action_copy_footprints_and_symbols.py -- copy the footprint and symbol files to the right directory
* action_generate_list_of_used_footprints_and_symbols.py -- make a yaml of the used footprints and symbols (used_footprints.yaml and used_symbols.yaml)
* action_generate_readme_index.py -- generate the index for navigtaing the readmes
* action_generate_doc.py -- copy the neccesary fioles to doc