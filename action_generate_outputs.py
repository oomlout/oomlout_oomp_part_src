import oomp
import os
import oomp_kicad
import oom_kicad


def main():

    git_commit = False
    git_commit = True

    oomp.load_parts(from_pickle=True)   
    
    oomp_kicad.create_footprint_library()
    
    if git_commit:
        oom_kicad.push_to_git(repo_directory = "tmp/generated/oomlout_oomp_part_kicad_footprints")
    
    
    oomp_kicad.create_symbol_library()
    
    
    if git_commit:
        oom_kicad.push_to_git(repo_directory = "tmp/generated/oomlout_oomp_part_kicad_symbols")
    



if __name__ == "__main__":
    main()