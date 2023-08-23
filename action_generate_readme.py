import os
import oomp
import jinja2

def main(**kwargs):
    oomp.load_parts(from_pickle = True)
    for part_id in oomp.parts:
        part = oomp.parts[part_id]
        directory = part.get("directory","")
        if directory == "":
            print(f"part {part_id} has no directory")
            return
        directory = f"{directory}/working"
        file_readme = os.path.join(directory,"readme.md")
        template_file = f"templates/part_readme_template.j2"
        part_flat = flatten_dict(part)
        markdown_string = ""
        with open(template_file, "r") as infile:
            markdown_string = infile.read()
        ##### sanitize part
        import copy
        part2 = copy.deepcopy(part)
        check_items = ["pins", "footprint", "symbol"]
        for check_item in check_items:
            if check_item not in part2:
                part2[check_item] = {}
        



        markdown_string = jinja2.Template(markdown_string).render(part2)
        with open(file_readme, "w") as outfile:
            outfile.write(markdown_string)
        x=1
    

def flatten_dict(d, parent_key='', separator='_'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{separator}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, separator=separator).items())
        else:
            items.append((new_key, v))
    return dict(items)




if __name__ == "__main__":
    main()