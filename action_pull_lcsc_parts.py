import oomp



def main():
    output_file = "tmp/lcsc_data/lcsc_parts.yaml"
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
                    match["part_id"] = part_id
                    match["part_number"] = f"C{lcsc}"
                    matches.append(match)
                    
                else:
                    print(f"no match found for {part_id} - {part_number}, manufacturer {manufacturer['name']}, ")
#dump matches to yaml
    import yaml
    with open(output_file, 'w') as file:
        yaml.dump(matches, file)
            

    code_dump_file = "tmp/lcsc_data/lcsc_parts.txt"
    with open(code_dump_file, 'w') as file:
        for match in matches:
            part_id = match["part_id"]
            part_number = match["part_number"]
            line = '    matches.append({"id":"' + part_id +'",\n'
            line += '                  "part_number": "' + part_number + '"})\n'
            line += '\n'


            file.write(line)    
    




if __name__ == "__main__":
    main()