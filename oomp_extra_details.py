import oomp

def get_extra_details(**kwargs):
    
    import oomp_extra_details_hardware
    kwargs = oomp_extra_details_hardware.get_extra_details(**kwargs)

    return kwargs
    