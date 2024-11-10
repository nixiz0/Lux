import ollama
from kernel.tools.tools_functions.tools_action.discussion_mode.CONFIG_TOOL import *


def discussion_llm_prompt(prompt, conversation_history):
    # Add current prompt to history
    conversation_history.append(f"User: {prompt}")

    # Limit history size
    if len(conversation_history) > DISCUSSION_LLM_MAX_HISTORY_LENGTH:
        conversation_history.pop(0)

    # Create the complete prompt including the history
    full_prompt = "\n".join(conversation_history)

    # Choose the LLM Server API you want:
    """ Local Ollama (on your computer) """
    client = ollama.Client()  

    """ API Ollama (on server) """
    # client = ollama.Client(host="http://172.17.0.1:11434/")

    response = client.generate(
        model=DISCUSSION_MODEL_NAME,  # Local Model
        # model=DISCUSSION_MODEL_NAME,  # Online API Model
        prompt=full_prompt
    )
    response_text = response['response']
    
    # Add model response to history
    conversation_history.append(f"Assistant: {response_text}")
    
    return response_text