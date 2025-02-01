import requests
import subprocess
from CONFIG import *


def generate_embedding(text):
    # Check if LLM_EMBEDDING model is present
    try:
        subprocess.run(["ollama", "list"], check=True, capture_output=True)
        models_list = subprocess.run(["ollama", "list"], capture_output=True, text=True).stdout
        if LLM_EMBEDDING not in models_list:
            if LANGUAGE == 'fr':
                print(f"Le modèle {LLM_EMBEDDING} n'est pas présent. Téléchargement en cours...")
            else: 
                print(f"The {LLM_EMBEDDING} model is not present. Download in progress...")
            subprocess.run(["ollama", "pull", LLM_EMBEDDING], check=True)
    except subprocess.CalledProcessError as e:
        if LANGUAGE == 'fr':
            print(f"Erreur lors de la vérification du modèle: {e}")
        else: 
            print(f"Error checking model: {e}")
        return None

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
