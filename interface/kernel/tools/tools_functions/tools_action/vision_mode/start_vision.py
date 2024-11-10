import streamlit as st
import requests 
import base64 
import json 
import subprocess
from CONFIG import LANGUAGE, TEMP_AUDIO_PATH
from kernel.tools.tools_functions.tools_action.vision_mode.CONFIG_TOOL import LLM_VISION_MODEL
from kernel.audio.speech_to_text.record import record_audio
from kernel.audio.speech_to_text.whisper import SpeechToText
from kernel.audio.synthetic_voice.voice import LuxVoice
from kernel.tools.tools_functions.tools_action.screenshot import screen
from kernel.tools.tools_functions.tools_action.cam.screen_cam import screen_with_cam


def start_llm_vision():
    url = "http://localhost:11434/api/generate"
    headers = {'Content-Type': "application/json",}
    vision_history = []
    whisper = SpeechToText()
    lux_voice = LuxVoice()
    running = True

    # Run the 'ollama list' command and get the output
    result = subprocess.run(['ollama', 'list'], capture_output=True, text=True)
    
    # Checks if LLM_NAME is in the list of models
    if LLM_VISION_MODEL in result.stdout:
        pass
    else:
        st.error(f"Modèle {LLM_VISION_MODEL} non trouvé. Installation.." if LANGUAGE == 'fr' else
                 f"Model {LLM_VISION_MODEL} not found. Installation..{LLM_VISION_MODEL}.")
        subprocess.run(['ollama', 'pull', LLM_VISION_MODEL])

    def encode_image_to_base64(image_path):
        with open(image_path, 'rb') as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def analyze_image(image_path, custom_prompt):
        vision_history.append(custom_prompt)
        image_base64 = encode_image_to_base64(image_path)
        
        payload = {
            "model": LLM_VISION_MODEL,
            "prompt": custom_prompt,
            "images": [image_base64]
        }
        
        response = requests.post(url, headers=headers, json=payload)
        try: 
            response_lines = response.text.strip().split('\n')
            full_response = ''.join(json.loads(line)['response'] for line in response_lines if 'response' in json.loads(line))
            
            # Read response to user
            lux_voice.speak(full_response)
            
            return full_response
        except Exception as e: 
            return f"Error: {e}"

    lux_voice.speak("D'accord, j'active le mode vision monsieur" if LANGUAGE == 'fr' else "Okay, I activate vision mode sir")

    while running:
        st.success(f"Mode vision.." if LANGUAGE == 'fr' else f"Vision mode..")
        record_audio()
        speech_transcribe = whisper.transcribe(TEMP_AUDIO_PATH)
        user_prompt = speech_transcribe
        st.write(user_prompt)
        
        # Check if the user wants to stop the LLM Vision for return to basic voice detection
        detect_stop_llm_keyords = ["désactive llm", "désactive vision", "désactive le llm", "désactive la vision",
                                   "désactive le mode vision", "arrête l'outil", "arrêt", "arrête", 
                                   "disable llm", "switch to classic mode", "switch classic mode"]
        if any(keyword in user_prompt for keyword in detect_stop_llm_keyords):
            if LANGUAGE == 'fr':
                lux_voice.speak("Arrêt du mode vision")
            else: 
                lux_voice.speak("Stopping the vision mode")
            st.success(f"Arrêt du mode vision." if LANGUAGE == 'fr' else f"Stopping the vision mode.")
            running = False
            continue

        # Check if the user wants to do screenshot
        screenshot_keywords = ["prends un screen", "prends une capture d'écran", "capture d'écran",
                               "prend un screen", "prend une capture d'écran",
                               "take a screen", "take a screenshot", "screenshot"]
        if any(keyword in user_prompt for keyword in screenshot_keywords ):
            screen()
            image_path = "photos/screenshot.png"
            if LANGUAGE == 'fr':
                lux_voice.speak("Dites moi ce que je dois faire avec cette image ?")
                lang_preprompt = "Parle en Français et réponds en français, "
            else:
                lux_voice.speak("Tell me what I should do with this image ?")
                lang_preprompt = "Speak in English and respond in English, "

            record_audio()
            speech_transcribe = whisper.transcribe(TEMP_AUDIO_PATH)
            user_prompt = speech_transcribe
            full_prompt = lang_preprompt + user_prompt
            st.write(full_prompt)
            analyze_image(image_path, full_prompt)
            
        # Check if the user wants to screen with the cam
        screen_cam_keywords = ["screen avec la caméra", "screen avec la cam", "screen cam", "screencam",         
                               "screen with camera", "cam screen"]
        if any(keyword in user_prompt for keyword in screen_cam_keywords ):
            screen_with_cam()
            image_path = "photos/camera.png"
            if LANGUAGE == 'fr':
                lux_voice.speak("Dites moi ce que je dois faire avec cette image ?")
                lang_preprompt = "Parle en Français et réponds en français, "
            else:
                lux_voice.speak("Tell me what I should do with this image ?")
                lang_preprompt = "Speak in English and respond in English, "

            record_audio()
            speech_transcribe = whisper.transcribe(TEMP_AUDIO_PATH)
            user_prompt = speech_transcribe
            full_prompt = lang_preprompt + user_prompt
            st.write(full_prompt)
            analyze_image(image_path, full_prompt)
