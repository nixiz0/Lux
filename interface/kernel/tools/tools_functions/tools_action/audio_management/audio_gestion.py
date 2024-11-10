from CONFIG import LANGUAGE

from kernel.tools.tools_functions.tools_action.audio_management.audio_change import set_volume, change_volume


def mute():
    # Volume Mute
    set_volume(0.0)
    return "Mute"

def demute():    
    # Volume deMute
    set_volume(0.5)
    return "Volume remis" if LANGUAGE == 'fr' else "Volume restarted"

def volume_increase():        
    # Volume Increase
    change_volume(0.2)
    return "Volume augmenté" if LANGUAGE == 'fr' else "Volume increased"

def volume_decrease():
    # Volume Decreases
    change_volume(-0.2)
    return "Volume diminué" if LANGUAGE == 'fr' else "Volume decreased"