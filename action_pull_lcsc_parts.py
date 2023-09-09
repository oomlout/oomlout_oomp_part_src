import oomp

def main():
    match()
    make_lcsc_basic_csv()
    #working()

def make_lcsc_basic_csv():
    output_file = "csv/lcsc_basic_parts.csv"
    sqllite_file_lcsc = "tmp/lcsc_data/cache.sqlite3"
    import sqlite3
    conn = sqlite3.connect(sqllite_file_lcsc)
    c = conn.cursor()
    
    #c.execute("SELECT * FROM components WHERE basic=1 LIMIT 5;")
    c.execute("SELECT * FROM components WHERE basic=1;")
    
    #dump result to a csv
    import csv
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([description[0] for description in c.description])
        writer.writerows(c)
    

def working():
    output_file = "src/distributor_matches_lcsc.yml"
    oomp.load_parts(from_pickle=True)
    sqllite_file_lcsc = "tmp/lcsc_data/cache.sqlite3"
    import sqlite3
    conn = sqlite3.connect(sqllite_file_lcsc)
    c = conn.cursor()
    #make a index with mfr as the key on table components
    
    #print("making index")
    
    #c.execute("CREATE INDEX mfr_index ON components (mfr);")
    c.execute("CREATE INDEX lcsc ON components (mfr);")
    
    #print("index made")
    #print list of tables
    #c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    #print(c.fetchall())
        #[('components',), ('manufacturers',), ('categories',)]
    #print the first component
    c.execute("SELECT * FROM components LIMIT 1;")
    #print(c.fetchall())
        #[(1002, 1, 'GZ1608D601TF', '0603', 2, 1, 1, '450mΩ ±25% 600Ω@100MHz 0603  Ferrite Beads ROHS', 'https://datasheet.lcsc.com/lcsc/2109180930_Sunlord-GZ1608D601TF_C1002.pdf', 328128, '[{"qFrom": 20, "qTo": 180, "price": 0.004323944}, {"qFrom": 200, "qTo": 780, "price": 0.003521127}, {"qFrom": 800, "qTo": 1580, "price": 0.003070423}, {"qFrom": 1600, "qTo": 9580, "price": 0.002788732}, {"qFrom": 9600, "qTo": 19980, "price": 0.00256338}, {"qFrom": 20000, "qTo": null, "price": 0.00243662}]', 1682999876, '{"id": 1354, "number": "C1002", "category": {"id1": 10991, "id2": 527, "name1": "Bead/Filter/EMI Optimization", "name2": "Ferrite Beads"}, "manufacturer": {"id": 270, "name": "Sunlord"}, "package": "0603", "title": "Sunlord GZ1608D601TF", "mpn": "GZ1608D601TF", "quantity": 264054, "quantity1": 218454, "quantity3": 45600, "moq": 1, "order_multiple": 100, "packaging": "Tape & Reel (TR)", "packaging_num": 4000, "prices": [{"min_qty": 100, "max_qty": 999, "currency": "USD", "price": 0.0048}, {"min_qty": 1000, "max_qty": 3999, "currency": "USD", "price": 0.0039}, {"min_qty": 4000, "max_qty": 7999, "currency": "USD", "price": 0.0034}, {"min_qty": 8000, "max_qty": 47999, "currency": "USD", "price": 0.0031}, {"min_qty": 48000, "max_qty": 99999, "currency": "USD", "price": 0.0028}, {"min_qty": 100000, "max_qty": 9999999, "currency": "USD", "price": 0.0027}], "datasheet": {"pdf": "https://datasheet.lcsc.com/lcsc/2109180930_Sunlord-GZ1608D601TF_C1002.pdf"}, "images": [{"96x96": "https://assets.lcsc.com/images/lcsc/96x96/20230331_Sunlord-GZ1608D601TF_C1002_front.jpg", "224x224": "https://assets.lcsc.com/images/lcsc/224x224/20230331_Sunlord-GZ1608D601TF_C1002_front.jpg", "900x900": "https://assets.lcsc.com/images/lcsc/900x900/20230331_Sunlord-GZ1608D601TF_C1002_front.jpg"}, {"96x96": "https://assets.lcsc.com/images/lcsc/96x96/20230331_Sunlord-GZ1608D601TF_C1002_back.jpg", "224x224": "https://assets.lcsc.com/images/lcsc/224x224/20230331_Sunlord-GZ1608D601TF_C1002_back.jpg", "900x900": "https://assets.lcsc.com/images/lcsc/900x900/20230331_Sunlord-GZ1608D601TF_C1002_back.jpg"}, {"96x96": "https://assets.lcsc.com/images/lcsc/96x96/20230331_Sunlord-GZ1608D601TF_C1002_blank.jpg", "224x224": "https://assets.lcsc.com/images/lcsc/224x224/20230331_Sunlord-GZ1608D601TF_C1002_blank.jpg", "900x900": "https://assets.lcsc.com/images/lcsc/900x900/20230331_Sunlord-GZ1608D601TF_C1002_blank.jpg"}], "rohs": true, "attributes": {"DC Resistance": "450m\\u03a9", "Impedance @ Frequency": "600\\u03a9@100MHz", "Circuits": "1", "Current Rating": "200mA", "Tolerance": "\\u00b125%"}, "description": "450m\\u03a9 \\u00b125% 600\\u03a9@100MHz 0603  Ferrite Beads ROHS", "url": "https://lcsc.com/product-detail/Ferrite-Beads_Sunlord-Sunlord-GZ1608D601TF_C1002.html"}', 1, 1693799506)]
    #print column names
    c.execute("SELECT * FROM components LIMIT 1;")
    print([description[0] for description in c.description])
        #['lcsc', 'category_id', 'mfr', 'package', 'joints', 'manufacturer_id', 'basic', 'description', 'datasheet', 'stock', 'price', 'last_update', 'extra', 'flag', 'last_on_stock']
    #print the first component
    
    #part_number = "RC0402JR-0710KL"
    
    #select where mfr equals part_number


