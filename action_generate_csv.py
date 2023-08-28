import os
import oomp
import jinja2

def main_full(**kwargs):
    oomp.load_parts(from_pickle = True)
    count = 1
    #dump oomp.parts to a csv file
    import csv
    #if csv directory doesn't exist create it
    if not os.path.exists("csv"):
        os.makedirs("csv")

    with open('csv/parts.csv', 'w', newline='') as csvfile:
        #go through all the parts make create a proto part that has all the keys
        #this is so we can get a list of all the keys
        flat_parts = {}
        proto_part = {}
        append_to_front = ["id", "short_code"]
        append_to_end = ["distributors", "manufacturers", "footprint", "symbol", "pins"]
        remove = ["make_files", "from_yaml", "filter"]
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
            writer.writerow(part)
            count += 1
            # print a . for every 100
            if count % 100 == 0:
                print(".", end="", flush=True)


def main_other(**kwargs):
    #if csv directory doesn't exist create it
    if not os.path.exists("csv"):
        os.makedirs("csv")
    filename = "csv/minimal.csv"
    headings = ["id", "short_code", "name", "github_link", "oomp_key", "md5_6"]
    import copy
    p2 = copy.deepcopy(oomp.parts)
    get_details(filename=filename, headings=headings)




def get_details(**kwargs):
    filename = kwargs.get("filename", "")
    headings = kwargs.get("headings", [])
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
            part = flat_parts[part_id]
            writer.writerow(part)
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



if __name__ == "__main__":
    main_full()
    main_other()