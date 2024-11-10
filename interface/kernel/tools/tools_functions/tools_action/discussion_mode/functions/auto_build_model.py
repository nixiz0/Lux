import streamlit as st
import subprocess
import os
import re
from kernel.tools.tools_functions.tools_action.discussion_mode.CONFIG_TOOL import *


def build_discussion_model():
    # Run the 'ollama show' command and get the output
    show_result = subprocess.run(['ollama', 'show', DISCUSSION_BASE_LLM, '--modelfile'], shell=True, capture_output=True, text=True, encoding='utf-8')

    # Create a file named 'modelfile' and write the output of 'ollama show' to it
    modelfile_path = os.path.join(DISCUSSION_SYSTEM_INSTRUCTION_PATH, 'modelfile')
    
    if show_result.returncode == 0 and show_result.stdout:
        with open(modelfile_path, 'w', encoding='utf-8') as file:
            file.write(show_result.stdout)
    else:
        st.error(f"La commande 'ollama show' n'a produit aucune sortie ou a échoué." if LANGUAGE == 'fr' else 
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
    
    # Find the TEMPLATE block and insert the SYSTEM after
    template_pattern = re.compile(r'(TEMPLATE """.*?""")', re.DOTALL)
    content = template_pattern.sub(r'\1\nSYSTEM """' + DISCUSSION_SYSTEM_INSTRUCTION + '"""', content)
    
    # Remove the LICENSE section and everything after it
    content = re.sub(r'LICENSE.*', '', content, flags=re.DOTALL)
    
    with open(modelfile_path, 'w', encoding='utf-8') as file:
        file.write(content)
    
    # Execute the command 'ollama create'
    subprocess.run(['ollama', 'create', DISCUSSION_MODEL_NAME, '--file', os.path.join(DISCUSSION_SYSTEM_INSTRUCTION_PATH, 'modelfile')])
    st.success(f"Modèle LLM '{DISCUSSION_MODEL_NAME}' créé avec succès." if LANGUAGE == 'fr' else 
               f"LLM Model '{DISCUSSION_MODEL_NAME}' created successfully.")
