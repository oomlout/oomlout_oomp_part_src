import oomp
import os
import yaml


def main(**kwargs):
    oomp.load_parts(from_pickle = True)

    generate_index()
    generate_collections(**kwargs)

def generate_collections(**kwargs):
    #get all the yaml filenames in colelctions directory
    import glob
    collection_files = glob.glob("collections/*.yaml")
    for collection_file in collection_files:
        just_filename = os.path.basename(collection_file)
        filename = f"collections/{just_filename}.md"        
        with open(collection_file, "r") as infile:
            components = yaml.load(infile, Loader=yaml.FullLoader)
        generate_index(components=components, filename=filename)

def generate_index(**kwargs):
    
    filename = kwargs.get("filename", "readme_index.md")
    components = kwargs.get("components", oomp.parts)
    print(f"generating index {filename}")
    readme_contents = generate_readme(components)
    readme_file = filename
    with open(readme_file, "w") as outfile:
        outfile.write(readme_contents)

def generate_readme(components):
    return_value = ""
    # Create an empty index dictionary
    index = {}
    # Group components based on hierarchy
    for component_id in components:
        #if components is a dict
        if isinstance(components, dict):
            component = components[component_id]
        else:
            try:
                component = oomp.parts[component_id.replace("oomp_", "")]
            except:
                print(f"component {component_id} not found")
                break
        classification = component["classification"]
        component_type = component["type"]
        size = component["size"]
        color = component["color"]
        
        if classification not in index:
            index[classification] = {}
        if component_type not in index[classification]:
            index[classification][component_type] = {}
        if size not in index[classification][component_type]:
            index[classification][component_type][size] = {}
        if color not in index[classification][component_type][size]:
            index[classification][component_type][size][color] = []
        
        index[classification][component_type][size][color].append(component)
    return_value = print_index(index)
    return return_value




# Print the index
def print_index(index, indent=0):
    return_value = ""
    for key, value in index.items():
        return_value += "#" * indent + "# " + key + "   \n"
        if isinstance(value, dict):
            return_value += print_index(value, indent + 1)
        else:
            for component in value:
                #return_value += "  " * (indent + 1) + "- Component:", component["description_main"] + "   \n"
                indentation = "  " * (indent + 1)
                #return_value += indentation + "Link:", component.get("link", "") + "   \n"
                url_base  = "https://github.com/oomlout/oomlout_oomp_part_src/tree/main"
                return_value += f'[{component["oomp_key"]}]({url_base}/{component["directory"]}/working)   \n'
                #return_value += f'{indentation} Part Number:{component["part_number"]}   \n'
    return return_value                    
    

if __name__ == "__main__":
    main()