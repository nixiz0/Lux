from constant.colors import *
from CONFIG import LANGUAGE


def mic_record_threshold():
    # Ask user for microphone sensitivity
    threshold = input(f"{GREEN}Entrez la sensibilité du microphone (par défaut 500):{RESET} " if LANGUAGE == 'fr' else 
                      f"{GREEN}Enter the microphone sensitivity (default 500):{RESET} ")
    
    # Use default if user enters nothing
    if not threshold:
        threshold = 500
    else:
        threshold = int(threshold)
    
    # Read the contents of the CONFIG.py file
    with open('CONFIG.py', 'r') as file:
        config_content = file.readlines()
    
    # Change the value of AUDIO_THRESHOLD
    with open('CONFIG.py', 'w') as file:
        for line in config_content:
            if line.startswith('AUDIO_THRESHOLD'):
                file.write(f'AUDIO_THRESHOLD = {threshold}\n')
            else:
                file.write(line)
    
    print(f"{CYAN}La sensibilité du microphone a été définie à {threshold}{RESET}" if LANGUAGE == 'fr' else 
          f"{CYAN}Microphone sensitivity has been set to {threshold}{RESET}")
