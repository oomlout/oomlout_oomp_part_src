import os
import oomp
import oom_yaml
import jinja2
import oom_office


def make_collections(**kwargs):    
    print("Generating csv collections")
    directory = "collections"
    #get only the directories no Recursion
    dirs = [x[0] for x in os.walk(directory)]
    dirs = dirs[1:]
    for dir in dirs:
        make_collection(directory=dir)
        load_part_data_into_yaml(directory=dir)


def load_part_data_into_yaml(**kwargs):    
    directory = kwargs.get("directory", "")
    yaml_file = os.path.join(directory, "working.yaml")
    collection_data = oom_yaml.load_yaml_directory(directory=directory)
    #### load parts in 
    filt_raw = []
    parts = collection_data.get("parts", "")
    #append parts
    if parts != "":
        for part in parts:
            filt_raw.append(part)
    
    #append parts_short_code
    short_code_parts = collection_data.get("parts_short_code", "")
    if short_code_parts != "":
        for part in short_code_parts:
            filt_raw.append(part)
    #laod shortcoides
    filt = []
    for value in filt_raw:
        part_id = oomp.search_for_part_id(value)   
        if part_id != "":     
            filt.append(part_id)

    oom_yaml.add_detail(yaml_file=yaml_file, detail=["parts_final",filt], add_markdown=True)

def make_collection(**kwargs):
    collection_name = kwargs.get("collection_name", "")    
    directory = kwargs.get("directory", "")
    print(f"Generating csv collection {directory}")
    if directory == "":
        directory = f"collections/{collection_name}"
    import yaml
    collection_data = oom_yaml.load_yaml_directory(directory=directory)
    
    filt = []
    parts = collection_data.get("parts", "")
    #append parts
    if parts != "":
        for part in parts:
            filt.append(part)
    
    #append parts_short_code
    short_code_parts = collection_data.get("parts_short_code", "")
    if short_code_parts != "":
        for part in short_code_parts:
            filt.append(part)
    

    filename = f"{directory}/working_label.csv"
    main_label(filename=filename, filter=filt)
    filename = f"{directory}/working.csv"
    main_full(filename=filename, filter=filt)

    

def main_full(**kwargs):    
    filename = kwargs.get("filename", 'csv/parts.csv')
    filt = kwargs.get("filter", [""])
    print(f"Generating csv full {filename}")
    oomp.load_parts(from_pickle = True)
    count = 1
    #dump oomp.parts to a csv file
    import csv
    #if csv directory doesn't exist create it
    if not os.path.exists("csv"):
        os.makedirs("csv")

    with open(filename, 'w', newline='') as csvfile:
        #go through all the parts make create a proto part that has all the keys
        #this is so we can get a list of all the keys
        flat_parts = {}
        proto_part = {}
        append_to_front = ["id", "short_code"]
        append_to_end = ["distributors", "manufacturers", "footprint", "symbol", "pins"]
        remove = ["make_files", "from_yaml", "filter"]
        for part_id in oomp.parts:

            #get list name
            part = oomp.parts.get(part_id, "")
            if part == "":
                print(f"getting from short_code {part_id}")
                part = oomp.parts_short_code.get(part_id, "")
                
            #remove some keys
            for item in remove:
                if item in part:
                    del part[item]
            #convert to ordered dict
            from collections import OrderedDict
            part = OrderedDict(part)
            #reorder the keys
            new_key_order = append_to_front
            for key in part.keys():
                if key not in append_to_end and key not in append_to_front:
                    new_key_order.append(key)
            for item in append_to_end:
                if item in part:
                    new_key_order.append(item)
            #make a new ordereddict 
            part2 = OrderedDict()
            for key in new_key_order:
                if key in part:
                    part2[key] = part[key]
            flat_part = flatten_dict(part2)
            flat_parts[part_id] = flat_part
            part = flat_part
            for key in part.keys():
                proto_part[key] = ""
        fieldnames = proto_part.keys()
        # some of the keys are dicts so add extra columns for them
        # not realt with
        #remove "id"
        fieldnames = list(fieldnames)
        
        
        
        

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for part_id in flat_parts:
            part = flat_parts[part_id]
            ###clip list filter
            include = False
            part_id_extra = f'{part["id"]}_{part["short_code"]}'
            
            for item in filt:
                if item.replace("oomp_","") in part_id_extra:
                    include = True
                
            



            if include:                
                writer.writerow(part)
                count += 1
                # print a . for every 100
                if count % 100 == 0:
                    print(".", end="", flush=True)
    
    oom_office.calc_convert_ods_to_xls(filename=filename)


