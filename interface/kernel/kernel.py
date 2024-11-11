import streamlit as st
import chromadb
import time
from CONFIG import * 
from kernel.audio.speech_to_text.record import record_audio
from kernel.audio.speech_to_text.whisper import SpeechToText
from kernel.audio.synthetic_voice.voice import LuxVoice
from kernel.tools.select_tool import analyze_tool_to_use
from kernel.tools.tools_list import tools


def start_lux(tools=tools):
    """
    Starts the Lux system, which involves connecting to a client, retrieving tool embeddings,
    and processing voice commands to determine the appropriate tool to use.

    Parameters:
    tools (list): A list of tools available for use in the system.

    The function initializes the necessary components, listens for voice commands, and processes
    them to determine the appropriate response. It handles pausing and resuming the system based
    on specific keywords and stops the system when instructed.
    """
    
    # Connect to the client & Get collection
    client = chromadb.PersistentClient(path=TEMP_TOOLS_DB_PATH)
    collection = client.get_collection(COLLECTION_NAME)
    tool_embeddings = collection.get(include=['embeddings'])

    whisper = SpeechToText()
    lux_voice = LuxVoice()

    paused = False
    pause_keyword = ["Système mis en pause", "System paused"]

    running = True
    while running:
        record_audio()
        speech_transcribe = whisper.transcribe(TEMP_AUDIO_PATH)
        prompt = speech_transcribe
        st.write(prompt)

        response = analyze_tool_to_use(prompt, tools, tool_embeddings)

        if response in pause_keyword:
            lux_voice.speak("Le système a été mis en pause monsieur" if LANGUAGE == 'fr' else "The system has been paused sir")
            paused = True
            while paused:
                record_audio()
                speech_transcribe = whisper.transcribe(TEMP_AUDIO_PATH)
                prompt = speech_transcribe
                st.write(prompt)

                if prompt in ["arrête le mode pause", "arrête la pause", "reprend le système", "tu peux reprendre", 
                            "stop pause mode", "stop pause", "restarting the system", "you can unpause", "unpaused"]:
                    paused = False
                    lux_voice.speak("Le système reprend de ses fonctions, ça fait du bien d'être de retour monsieur" if LANGUAGE == 'fr' else 
                                    "The system is resuming its functions, it's good to be back sir")
                    break

        if response != "stop system" and response not in pause_keyword:
            lux_voice.speak(response)
            st.write(response)

        if response == "stop system":
            lux_voice.speak("Au revoir Monsieur. A bientot" if LANGUAGE == 'fr' else "By Sir. See you soon")
            time.sleep(4)
            break
