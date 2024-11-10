import streamlit as st
import os 
import shutil
import chromadb
import sqlite3
from CONFIG import LANGUAGE, TEMP_TOOLS_DB_PATH, COLLECTION_NAME
from kernel.tools.tools_list import tools
from kernel.agent_llm.llm.llm_embeddings import generate_embedding


# Generate and store tool description embeddings only once
def generate_tool_embeddings(tools):
    tool_descriptions = [tools[tool]["description"] for tool in tools]
    embeddings = [generate_embedding(description) for description in tool_descriptions]
    return embeddings

def tools_vectorization():
    embeddings_data = None 
    
    # Check if the folder exists, if not create it and vectorize tools
    if not os.path.exists(TEMP_TOOLS_DB_PATH):
        os.makedirs(TEMP_TOOLS_DB_PATH)

        # Initialize Chroma DB
        client = chromadb.PersistentClient(path=TEMP_TOOLS_DB_PATH)

        # Create or get the collection name
        collection = client.get_or_create_collection(COLLECTION_NAME)

        # Generate embeddings
        tool_embeddings = generate_tool_embeddings(tools)
        
        # Store embeddings in Chroma DB
        for tool_name, embedding in zip(tools.keys(), tool_embeddings):
            collection.add(ids=[tool_name], documents=[tool_name], embeddings=[embedding])

        embeddings_data = collection.get(include=['embeddings'])
        
        st.sidebar.success(f"Les outils ont été vectorisés avec succès." if LANGUAGE == 'fr' else 
                           f"The tools were successfully vectorized.")
    else:
        st.sidebar.write(f"Revectoriser les outils ou laisser les vecteurs actuels:" if LANGUAGE == 'fr' else 
                         f"Revectorize the tools or leave the current vectors:")

        col1, col2, _ = st.sidebar.columns([1, 1, 2.2])
        with col1:
            if st.button("Oui" if LANGUAGE == 'fr' else "Yes", key="btn_yes_vectorize_tool"):
                st.sidebar.warning(f"Vectorisation des outils en cours..." if LANGUAGE == 'fr' else f"Vectorizing tools...")

                # Path to chroma.sqlite3 file
                chroma_db_path = os.path.join(TEMP_TOOLS_DB_PATH, 'chroma.sqlite3')

                # Close the database if it's open
                try:
                    conn = sqlite3.connect(chroma_db_path)
                    conn.close()
                except sqlite3.Error as e:
                    st.sidebar.error(f"Erreur lors de la fermeture de la base de données : {e}" if LANGUAGE == 'fr' else 
                                     f"Error closing database : {e}")

                try:
                    if os.path.exists(chroma_db_path):
                        os.remove(chroma_db_path)
                    else:
                        st.sidebar.error(f"Le fichier chroma.sqlite3 n'existe pas." if LANGUAGE == 'fr' else 
                                         f"The chroma.sqlite3 file does not exist.")

                    # Recreate folder to vectorize again with new tools
                    shutil.rmtree(TEMP_TOOLS_DB_PATH)
                    os.makedirs(TEMP_TOOLS_DB_PATH)

                    # Initialize Chroma DB & Create or get the collection name
                    client = chromadb.PersistentClient(path=TEMP_TOOLS_DB_PATH)
                    collection = client.get_or_create_collection(COLLECTION_NAME)

                    # Generate embeddings
                    tool_embeddings = generate_tool_embeddings(tools)

                    # Store embeddings in Chroma DB
                    for tool_name, embedding in zip(tools.keys(), tool_embeddings):
                        collection.add(ids=[tool_name], documents=[tool_name], embeddings=[embedding])
                    
                    embeddings_data = collection.get(include=['embeddings'])
                    
                    st.sidebar.success(f"Les outils ont été revectorisés et stockés avec succès dans Chroma DB." if LANGUAGE == 'fr' else
                                       f"The tools have been successfully revectorized and stored in Chroma DB.")
                except PermissionError as e:
                    st.sidebar.error(f"Veuillez redémarrer l'application pour revectoriser les outils." if LANGUAGE == 'fr' else 
                                     f"Please restart the application to revectorize the tools.")
        with col2:
            if st.button("Non" if LANGUAGE == 'fr' else "No", key="btn_no_vectorize_tool"):
                st.sidebar.write(f"Les vecteurs actuels sont conservés." if LANGUAGE == 'fr' else f"Current vectors are kept.")

                # Initialize Chroma DB & Create or get the collection name
                client = chromadb.PersistentClient(path=TEMP_TOOLS_DB_PATH)
                collection = client.get_or_create_collection(COLLECTION_NAME)
                embeddings_data = collection.get(include=['embeddings'])
                st.sidebar.success(f"Les vecteurs des outils actuels sont conservés." if LANGUAGE == 'fr' else
                                   f"Current tool vectors are retained.")

    return embeddings_data