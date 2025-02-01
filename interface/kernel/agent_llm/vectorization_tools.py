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
    """
    Generates embeddings for the descriptions of the provided tools.

    Parameters:
    tools (dict): A dictionary of tools where each tool has a description.

    Returns:
    list: A list of embeddings for the tool descriptions.
    """
    tool_descriptions = [tools[tool]["description"] for tool in tools]
    embeddings = [generate_embedding(description) for description in tool_descriptions]
    return embeddings

def vectorize_tool():
    """
    Initialize Vector DB and vectorize tools on it.

    Returns:
    dict: The embeddings data from Chroma DB.
    """
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
    return embeddings_data

def revectorize_tool():
    """
    Recreate & generate new embedding from the tools list if the user check the checkbox on sidebar menu.

    Returns:
    dict: The embeddings data from Chroma DB.
    """
    embeddings_data = None 
    st.warning(f"Ajout des outils en cours..." if LANGUAGE == 'fr' else f"Adding tools in progress...")

    # Path to chroma.sqlite3 file
    chroma_db_path = os.path.join(TEMP_TOOLS_DB_PATH, 'chroma.sqlite3')

    # Close the database if it's open
    try:
        conn = sqlite3.connect(chroma_db_path)
        conn.close()
    except sqlite3.Error as e:
        st.error(f"Erreur lors de la fermeture de la base de données : {e}" if LANGUAGE == 'fr' else 
                 f"Error closing database : {e}")

    try:
        if os.path.exists(chroma_db_path):
            os.remove(chroma_db_path)
        else:
            st.error(f"Le fichier chroma.sqlite3 n'existe pas." if LANGUAGE == 'fr' else 
                     f"The chroma.sqlite3 file does not exist.")

        # Recreate folder to vectorize again with new tools
        shutil.rmtree(TEMP_TOOLS_DB_PATH)
        os.makedirs(TEMP_TOOLS_DB_PATH)
        vectorize_tool()
        
        st.success(f"Les outils ont été ajoutés à votre assistant avec succès." if LANGUAGE == 'fr' else
                   f"The tools have been successfully added to your assistant.")
    except PermissionError as e:
        st.error(f"Veuillez redémarrer l'application, revenir sur cette page et recliquer sur ce bouton pour ajouter vos outils." if LANGUAGE == 'fr' else 
                 f"Please restart the application, return to this page and click this button again to add your tools.")

    return embeddings_data