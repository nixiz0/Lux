import requests
from CONFIG import *


def generate_embedding(text):
    # Choose the LLM Embedding Server API you want:
    """ Local Ollama (on your computer) """
    url = "http://localhost:11434/api/embeddings"

    """ API Ollama (on server) """
    # url = "http://172.17.0.1:11434/api/embeddings"

    payload = {
        "model": LLM_EMBEDDING,  # Local Model
        # "model": "nomic-embed-text",  # API Model
        "prompt": text
    }
    response = requests.post(url, json=payload)
    
    # Check if the response is not empty
    if response.text:
        try:
            data = response.json()
            embeddings = data['embedding']
        except ValueError as e:
            print(f"Erreur de décodage JSON: {e}" if LANGUAGE == 'fr' else f"JSON decoding error: {e}")
            embeddings = None
            pass
    else:
        print("La réponse est vide." if LANGUAGE == 'fr' else "The answer is empty.")
        embeddings = None

    return embeddings