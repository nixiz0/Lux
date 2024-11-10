import time
import sys
import chromadb
import subprocess
from CONFIG import * 
from agent_llm.build_llm.auto_build_llm import build_the_model
from agent_llm.build_llm.llm_reset import choose_llm_reset
from audio.select_language import select_lang
from audio.select_microphone import select_microphone
from audio.micro_sensitivity import mic_record_threshold
from agent_llm.vectorization_tools import tools_vectorization
from audio.speech_to_text.record import record_audio
from audio.speech_to_text.whisper import SpeechToText
from audio.synthetic_voice.voice import LuxVoice
from tools.select_tool import analyze_tool_to_use
from tools.tools_list import tools


# Auto install & build Lux personality
build_the_model()

# Ask the user to press a key
user_input = input("Press Enter to continue or another key to configure: ")
tools = tools

# If user doesn't press Enter execute configurations functions
if user_input != "":
    select_lang()
    select_microphone()
    mic_record_threshold()
    tool_embeddings = tools_vectorization()
    choose_llm_reset()
    subprocess.run([sys.executable, 'main.py'])  # Restart the application only after configuration
    sys.exit()  # Ensure the script exits after restarting
else: 
    try:
        # Connect to the client & Get collection
        client = chromadb.PersistentClient(path=TEMP_TOOLS_DB_PATH)
        collection = client.get_collection(COLLECTION_NAME)
        tool_embeddings = collection.get(include=['embeddings'])
    except chromadb.CollectionNotFoundError:
        # If the collection does not exist, use tools_vectorization
        tool_embeddings = tools_vectorization()

whisper = SpeechToText()
lux_voice = LuxVoice()

paused = False
pause_keyword = ["Système mis en pause", "System paused"]

running = True
while running:
    record_audio()
    speech_transcribe = whisper.transcribe(TEMP_AUDIO_PATH)
    prompt = speech_transcribe
    print(prompt)

    response = analyze_tool_to_use(prompt, tools, tool_embeddings)

    if response in pause_keyword:
        lux_voice.speak("Le système a été mis en pause monsieur" if LANGUAGE == 'fr' else "The system has been paused sir")
        paused = True
        while paused:
            record_audio()
            speech_transcribe = whisper.transcribe(TEMP_AUDIO_PATH)
            prompt = speech_transcribe
            print(prompt)

            if prompt in ["arrête le mode pause", "arrête la pause", "reprend le système", "tu peux reprendre", 
                          "stop pause mode", "stop pause", "restarting the system", "you can unpause", "unpaused"]:
                paused = False
                lux_voice.speak("Le système reprend de ses fonctions, ça fait du bien d'être de retour monsieur" if LANGUAGE == 'fr' else 
                                "The system is resuming its functions, it's good to be back sir")
                break

    if response != "stop system" and response not in pause_keyword:
        lux_voice.speak(response)
        print(response)

    if response == "stop system":
        lux_voice.speak("Au revoir Monsieur. A bientot" if LANGUAGE == 'fr' else "By Sir. See you soon")
        time.sleep(4)
        break
