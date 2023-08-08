import oomp




def main():
    oomp.clone_data_files()
    oomp.load_parts(from_yaml=False, make_files=True)
    oomp.save_parts()




if __name__ == "__main__":
    main()