presets:
    
file_name
time_from_start(s), mode/effect,para0,para1,para2,para3,para4,para5

need:
    get_preset -> list[[]] done!
    set_preset done!
    add_preset_line
    delete_preset_line
    change_preset
    delete_preset
    
    active_preset -> loop through preset and set a time variable for the next preset to be triggred,
                     then loop through the preset to get the information
    