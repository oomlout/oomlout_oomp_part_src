import oomp
import os
import oomp_kicad
import oom_kicad

####### action_generate_pinouts.py -- check all footprints for parts, if the part has a footprint, check if it has a pinout svg, if it does if it has pin names replace them and create.


def main():

    oomp.load_parts(from_pickle=True)   
    
    for root, dirs, files in os.walk("parts"):
        #go through all files
        for file in files:
            #check for a brd file
            
            filename = os.path.join(root, file)
            filter = ["sparkfun","adafruit","omerk"]
            filter = ["omerk"]
            filter = [""]
            #filter = ["microsd_yamaichi_pjs_ver3t"]
            if any(x in filename for x in filter):
                if "working.yaml" in filename:                    
                    
                    pass
    
    



if __name__ == "__main__":
    main()