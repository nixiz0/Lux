import streamlit as st
import os
import json
from CONFIG import LANGUAGE, JSON_SAVE_DIR
from configuration._ui_custom.page_title import set_page_title
from configuration._ui_custom.custom_ui import custom_ui
from kernel.start_kernel import start_lux


set_page_title("Lux-Assistant")
custom_ui()

if st.sidebar.checkbox("🤖​Démarrer Lux" if LANGUAGE == 'fr' else "🤖​Start Lux", key='start_lux'):
    start_lux()

st.sidebar.markdown("<hr style='margin:0px;'>", unsafe_allow_html=True)

def load_conversation(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def list_conversations(directory=JSON_SAVE_DIR):
    if not os.path.exists(directory):
        return []
    return [''] + [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def rename_conversation(old_path, new_name):
    directory, _ = os.path.split(old_path)
    new_path = os.path.join(directory, new_name + '.json')
    os.rename(old_path, new_path)

def delete_conversation(file_path):
    os.remove(file_path)

def download_conversation(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        conversation = json.load(file)
    csv_content = ""
    for message in conversation:
        csv_content += f"{message['role']}: {message['content']}\n"
    st.sidebar.download_button(
        label="Télécharger CSV" if LANGUAGE == 'fr' else "Download CSV",
        data=csv_content,
        file_name=os.path.basename(file_path).replace('.json', '.csv'),
        mime='text/csv'
    )

# Streamlit UI
conversations = list_conversations()
selected_conversation = st.sidebar.selectbox('Sélectionnez une conversation' if LANGUAGE == 'fr' else 
                                             'Select a conversation', conversations, key='selected_conversation')

if selected_conversation:
    conversation_path = os.path.join(JSON_SAVE_DIR, selected_conversation)
    
    # Clear session state if a new conversation is selected
    if 'session_state' not in st.session_state or st.session_state.selected_conversation_path != conversation_path:
        st.session_state.session_state = []
        st.session_state.selected_conversation_path = conversation_path

        conversation = load_conversation(conversation_path)

        # Adapt the data format to store roles and content in session state
        for message in conversation:
            st.session_state.session_state.append({"role": message["role"], "content": message["content"]})
    
    # Display the chat history on Streamlit
    for message in st.session_state.session_state:
        with st.chat_message(message['role']):
            st.write(message['content'])
    
    if st.sidebar.button('Renommer' if LANGUAGE == 'fr' else "Rename"):
        new_name = st.sidebar.text_input('Nouveau nom' if LANGUAGE == 'fr' else 'New name')
        if new_name:
            rename_conversation(conversation_path, new_name)
            st.rerun()

    if st.sidebar.button('Supprimer' if LANGUAGE == 'fr' else 'Delete'):
        delete_conversation(conversation_path)
        st.rerun()

    download_conversation(conversation_path)
