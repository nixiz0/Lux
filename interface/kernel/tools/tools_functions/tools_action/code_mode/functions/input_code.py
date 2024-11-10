import streamlit as st
import platform
import subprocess
import time
import os
from pathlib import Path
from CONFIG import LANGUAGE, TEMP_AUDIO_PATH
from kernel.tools.tools_functions.tools_action.code_mode.CONFIG_TOOL import *
from kernel.audio.speech_to_text.record import record_audio


def save_temp_code(code, detect_code_keywords):
    temp_folder = Path(TEMP_CODE_PATH) 
    temp_folder.mkdir(parents=True, exist_ok=True)
    temp_file = temp_folder / 'temp_code.txt'
    
    # Remove the trigger keywords from the code
    for keyword in detect_code_keywords:
        code = code.replace(keyword, '')
    with open(temp_file, 'w', newline='', encoding='utf-8') as file:
        file.write(code)
    # Open the file for the user to edit
    if platform.system() == 'Windows':
        os.startfile(temp_file)
    elif platform.system() == 'Darwin':  # macOS
        subprocess.run(['open', temp_file])
    else:  # linux variants
        subprocess.run(['xdg-open', temp_file])

def ask_user_intent(whisper, lux_voice):
    trigger_phrases = ["c'est bon", "j'ai déposé mon code", "code déposé", 
                       "it's okay", "I submitted my code", "code submitted", 
                       "it is okay", "okai", "ok", "okay"]
    
    st.warning(f"Pour continuer, dire:\n {trigger_phrases}\n") if LANGUAGE == 'fr' else \
    st.warning(f"To continue, say:\n{trigger_phrases}\n")

    # Wait until the user says one of the trigger phrases
    while True:
        record_audio()
        speech_transcribe = whisper.transcribe(TEMP_AUDIO_PATH)
        user_prompt = speech_transcribe
        st.write(user_prompt + "\n")
        if any(keyword in user_prompt for keyword in trigger_phrases):
            break
        time.sleep(1)

    if LANGUAGE == 'fr':
        lux_voice.speak("Que voulez-vous faire avec le code fourni ?")
    else: 
        lux_voice.speak("What do you want to do with the code provided ?")

    record_audio()
    user_intent = speech_transcribe = whisper.transcribe(TEMP_AUDIO_PATH)
    return user_intent