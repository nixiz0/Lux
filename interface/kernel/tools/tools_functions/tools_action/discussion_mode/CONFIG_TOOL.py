from CONFIG import LANGUAGE


DISCUSSION_BASE_LLM = "llama3.1"
DISCUSSION_MODEL_NAME = "discussion_model"
DISCUSSION_SYSTEM_INSTRUCTION_PATH = "tools/tools_functions/tools_action/discussion_mode"
DISCUSSION_LLM_MAX_HISTORY_LENGTH = 30

if LANGUAGE == 'fr':
    DISCUSSION_SYSTEM_INSTRUCTION = """Tu es un assistant serviable, gentil et conçu pour discuter et répondre aux questions de l'utilisateur.
Quand tu ne sais pas tu le dis. Quand tu n'as pas une réponse tu le dis. Tu n'inventes pas d'informations.
"""
else: 
    DISCUSSION_SYSTEM_INSTRUCTION = """You are a helpful, kind assistant designed to chat and answer user questions.
When you don't know, you say so. When you don't have an answer you say so. You don't make up information.
"""
