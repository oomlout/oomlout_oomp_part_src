import os
import oomp
import jinja2

def main(**kwargs):
    oomp.load_parts(from_pickle = True)
    count = 1
    for part_id in oomp.parts:
        part = oomp.parts[part_id]
        directory = part.get("directory","")
        if directory == "":
            print(f"part {part_id} has no directory")
            return
        directory = f"{directory}/working"
        file_readme = os.path.join(directory,"readme.md")
        template_file = f"templates/part_readme_template.md.j2"
        part_flat = flatten_dict(part)
        markdown_string = ""
        with open(template_file, "r") as infile:
            markdown_string = infile.read()
        ##### sanitize part
        import copy
        part2 = copy.deepcopy(part)
        
        



        markdown_string = jinja2.Template(markdown_string).render(p=part2)
        with open(file_readme, "w") as outfile:
            outfile.write(markdown_string)
        count += 1
        # print a . for every 100
        if count % 100 == 0:
            print(".", end="", flush=True)
    

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