def main_other(**kwargs):
    filter = kwargs.get("filter", [""])
    #if csv directory doesn't exist create it
    print(f"Generating csv other {filter}" )
    if not os.path.exists("csv"):
        os.makedirs("csv")
    filename = "csv/minimal.csv"
    headings = ["id", "short_code", "name", "github_link", "oomp_key", "md5_6"]
    import copy
    p2 = copy.deepcopy(oomp.parts)
    get_details(filename=filename, headings=headings, filter=filter)

def main_label(**kwargs):
    clip_list = kwargs.get("clip_list", None)
    filename = kwargs.get("filename", "csv/oomp_label.csv")
    filt = kwargs.get("filter", [""])
    #if csv directory doesn't exist create it
    print(f"Generating csv label {filename}" )
    if not os.path.exists("csv"):
        os.makedirs("csv")
    
    headings = ["id", "oomp_key", "id_no_class", "id_no_type", "md5_6", "md5_6_upper", "name", "short_code", "short_code_upper", "classification", "type", "type_first_letter", "type_first_letter_upper", "size", "size_only_numbers", "size_only_numbers_no_zeros", "color", "description_main", "description_only_numbers", "description_only_numbers_short", "description_extra", "manufacturer", "part_number", "short_name", "description_or_color", "description_or_color_upper"]
    
    import copy
    p2 = copy.deepcopy(oomp.parts)
    get_details(filename=filename, headings=headings, filter=filt, clip_list=clip_list)
    oom_office.calc_convert_ods_to_xls(filename=filename)


def get_details(**kwargs):
    filename = kwargs.get("filename", "")
    headings = kwargs.get("headings", [])
    filt = kwargs.get("filter", [""])
    oomp.load_parts(from_pickle = True)
    count = 1
    #dump oomp.parts to a csv file
    import csv
    with open(filename, 'w', newline='') as csvfile:
        #go through all the parts make create a proto part that has all the keys
        #this is so we can get a list of all the keys
        flat_parts = {}
        proto_part = {}
        append_to_front = ["id", "short_code"]
        append_to_end = ["distributors", "manufacturers", "footprint", "symbol", "pins"]
        remove = ["make_files", "from_yaml", "filter"]
        clip_list = kwargs.get("clip_list", None)
        #get a list of all fields
        for part_id in oomp.parts:
            part = oomp.parts[part_id]
            
            #remove some keys
            for item in remove:
                if item in part:
                    del part[item]
            #convert to ordered dict
            from collections import OrderedDict
            part = OrderedDict(part)
            #reorder the keys
            new_key_order = append_to_front
            for key in part.keys():
                if key not in append_to_end and key not in append_to_front:
                    new_key_order.append(key)
            for item in append_to_end:
                if item in part:
                    new_key_order.append(item)
            #make a new ordereddict 
            part2 = OrderedDict()
            for key in headings:
                if key in part:
                    part2[key] = part[key]
            flat_part = flatten_dict(part2)
            flat_parts[part_id] = flat_part
            part = flat_part
            for key in part.keys():
                proto_part[key] = ""
        fieldnames = proto_part.keys()
        # some of the keys are dicts so add extra columns for them
        # not realt with
        #remove "id"
        fieldnames = list(fieldnames)
        
        
        
        

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for part_id in flat_parts:
            
            #getting from id or short_code
            part = oomp.parts.get(part_id, "")            

            #add short code to id string
            part_id_extra = f'{part["id"]}_{part["short_code"]}'

            
            
            #if any of filter are in part_id include
            include_filter = False
            if filt != [""]:
                pass
            for item in filt:
                if item.replace("oomp_","") in part_id_extra:
                    include_filter = True
            



            
            ###clip list filter
            include = True
            if clip_list != None:
                if clip_list["type"] == "short_code":
                    if part["short_code"] not in clip_list["list"]:
                        include = False

            #make a part with only the right fields
            part2 = OrderedDict()
            for key in headings:
                if key in part:
                    part2[key] = part.get(key,"")

            
            if include_filter and include:
                writer.writerow(part2)
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
        if isinstance(v, list):
            #add the index to the key
            for i in range(len(v)):
                new_key2 = f"{new_key}{separator}{i}"
                items.extend(flatten_dict(v[i], new_key2, separator=separator).items())
        else:
            items.append((new_key, v))
    return dict(items)
