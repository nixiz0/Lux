import streamlit as st
from CONFIG import LANGUAGE, LLM_USE_MAX_HISTORY_LENGTH
from configuration.update_config import update_config


def set_llm_history_length():
    llm_history_length = st.number_input("Configurer votre longueur de conversation pour le LLM (par défaut 10)" if LANGUAGE == 'fr' else
                                         "Configure your conversation length for the LLM (default 10)", min_value=1, value=LLM_USE_MAX_HISTORY_LENGTH)
    if st.button("Mettre à jour" if LANGUAGE == 'fr' else "Update", key='btn_set_llm_history_length'):
        update_config('LLM_USE_MAX_HISTORY_LENGTH', llm_history_length)
        st.success(f"Longueur de conversation pour le LLM  mise à jour en {llm_history_length}" if LANGUAGE == 'fr' else 
                   f"Conversation length for the LLM updated in {llm_history_length}")