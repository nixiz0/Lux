import ollama 
from CONFIG import *


def generate_llm_response(prompt, context):
    # Template for the prompt
    if LANGUAGE == 'fr':
        prompt_template = f"""Répondez à la question en français en vous basant uniquement sur le contexte suivant:
        Contexte: {context}
        Question: {prompt}
        """
    else:
        prompt_template = f"""Answer to the question in english based only on the following context:
        Context: {context}
        Question: {prompt}
        """

    # Choose the LLM Server API you want:
    """ Local Ollama (on your computer) """
    client = ollama.Client()  

    """ API Ollama (on server) """
    # client = ollama.Client(host="http://172.17.0.1:11434/")

    response = client.generate(
        model=LLM_USE,  # Local Model
        # model="llama3.1",  # API Model
        prompt=prompt_template
    )

    text_content = response['response']
    return text_content