import sounddevice as sd
from constant.colors import *
from CONFIG import LANGUAGE


def update_config(mic_index):
    with open('CONFIG.py', 'r') as file:
        lines = file.readlines()

    with open('CONFIG.py', 'w') as file:
        for line in lines:
            if line.startswith('MIC_INDEX'):
                file.write(f'MIC_INDEX = {mic_index}\n')
            else:
                file.write(line)

def select_microphone():
    try:
        devices = sd.query_devices()
        valid_ids = []
        for i, device in enumerate(devices):
            if device['max_input_channels'] > 0 and device['hostapi'] == 0:
                try:
                    sd.check_input_settings(device=i)
                    valid_ids.append(i)
                    print(f"{GREEN}Input Device id {RESET}", i, " - ", device['name'])
                except sd.PortAudioError:
                    pass

        if not valid_ids:
            print(f"{RED}Aucun périphérique d'entrée actif trouvé.{RESET}" if LANGUAGE == 'fr' else 
                  f"{RED}No active input devices found.{RESET}")
            return

        while True:
            try:
                device_index = int(input(f"Entrez l'ID du microphone souhaité: " if LANGUAGE == 'fr' else 
                                         f"Enter the microphone ID to use: "))
                if device_index in valid_ids:
                    update_config(device_index)
                    return device_index
                else:
                    print(f"{RED}Veuillez entrer un micro valide{RESET}" if LANGUAGE == 'fr' else 
                          f"{RED}Please enter a valid microphone ID.{RESET}")
            except ValueError:
                print(f"{RED}Veuillez entrer un nombre valide{RESET}" if LANGUAGE == 'fr' else 
                      f"{RED}Please enter a valid integer.{RESET}")
    except AttributeError as e:
        print(f"{RED}Erreur: {e}{RESET}" if LANGUAGE == 'fr' else f"{RED}Error: {e}{RESET}")
        print(f"{RED}Assurez-vous que la bibliothèque sounddevice est correctement installée et à jour.{RESET}" if LANGUAGE == 'fr' else 
              f"{RED}Make sure the sounddevice library is correctly installed and up to date.{RESET}")
