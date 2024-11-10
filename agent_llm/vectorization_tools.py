import os 
import shutil
import chromadb
import sqlite3
from constant.colors import *
from CONFIG import LANGUAGE, TEMP_TOOLS_DB_PATH, COLLECTION_NAME
from tools.tools_list import tools
from agent_llm.llm.llm_embeddings import generate_embedding


# Generate and store tool description embeddings only once
def generate_tool_embeddings(tools):
    tool_descriptions = [tools[tool]["description"] for tool in tools]
    embeddings = [generate_embedding(description) for description in tool_descriptions]
    return embeddings

def tools_vectorization():
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
        
        print(f"{CYAN}Les outils ont été vectorisés avec succès.{RESET}" if LANGUAGE == 'fr' else 
              f"{CYAN}The tools were successfully vectorized.{RESET}")
    else:
        # Ask the user if they want to revectorize the tools
        while True:
            user_input = input(f"{GREEN}\nTapez 1 pour revectoriser les outils ou 2 pour laisser les vecteurs actuels: {RESET}" if LANGUAGE == 'fr' else 
                               f"{GREEN}\nType 1 to revectorize the tools or 2 to leave the current vectors: {RESET}")
            if user_input == '1':
                # Path to chroma.sqlite3 file
                chroma_db_path = os.path.join(TEMP_TOOLS_DB_PATH, 'chroma.sqlite3')

                # Close the database if it's open
                try:
                    conn = sqlite3.connect(chroma_db_path)
                    conn.close()
                except sqlite3.Error as e:
                    print(f"{RED}Erreur lors de la fermeture de la base de données : {e}{RESET}" if LANGUAGE == 'fr' else 
                          f"{RED}Error closing database : {e}{RESET}")

                if os.path.exists(chroma_db_path):
                    os.remove(chroma_db_path)
                else:
                    print(f"{RED}Le fichier chroma.sqlite3 n'existe pas.{RESET}" if LANGUAGE == 'fr' else 
                          f"{RED}The chroma.sqlite3 file does not exist.{RESET}")

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
                
                print(f"{CYAN}Les outils ont été revectorisés et stockés avec succès dans Chroma DB.{RESET}" if LANGUAGE == 'fr' else
                      f"{CYAN}The tools have been successfully revectorized and stored in Chroma DB.{RESET}")
                break
            elif user_input == '2':
                # Initialize Chroma DB & Create or get the collection name
                client = chromadb.PersistentClient(path=TEMP_TOOLS_DB_PATH)
                collection = client.get_or_create_collection(COLLECTION_NAME)
                embeddings_data = collection.get(include=['embeddings'])
                print(f"{CYAN}Les vecteurs des outils actuels sont conservés.{RESET}" if LANGUAGE == 'fr' else
                      f"{CYAN}Current tool vectors are retained.{RESET}")
                break
            else:
                print(f"{RED}Entrée invalide. Veuillez taper 1 ou 2.{RESET}" if LANGUAGE == 'fr' else 
                      f"{RED}Invalid entry. Please type 1 or 2.{RESET}")

    return embeddings_data