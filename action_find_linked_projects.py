import oomp
import os
import oomp_kicad
import oom_kicad


def main():

    oomp.load_parts(from_yaml=True)   
    
    #load_projects
    projects_yaml = "tmp/oomlout_oomp_project_bot/projects.yaml"
    #import projects from yaml
    import yaml
    with open(projects_yaml, 'r') as stream:
        print(f"loading projects from {projects_yaml}")
        projects = yaml.load(stream, Loader=yaml.FullLoader)

    for project_id in projects:
        project = projects[project_id]
        if "parts_oomp" in project:
            parts_oomp = project["parts_oomp"]
            for part_oomp in parts_oomp:
                part_id = part_oomp.get("oomp_part","unmatched")
                if part_id != "unmatched":
                    part_id = part_id.get("id","unmatched")
                    if part_id != "unmatched":
                        matched_part = oomp.parts.get(part_id, "unmatched")
                        if matched_part != "unmatched":
                            test_projects_this_part_is_in = matched_part.get("projects_this_part_is_in",{})
                            if project_id not in test_projects_this_part_is_in:
                                project_details = {}
                                project_details["project_id"] = project_id
                                test_projects_this_part_is_in[project_id] = project_details
                                matched_part["projects_this_part_is_in"] = test_projects_this_part_is_in    
                            else:
                                print(f"project {project_id} already in matched_part['projects_this_part_is_in']")
    oomp.save_parts_to_individual_yaml_files()
                    

    
    
    # oom_kicad.push_to_git()




if __name__ == "__main__":
    main()