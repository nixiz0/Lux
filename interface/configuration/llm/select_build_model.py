import streamlit as st
import subprocess
from CONFIG import LANGUAGE, LLM_USE, LLM_DEFAULT_TO_PULL, LLM_EMBEDDING
from kernel.agent_llm.build_llm.auto_build_llm import build_the_model


def set_build_model():
    """
    Checks if the specified language model (LLM) is available. If not, it initializes the installation of the required LLMs.
    Provides options to rebuild the model if it already exists.

    The function runs the 'ollama list' command to check for the presence of the LLM. If the LLM is not found, it pulls the necessary models.
    If the LLM is found, it provides options to either rebuild or keep the current model.
    """
    # Run the 'ollama list' command and get the output
    result = subprocess.run(['ollama', 'list'], capture_output=True, text=True)
    
    # Checks if LLM_NAME is in the list of models
    if LLM_USE not in result.stdout:
        st.sidebar.error(f"Modèle {LLM_USE} non trouvé. Construction automatique de l'Assistant Lux." if LANGUAGE == 'fr' else
                         f"Model {LLM_USE} not found. Automatic build of the Lux Assistant.")
        subprocess.run(['ollama', 'pull', LLM_DEFAULT_TO_PULL])
        subprocess.run(['ollama', 'pull', LLM_EMBEDDING])

        st.sidebar.warning("Construction du modèle en cours" if LANGUAGE == 'fr' else "Building the model in progress")
        build_the_model()