import streamlit as st
import subprocess
import os
import re
from CONFIG import *


def build_the_model():
    """
    Builds a language model by running the 'ollama show' command, modifying the output,
    and then creating the model using the 'ollama create' command.

    The function performs the following steps:
    1. Runs the 'ollama show' command to get the model file.
    2. Writes the output to a file named 'modelfile'.
    3. Modifies the content of the 'modelfile' to replace the SYSTEM instruction and remove the LICENSE section.
    4. Executes the 'ollama create' command to create the model.
    """
    # Run the 'ollama show' command and get the output
    show_result = subprocess.run(['ollama', 'show', LLM_DEFAULT_TO_PULL, '--modelfile'], shell=True, capture_output=True, text=True, encoding='utf-8')

    # Create a file named 'modelfile' and write the output of 'ollama show' to it
    modelfile_path = os.path.join(SYSTEM_INSTRUCTION_PATH, 'modelfile')
    
    if show_result.returncode == 0 and show_result.stdout:
        with open(modelfile_path, 'w', encoding='utf-8') as file:
            file.write(show_result.stdout)
    else:
        st.sidebar.error(f"La commande 'ollama show' n'a produit aucune sortie ou a échoué." if LANGUAGE == 'fr' else 
                         f"The 'ollama show' command produced no output or failed.")
        return
    
    # Get the content from the line below the first 'FROM'
    with open(modelfile_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    from_index = content.find('FROM')
    if from_index != -1:
        content = content[from_index:]
        next_line_index = content.find('\n') + 1
        content = content[next_line_index:]
    
    # Replaces the content between SYSTEM " " with SYSTEM_INSTRUCTION
    content = re.sub(r'SYSTEM ".*?"', f'SYSTEM "{SYSTEM_INSTRUCTION}"', content, flags=re.DOTALL)
    
    # Remove the LICENSE section and everything after it
    content = re.sub(r'LICENSE.*', '', content, flags=re.DOTALL)
    
    with open(modelfile_path, 'w', encoding='utf-8') as file:
        file.write(content)
    
    # Execute the command 'ollama create'
    subprocess.run(['ollama', 'create', LLM_USE, '--file', os.path.join(SYSTEM_INSTRUCTION_PATH, 'modelfile')])
    st.sidebar.success(f"Modèle LLM '{LLM_USE}' créé avec succès." if LANGUAGE == 'fr' else 
                       f"LLM Model '{LLM_USE}' created successfully.")
