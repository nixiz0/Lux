from CONFIG import LANGUAGE
from constant.colors import *
from constant.update_config import update_config


def mic_record_threshold():
    """
    Prompts the user to set the microphone sensitivity and updates the configuration file accordingly.

    The function asks the user to input a new microphone sensitivity value. If no value is provided, it defaults to 500.
    It then updates the 'AUDIO_THRESHOLD' setting in the 'CONFIG.py' file and confirms the new sensitivity value.
    """
    # Ask user for microphone sensitivity
    threshold = input(f"{GREEN}Entrez la sensibilité du microphone (par défaut 500):{RESET} " if LANGUAGE == 'fr' else 
                      f"{GREEN}Enter the microphone sensitivity (default 500):{RESET} ")
    
    # Use default if user enters nothing
    if not threshold:
        threshold = 500
    else:
        threshold = int(threshold)
    
    # Updates CONFIG.py with the universal update_config function
    update_config('AUDIO_THRESHOLD', threshold)
    
    print(f"{CYAN}La sensibilité du microphone a été définie à {threshold}{RESET}" if LANGUAGE == 'fr' else 
          f"{CYAN}Microphone sensitivity has been set to {threshold}{RESET}")