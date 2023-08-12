import oomp
import os
import oomp_kicad
import oom_kicad


def main():

    oomp.load_parts(from_yaml=True)   
    
    for root, dirs, files in os.walk("parts"):
        #go through all files
        for file in files:
            #check for a brd file
            
            filename = os.path.join(root, file)
            filter = ["sparkfun","adafruit","omerk"]
            filter = ["omerk"]
            filter = [""]
            #filter = ["microsd_yamaichi_pjs_vert"]
            if any(x in filename for x in filter):
                if "working.yaml" in filename:                    
                    oomp.generate_readme(filename=filename)
    
    
    
    oomp_kicad.create_footprint_library()
    oom_kicad.push_to_git(repo_directory = "c:/gh/oomlout_oomp_part_kicad_footprints")
    oomp_kicad.create_symbol_library()
    oom_kicad.push_to_git(repo_directory = "c:/gh/oomlout_oomp_part_kicad_symbols")
    #oom_kicad.push_to_git()




if __name__ == "__main__":
    main()