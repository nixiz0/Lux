import streamlit as st
from CONFIG import LANGUAGE, SIMILARITY
from configuration.update_config import update_config


def set_similarity():
    """
    Configures the similarity for the application.
    """
    similarity = st.number_input("Configurer votre similarité (par défaut 0.65)" if LANGUAGE == 'fr' else
                                 "Configure your similarity (default 0.65)", min_value=0.1, value=SIMILARITY)
    if st.button("Mettre à jour" if LANGUAGE == 'fr' else "Update", key='btn_set_similarity'):
        update_config('SIMILARITY', similarity)
        st.success(f"Similarité mise à jour en {similarity}" if LANGUAGE == 'fr' else 
                   f"Similarity updated in {similarity}")