import streamlit as st
import os 
import shutil
from CONFIG import LANGUAGE, AUDIO_VOICE_PATH


def manage_voice():
    st.title("Changer la voix synthétique" if LANGUAGE == 'fr' else "Change the synthetic voice")

    uploaded_file = st.file_uploader("Choisissez un fichier .wav" if LANGUAGE == 'fr' else "Choose a .wav file", type=["wav"])
    
    if uploaded_file is not None:
        # Ensure the temp_dir directory exists
        if not os.path.exists("temp_dir"):
            os.makedirs("temp_dir")
        
        # Save the uploaded file in the temp_dir directory
        temp_file_path = os.path.join("temp_dir", uploaded_file.name)
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Replace the old file with the new one
        shutil.move(temp_file_path, AUDIO_VOICE_PATH)
        
        # Remove the temp_dir directory
        shutil.rmtree("temp_dir")
        
        st.success("La voix synthétique a été changée !" if LANGUAGE == 'fr' else "The synthetic voice has been changed!")