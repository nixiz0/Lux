import streamlit as st
import subprocess
import os
from CONFIG import LANGUAGE, LLM_USE, LLM_DEFAULT_TO_PULL, LLM_EMBEDDING
from kernel.agent_llm.build_llm.auto_build_llm import build_the_model


def set_build_model():
    # Run the 'ollama list' command and get the output
    result = subprocess.run(['ollama', 'list'], capture_output=True, text=True)
    
    # Checks if LLM_NAME is in the list of models
    if LLM_USE not in result.stdout:
        st.sidebar.error(f"Modèle {LLM_USE} non trouvé. Initialisation des installations des LLMS utilisés par l'Assistant." if LANGUAGE == 'fr' else
                         f"Model {LLM_USE} not found. Initialization of the installations of LLMS used by the Assistant. {LLM_DEFAULT_TO_PULL}.")
        subprocess.run(['ollama', 'pull', LLM_DEFAULT_TO_PULL])
        subprocess.run(['ollama', 'pull', LLM_EMBEDDING])

        st.sidebar.warning("Construction du modèle en cours" if LANGUAGE == 'fr' else "Building the model in progress")
        build_the_model()
    else: 
        col1, col2, _ = st.sidebar.columns([1, 1, 2.2])
        with col1:
            if st.button("Oui" if LANGUAGE == 'fr' else "Yes", key="btn_yes_build_model"):
                os.system(f"ollama rm {LLM_USE}")
                st.sidebar.warning("Construction du modèle en cours" if LANGUAGE == 'fr' else "Building the model in progress")
                build_the_model()
        with col2:
            if st.button("Non" if LANGUAGE == 'fr' else "No", key="btn_no_build_model"):
                st.sidebar.success("Modèle conservé" if LANGUAGE == 'fr' else "Model kept")
                pass