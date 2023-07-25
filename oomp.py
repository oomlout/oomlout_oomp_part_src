
import oomp_create_parts
import oomp_kicad_footprint
import oomp_kicad_symbol
import oomp_short_code
import oomp_short_name
import oomp_distributors

parts = {}
parts_md5 = {}
parts_md5_5 = {}
parts_md5_6 = {}
parts_md5_10 = {}
parts_short_code = {}


names_of_main_elements = ["classification", "type", "size", "color", "description_main", "description_extra", "manufacturer", "part_number"]


def load_parts(**kwargs):
    oomp_create_parts.load_parts(**kwargs)

def create_parts_readme():
    #create a file called parts_readme.md that links to all the parts in the parts directory
    readme = ""
    readme += "# Parts\n"
    readme += "\n"
    for part in parts:
        readme += f"[{parts[part]['name']}](parts/{parts[part]['id']}/readme.md)\n"
    with open("readme_parts.md", "w") as outfile:
        outfile.write(readme)

    


def add_parts(parts, make_files=True):
    #expand the parts list into parts_processed, make this a list of permutations of the part using itertools
    import itertools

    # Initialize an empty dictionary for lists
    my_dict_lists = {}

    # Convert all the dictionary values to lists but only use the keys in names_of_main_elements
    
    for part in parts:
        # get all the dict values that aren't in names_of_main_elements 
        not_main_elements = {}
        for key, value in part.items():
            if key not in names_of_main_elements:
                not_main_elements[key] = (part[key])
        for key, value in part.items():
            #only check if the key is in names_of_main_elements
            if key in names_of_main_elements:
                # Check if the value is a string
                if isinstance(value, str):
                    # If it is, convert it to a list and add to the new dictionary
                    my_dict_lists[key] = [value]
                else:
                    # If it's not a string, we assume it's a list and add it to the new dictionary as is
                    my_dict_lists[key] = value

        # Prepare a list to hold the combinations
        combinations = []

        # The itertools.product function takes any number of arguments, 
        # but we have a list of lists, so we need to "unpack" this list 
        # into separate arguments using the * operator.
        # This will generate a Cartesian product of the given lists,
        # i.e., all possible combinations of the elements in the lists.
        for combo in itertools.product(*my_dict_lists.values()):
            # Add each combination to our list of combinations
            combinations.append(combo)

        # Print all combinations
        for combo in combinations:
            add_part(classification=combo[0], type=combo[1], size=combo[2], color=combo[3], description_main=combo[4], description_extra=combo[5], manufacturer=combo[6], part_number=combo[7], not_main_elements=not_main_elements, make_files=make_files)
        

def copy_files():
    pass

