import ollama 
import re
from CONFIG import *


def llm_prompt(prompt, conversation_history):
    # Add current prompt to history
    conversation_history.append({"role": "user", "content": prompt})

    # Limit history size
    if len(conversation_history) > LLM_USE_MAX_HISTORY_LENGTH:
        conversation_history.pop(0)

    # Choose the LLM Server API you want:
    """ Local Ollama (on your computer) """
    client = ollama.Client()  

    """ API Ollama (on server) """
    # client = ollama.Client(host="http://172.17.0.1:11434")

    response = client.chat(
        model=LLM_USE,  # Local Model
        # model="llama3.1",  # Online API Model
        messages=conversation_history
    )
    response_text = response.message.content
    
    # Clean generated response
    cleaned_response = re.sub(r'[<>*_]', '', response_text)
    
    # Add model response to history
    conversation_history.append({"role": "assistant", "content": cleaned_response})
    
    return cleaned_response