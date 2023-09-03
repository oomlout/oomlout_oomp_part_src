import oomp

def main(** kwargs):
    oomp.load_parts(from_pickle=True)
    for part_id in oomp.parts:
        part = oomp.parts[part_id]
        directory_part = part.get("directory", "")
        types = ["footprint", "symbol"]
        #types = ["footprint"]
        for type in types:
            directory_type = f"{directory_part}/working/{type}"
            list = part.get(f"{type}", [])
            count = 0
            for item in list:
                directory_item_dst = f"{directory_type}/{count}/working"
                directory_item_original = item['directory'].replace("working.kicad_mod", "").replace("working.kicad_sym", "")
                directory_item_src = f"tmp/{directory_item_original}"
                #copy from src to dst overwrite if file exists using shutil
                import shutil
                #remove double slashes
                directory_item_src = directory_item_src.replace("//","/")
                shutil.copytree(directory_item_src, directory_item_dst, dirs_exist_ok=True)
                print(f"copied {directory_item_src} to {directory_item_dst}")
                count += 1


if __name__ == "__main__":
    main()