def add_part(**kwargs):
    make_files = kwargs.get("make_files", True)

    #pop out the not_main_elements from kwargs
    not_main_elements = kwargs.pop("not_main_elements")
    #add them back as regular keys
    for key, value in not_main_elements.items():
        kwargs[key] = value

    ## get id
    id = get_id(**kwargs)
    
    
    
    ## add part to dict
    print("    adding part " + id)
    
    #add id as a keyed item to kwargs
    kwargs["id"] = id
    
    #add the directory
    kwargs["directory"] = f'parts/{id}'

    #add name, the name is the id with proper capitalization and _ replaced with ' '
    kwargs["name"] = id.replace("_", " ").title()
    
    #add short code from a get_short_code function
    kwargs["short_code"] = oomp_short_code.get_short_code(**kwargs)
    parts_short_code[kwargs["short_code"]] = kwargs["id"]
    
    # add short name from a get_short_name function
    short_name = oomp_short_name.get_short_name(**kwargs)
    if short_name != "":
        kwargs["short_name"] = short_name


    #add distributors from a function get_distributors in oomp_distributors.py
    
    kwargs = oomp_distributors.get_distributors(**kwargs)



    #add a md5 hash of the id as a keyed item to kwargs
    import hashlib
    kwargs["md5"] = hashlib.md5(id.encode()).hexdigest()
    #trim md5 to 6 and add it as md5_6
    kwargs["md5_5"] = kwargs["md5"][0:5]
    #add to md5_5 dict
    parts_md5_5[kwargs["md5_5"]] = id
    kwargs["md5_6"] = kwargs["md5"][0:6]    
    parts_md5_6[kwargs["md5_6"]] = id
    kwargs["md5_10"] = kwargs["md5"][0:10]
    parts_md5_10[kwargs["md5_10"]] = id
    

    ## print part nicely indented by six spaces
    ### print("      " + str(kwargs).replace(", ", ",\n      "))

    if make_files:
        ######### file stuff
        
        ## make a directory in /parts for the part the name is its id
        import os
        if not os.path.exists("parts/" + id):
            os.makedirs("parts/" + id)
        
        ## write the part details in json to the directory name the file details.json
        import json
        with open("parts/" + id + "/details.json", "w") as outfile:
            json.dump(kwargs, outfile, indent=4)
        ## write the part details in yaml to the directory name the file details.json
        import yaml
        with open("parts/" + id + "/details.yaml", "w") as outfile:
            yaml.dump(kwargs, outfile, indent=4)

        file_types = ["datasheet.pdf", "image.jpg", "image_reference.jpg"]
        #for each file type look in the src directory for a file named (id)_(file_type) if it exists copy it to the parts directory as the file_type name
        for file_type in file_types:
            import os.path
            if os.path.isfile("src/" + id + "_" + file_type):
                import shutil
                shutil.copy("src/" + id + "_" + file_type, "parts/" + id + "/" + file_type)

    

        ### eda stuff
        kwargs = oomp_kicad_footprint.get_footprints(**kwargs)
        kwargs = oomp_kicad_symbol.get_symbols(**kwargs)

        #call pass the part to a function to gebneratre a readme.md file then save it
        readme = generate_readme(**kwargs)
        with open("parts/" + id + "/readme.md", "w") as outfile:
            outfile.write(readme)


    parts[id] = kwargs


def generate_readme(**kwargs):
    #generate a readme.md file for the part
    readme = ""
    readme += "# " + kwargs["name"] + "\n"
    readme += "\n"
    readme += "## Description\n"
    readme += "\n"
    readme += "## Properties\n"
    readme += "\n"
    
    ## datasheet
    ### add datasheet link if datasheet.pdf is a file in the parts directory
    import os.path
    if os.path.isfile("parts/" + kwargs["id"] + "/datasheet.pdf"):
        readme += "\n"
        readme += "![Datasheet](datasheet.pdf)\n"
    readme += "\n"
    
    ## images 
    readme += "## Image\n"
    readme += "\n"
    images = ["image.jpg", "image_reference.jpg"]
    ### add images if any of the image files exist
    for image in images:
        if os.path.isfile("parts/" + kwargs["id"] + "/" + image):
            readme += "\n"
            #add image use an f string
            readme += f"![{kwargs['name']} image]({image})\n"
            readme += "\n"
    
    ## add all values in the dict to a table
    readme += "\n"
    readme += "## Values\n"
    readme += "\n"
    readme += "| Key | Value |\n"
    readme += "| --- | --- |\n"
    for key, value in kwargs.items():
        #if the value is a list add each value on a new line, also handle it if its a dict also handle if its a nested list or dict
        if isinstance(value, list):
            value_string = ""
            for item in value:
                #add a way to unwrap nested lists and dicts
                if isinstance(item, list):
                    value_string += "<br>"
                    for subitem in item:
                        value_string += f"  - {subitem}\n"
                elif isinstance(item, dict):
                    value_string += "<br>"
                    for subitem in item:
                        value_string += f"  - {subitem}: {item[subitem]}<br>"
                else:
                    value_string += f"  - {item}<br>"
                
        readme += "| " + key + " | " + str(value) + " |\n"
    readme += "\n"  

    ## add notes
    readme += "## Notes\n"
    readme += "\n"
    return readme


def get_id(**kwargs):
    #concate all the elements in kwargs from names_of_main_elements with '_' and return the string if the element isn't '' include it
    id = ""
    for name in names_of_main_elements:
        if kwargs[name] != "":
            id += kwargs[name] + "_"
    #remove the trailing '_'
    id = id[:-1]
    return id






    