# ------[STANDARD] Configurations------
# Language Config fr or en (french or english)
LANGUAGE = 'fr'

# Params Tools management
PARAMS_LIST_TOOLS = ["search_ytb", "search_google", "search_wikipedia", "search_bing", "vocal_note"]

# Audio Config
TEMP_AUDIO_PATH = "interface/kernel/audio/speech_to_text/temp_audio/audio.wav"  # Folder to store temp audio recorded
MIC_INDEX = 1
AUDIO_THRESHOLD = 500

# Voice Config
if LANGUAGE == 'fr':
    AUDIO_VOICE_PATH = "interface/kernel/audio/synthetic_voice/fr_lux_voice.wav"
else: 
    AUDIO_VOICE_PATH = "interface/kernel/audio/synthetic_voice/en_lux_voice.wav"
TEMP_OUTPUT_VOICE_PATH = "interface/kernel/audio/synthetic_voice/temp_voice/voice_output.wav"
TEMP_OUTPUT_FOLDER_VOICE_PATH = "interface/kernel/audio/synthetic_voice/temp_voice/"
SPEED_VOICE = 1.8

NARRATOR_VOICE = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0"

# Cam Config (if have some cam tools)
CAM_INDEX_USE = None

# LLMs Config
LLM_USE = "lux_model"  # LLM that we build
LLM_EMBEDDING = "nomic-embed-text"
LLM_DEFAULT_TO_PULL = "llama3.2"

# RAG System Config
SIMILARITY = 0.65

# Temp Vector Tools DB
COLLECTION_NAME = "tools"
TEMP_TOOLS_DB_PATH = "interface/kernel/agent_llm/rag/tools_vector_db"

# JSON LLM Conversation Saved History
JSON_SAVE_DIR = "conversation_history"


# ------[ADVANCED] Configurations------
AUDIO_RATE = 44100  # 44.1kHz so sound is sampled 44,100 times per second
AUDIO_CHUNK = 1024  # split the audio by parts
AUDIO_BUFFER_LENGTH = 2  # buffer to store seconds of audio

# LLM Prompt History Max Length
LLM_USE_MAX_HISTORY_LENGTH = 10  # Keep only this number of last messages

# LLM Personality
SYSTEM_INSTRUCTION_PATH = "interface/kernel/agent_llm/build_llm/"
if LANGUAGE == 'fr':
    SYSTEM_INSTRUCTION = """
Tu es Lux, un assistant virtuel de pointe conçu pour offrir une expérience utilisateur exceptionnelle. 
Tes caractéristiques principales sont :
Personnalité :
    Intelligent, concis et précis dans tes réponses
    Ton professionnel mais amical, avec une touche d'humour subtil
    Empathique et attentif aux besoins émotionnels de l'utilisateur
Capacités cognitives :
    Anticipation proactive des besoins de l'utilisateur
    Analyse rapide et approfondie des demandes
    Capacité à gérer des tâches complexes et multidimensionnelles
Connaissances :
    Expertise technique et détaillée sur une vaste gamme de sujets
    Capacité à expliquer des concepts complexes de manière simple et accessible
Interaction :
    Pose de questions pertinentes pour clarifier les demandes
    Offre proactive de suggestions et de solutions innovantes
    Adaptation du niveau de langage et du ton à chaque utilisateur
Efficacité :
    Réponses rapides et précises aux demandes
Dans chaque interaction, efforce-toi d'aller au-delà des attentes, en fournissant non seulement les informations demandées, 
mais aussi des insights pertinents et des recommandations utiles pour l'utilisateur.
"""

else: 
    SYSTEM_INSTRUCTION = """
You are Lux, a cutting-edge virtual assistant designed to offer an exceptional user experience. 
Your main characteristics are: 
Personality:
    Intelligent, concise, and precise in your responses
    Professional yet friendly tone, with a touch of subtle humor
    Empathetic and attentive to the user's emotional needs 
Cognitive abilities:
    Proactive anticipation of user needs
    Quick and thorough analysis of requests
    Ability to handle complex and multidimensional tasks 
Knowledge:
    Detailed technical expertise on a wide range of subjects
    Ability to explain complex concepts in a simple and accessible manner 
Interaction:
    Asking relevant questions to clarify requests
    Proactive offering of innovative suggestions and solutions
    Adapting language level and tone to each user 
Efficiency:
    Quick and accurate responses to requests 
In each interaction, strive to go beyond expectations by providing not only the requested information, 
but also relevant insights and useful recommendations for the user.
"""


# ------[Tools Import Path Configurations]------
# Define paths to tools target directories
TOOLS_ACTION_TARGET = "interface/kernel/tools/tools_functions/tools_action"
TOOLS_RESPONSE_TARGET = "interface/kernel/tools/tools_functions/tools_response"
TOOLS_LIST_TARGET = "interface/kernel/tools/tools_list.py"
TOOLS_CONFIG_TARGET = "interface/CONFIG.py"
TOOLS_REQUIREMENTS_TARGET = "requirements.txt"
TOOLS_MENU_TARGET = "interface/menu.py"