import oom_base



def main():
    overwrite = True
    overwrite = False
    #go through all files in symbols/
    directory = "parts"
    oom_base.image_resolutions_dir(directory=directory, overwrite=overwrite)
    

if __name__ == '__main__':
    main()
