import oom_base



def main(**kwargs):
    overwrite = False
    directory = "parts"
    oom_base.image_resolutions_dir(directory=directory, overwrite=overwrite)




if __name__ == "__main__":
    main()