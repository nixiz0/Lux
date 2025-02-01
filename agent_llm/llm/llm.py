import ollama 
import re
from CONFIG import *


def llm_prompt(prompt, conversation_history):
    # Add current prompt to history
    conversation_history.append(f"User: {prompt}")

    # Limit history size
    if len(conversation_history) > LLM_USE_MAX_HISTORY_LENGTH:
        conversation_history.pop(0)

    # Create the complete prompt including the history
    full_prompt = "\n".join(conversation_history)

    # Choose the LLM Server API you want:
    """ Local Ollama (on your computer) """
    client = ollama.Client()  

    """ API Ollama (on server) """
    # client = ollama.Client(host="http://172.17.0.1:11434/")

    response = client.generate(
        model=LLM_USE,  # Local Model
        # model="llama3.1",  # Online API Model
        prompt=full_prompt
    )
    response_text = response['response']
    
    # Clean generated response
    cleaned_response = re.sub(r'[<>*_]', '', response_text)
    
    # Add model response to history
    conversation_history.append(f"Assistant: {cleaned_response}")
    
    return cleaned_response