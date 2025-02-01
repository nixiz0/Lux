import ollama 
from CONFIG import *


def generate_llm_response(prompt, context):
    # Template for the prompt
    if LANGUAGE == 'fr':
        system_message = "Vous êtes un assistant IA qui répond aux questions en français en se basant uniquement sur le contexte fourni."
        user_message = f"Contexte: {context}\nQuestion: {prompt}"
    else:
        system_message = "You are an AI assistant that answers questions in English based only on the provided context."
        user_message = f"Context: {context}\nQuestion: {prompt}"

    # Choose the LLM Server API you want:
    """ Local Ollama (on your computer) """
    client = ollama.Client()  

    """ API Ollama (on server) """
    # client = ollama.Client(host="http://172.17.0.1:11434")

    response = client.chat(
        model=LLM_USE,  # Local Model
        # model="llama3.1",  # API Model
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ]
    )

    text_content = response.message.content
    return text_content