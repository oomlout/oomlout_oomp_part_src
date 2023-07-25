
def get_short_name(**kwargs):
    replace_dict = {}
    #don't do it if short_name already exists
    if "short_name" in kwargs:
        return kwargs["short_name"]
    else:
        #if an led
        short_name = ""
        if kwargs["type"] == "led":
            short_name = f"{kwargs['size']}_{kwargs['color']}{kwargs['description_main']}_led"
        
        #headers
        elif kwargs["type"] == "header":
            #if size is 2d54_mm
            if kwargs["size"] == "2d54_mm":
                short_name = f"{kwargs['size']}_{kwargs['description_main']}_{kwargs['description_extra']}_{kwargs['type']}"
                short_name = short_name.replace("2d54_mm",'0.1"')
                pass
            #if size is 2_mm_jst_ph
            elif kwargs["size"] == "2_mm_jst_ph":
                short_name = f"{kwargs['size']}_{kwargs['description_main']}_{kwargs['description_extra']}_{kwargs['type']}_2_mm_pitch"
                short_name = short_name.replace("2_mm_jst_ph",'JST_PH')
                pass
            #if size is 2d54_mm_jst_xh
            elif kwargs["size"] == "2d54_mm_jst_xh":
                short_name = f"{kwargs['size']}_{kwargs['description_main']}_{kwargs['description_extra']}_{kwargs['type']}_2.54_mm_pitch"
                short_name = short_name.replace("2d54_mm_jst_xh",'JST_XH')
                pass
            #if size is 1_mm_jst_sh
            elif kwargs["size"] == "1_mm_jst_sh":
                short_name = f"{kwargs['size']}_{kwargs['description_main']}_{kwargs['description_extra']}_{kwargs['type']}_1_mm_pitch"
                short_name = short_name.replace("1_mm_jst_sh",'JST_SH')
                pass
        #mounting holes
        elif kwargs["type"] == "mounting_hole":
            short_name = f"{kwargs['size']}_{kwargs['description_main']}_{kwargs['type']}"
            
            pass



        short_name = short_name.replace("__", "_")
        short_name = short_name.replace("__", "_")
        short_name = short_name.replace("__", "_")
        short_name = short_name.replace("_", " ")
        short_name = short_name.title()


    return short_name
