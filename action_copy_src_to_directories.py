import os
import shutil

filenames_to_check = ["image.jpg","datasheet.pdf","datasheet.txt","image_reference.jpg"]

def main():
    #go through all files in src directory no recursion
    for root, dirs, files in os.walk("src"):
        #go trhough all files

        for file in files:
            for file_to_check in filenames_to_check:
                if file_to_check in file:
                    root = root.replace("\\","/")            
                    #split based on _
                    directory = file.replace(f"_{file_to_check}","")
                    filename = file_to_check
                    src = f"{root}/{file}"
                    dst = f"parts/{directory}/working/{filename}"
                    print(f"copying {src} to {dst}")
                    os.makedirs(f"parts/{directory}", exist_ok=True)
                    #if dst exists delete first
                    if os.path.exists(dst):
                        os.remove(dst)
                    #copy src to dst using shutil
                    
                    try:
                        shutil.copyfile(src, dst)
                    except:
                        print(f"could not copy {src} to {dst}")
                




if __name__ == "__main__":
    main()