def match():
    output_file = "src/distributor_matches_lcsc.yml"
    oomp.load_parts(from_pickle=True)
    sqllite_file_lcsc = "tmp/lcsc_data/cache.sqlite3"
    import sqlite3
    conn = sqlite3.connect(sqllite_file_lcsc)
    c = conn.cursor()
    #make a index with mfr as the key on table components
    print("making index")
    #c.execute("CREATE INDEX mfr_index ON components (mfr);")
    print("index made")
    #print list of tables
    #c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    #print(c.fetchall())
    #print the first component
    #c.execute("SELECT * FROM components LIMIT 1;")
    #print(c.fetchall())
    #print column names
    #c.execute("SELECT * FROM components LIMIT 1;")
    #print([description[0] for description in c.description])
    #print the first component
    
    #part_number = "RC0402JR-0710KL"
    
    #select where mfr equals part_number
    matches = []
    for part_id in oomp.parts:
        print(f"checking {part_id}")
        part = oomp.parts[part_id]
        manufacturers = part["manufacturers"]
        if len(manufacturers) > 0:
            for manufacturer in manufacturers:
                part_number = manufacturer["part_number"]
                #only select lcsc where mfr is part_number
                c.execute(f"SELECT * FROM components WHERE mfr='{part_number}';")                
                #if theres a match
                results = c.fetchall()
                if results:
                    lcsc = results[0][0]                    
                    match = {}
                    match["id"] = part_id
                    match["part_number"] = f"C{lcsc}"
                    matches.append(match)
                    
                else:
                    print(f"no match found for {part_id} - {part_number}, manufacturer {manufacturer['name']}, ")
#dump matches to yaml
    import yaml
    with open(output_file, 'w') as file:
        yaml.dump(matches, file)
            

    #code_dump_file = "src/distributor_matches_lcsc.yml"
    #with open(code_dump_file, 'w') as file:
    #    for match in matches:
    #        part_id = match["part_id"]
    #        part_number = match["part_number"]
    #        line = '    matches.append({"id":"' + part_id +'",\n'
    #        line += '                  "part_number": "' + part_number + '"})\n'
    #        line += '\n'


    #        file.write(line)    
    




if __name__ == "__main__":
    main()