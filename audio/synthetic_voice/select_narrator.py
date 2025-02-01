import pyttsx3
from CONFIG import LANGUAGE
from constant.update_config import update_config


def get_voice_list():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    voice_dict = {i: voice for i, voice in enumerate(voices)}
    return voice_dict

def manage_voice():
    voices = get_voice_list()
    voice_names = [voices[i].name for i in voices]
    
    # Shows voice options with indexes
    for idx, name in enumerate(voice_names, start=1):
        print(f"{idx}. {name}")
    
    # Asks the user to select a voice via the index
    selected_index = int(input("Entrez le nombre correspondant à la voix que vous souhaitez utiliser: " if LANGUAGE == 'fr' else 
                               "Enter the number corresponding to the voice you want to use: ")) - 1

    if selected_index < 0 or selected_index >= len(voice_names):
        print("Invalid index")
        return None

    selected_voice_name = voice_names[selected_index]
    selected_voice_id = [voice.id for voice in voices.values() if voice.name == selected_voice_name][0] if selected_voice_name else ''

    if LANGUAGE == "fr":
        print(f"ID de la Voix du Narrateur sélectionné: {selected_voice_id}")
    else:
        print(f"Selected Narrator Voice ID: {selected_voice_id}")

    # Updates CONFIG.py with update_config function
    update_config('NARRATOR_VOICE', f'"{selected_voice_id}"')

    return selected_voice_id