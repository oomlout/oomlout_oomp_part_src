import oomp



def main(**kwargs):
    oomp.load_parts(from_pickle = True)

    readme_contents = generate_readme(oomp.parts)
    readme_file = "readme_index.md"
    with open(readme_file, "w") as outfile:
        outfile.write(readme_contents)

def generate_readme(components):
    return_value = ""
    # Create an empty index dictionary
    index = {}
    # Group components based on hierarchy
    for component_id in components:
        component = components[component_id]
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
                return_value += f'[{component["oomp_key"]}]({component["directory"]}/working)   \n'
                #return_value += f'{indentation} Part Number:{component["part_number"]}   \n'
    return return_value                    
    

if __name__ == "__main__":
    main()