import streamlit as st
import subprocess
import os
from CONFIG import LANGUAGE, TEMP_AUDIO_PATH
from kernel.tools.tools_functions.tools_action.code_mode.CONFIG_TOOL import *
from kernel.tools.tools_functions.tools_action.code_mode.functions.code_llm import code_llm_prompt
from kernel.audio.speech_to_text.record import record_audio
from kernel.audio.speech_to_text.whisper import SpeechToText
from kernel.audio.synthetic_voice.voice import LuxVoice
from kernel.tools.tools_functions.tools_action.code_mode.functions.save_to_txt import save_to_txt
from kernel.tools.tools_functions.tools_action.code_mode.functions.input_code import save_temp_code, ask_user_intent


conversation_history = []
def use_code_mode():
    global conversation_history
    whisper = SpeechToText()
    lux_voice = LuxVoice()

    # Run the 'ollama list' command and get the output
    result = subprocess.run(['ollama', 'list'], capture_output=True, text=True)
    
    # Checks if LLM_NAME is in the list of models
    if CODE_LLM in result.stdout:
        pass
    else:   
        st.error(f"Modèle {CODE_LLM} non trouvé. Installation.." if LANGUAGE == 'fr' else
                 f"Model {CODE_LLM} not found. Installation..{CODE_LLM}.")
        subprocess.run(['ollama', 'pull', CODE_LLM])

    lux_voice.speak("Activation du mode code" if LANGUAGE == 'fr' else "Activation of code mode")

    running = True
    skip_prompt = False
    while running:
        skip_prompt = False
        record_audio()
        speech_transcribe = whisper.transcribe(TEMP_AUDIO_PATH)
        user_prompt = speech_transcribe
        st.write(user_prompt + "\n")

        # Check if the user wants to enter code
        detect_code_keywords = ["je veux rentrer du code", "modification de code", "je veux mettre du code", "je veux insérer du code",
                                "I want to enter code", "I want to modify code", "I want to modify some code", "I want to put code", "I want to put some code"]
        if any(keyword in user_prompt for keyword in detect_code_keywords):
            save_temp_code(user_prompt, detect_code_keywords)
            user_intent = ask_user_intent(whisper, lux_voice)
            with open(f'{TEMP_CODE_PATH}/temp_code.txt', 'r', encoding='utf-8') as file:
                code = file.read()
            user_prompt = user_intent + "\n" + code + "\n\n" 
            response_text = code_llm_prompt(user_prompt, conversation_history)
            st.write(response_text)
            lux_voice.speak("voilà monsieur c'est fait" if LANGUAGE == 'fr' else "it's done sir")
            os.remove(f"{TEMP_CODE_PATH}/temp_code.txt")
            skip_prompt = True
            continue

        if user_prompt in ["c'est bon", "merci", "ok parfait", "tu peux arrêter", "nickel merci", "ok merci", "arrête",
                           "c'est bon tu peux arrêter", "it's okay you can stop", "it is okay you can stop", 
                           "it's okay", "thank you", "ok perfect", "you can stop", "nice thank you", "okay thank you"]:
            lux_voice.speak("Arrêt de l'outil" if LANGUAGE == 'fr' else "Stopping the tool")
            running = False
            continue

        if user_prompt in ["sauvegarde", "sauvegarde ce code", "sauvegarde le code là", "sauvegarde le code", "sauvegarde moi ça",
                           "save", "save this code", "save the code there", "save the code", "save this for me"]:
            save_to_txt(response_text)
            skip_prompt = True
            lux_voice.speak("Sauvegarde sur votre bureau effectué Monsieur" if LANGUAGE == 'fr' else 
                            "Saved in your desktop done sir")
            continue

        if user_prompt in ["sauvegarde moi tout ça", "sauvegarde tout", "sauvegarde tout le code", 
                           "sauvegarde notre conversation", "sauvegarde notre discussion", "sauvegarde-moi tout ça",
                           "save all of this", "save everything", "save all the code", 
                           "save our conversation", "save our discussion"]:
            save_to_txt(conversation_history)
            skip_prompt = True
            lux_voice.speak("Sauvegarde de toute notre discussion sur votre bureau effectué Monsieur" if LANGUAGE == 'fr' else 
                            "Saving our entire discussion in your desktop completed sir")
            continue

        if not skip_prompt:
            response_text = code_llm_prompt(user_prompt, conversation_history)
            st.write(response_text)
        else:
            skip_prompt = False