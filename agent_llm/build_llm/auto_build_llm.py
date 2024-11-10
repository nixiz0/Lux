import subprocess
import os
import re
from CONFIG import *
from constant.colors import *


def build_the_model():
    # Run the 'ollama list' command and get the output
    result = subprocess.run(['ollama', 'list'], capture_output=True, text=True)
    
    # Checks if LLM_NAME is in the list of models
    if LLM_USE in result.stdout:
        pass
    else:
        print(f"{RED}Modèle {LLM_USE} non trouvé. Initialisation des installations des LLMS utilisés par l'Assistant.{RESET}" if LANGUAGE == 'fr' else
              f"{RED}Model {LLM_USE} not found. Initialization of the installations of LLMS used by the Assistant. {LLM_DEFAULT_TO_PULL}.{RESET}")
        subprocess.run(['ollama', 'pull', LLM_DEFAULT_TO_PULL])
        subprocess.run(['ollama', 'pull', LLM_EMBEDDING])

        # Run the 'ollama show' command and get the output
        show_result = subprocess.run(['ollama', 'show', LLM_DEFAULT_TO_PULL, '--modelfile'], shell=True, capture_output=True, text=True, encoding='utf-8')

        # Create a file named 'modelfile' and write the output of 'ollama show' to it
        modelfile_path = os.path.join(SYSTEM_INSTRUCTION_PATH, 'modelfile')
        
        if show_result.returncode == 0 and show_result.stdout:
            with open(modelfile_path, 'w', encoding='utf-8') as file:
                file.write(show_result.stdout)
        else:
            print(f"{RED}La commande 'ollama show' n'a produit aucune sortie ou a échoué.{RESET}" if LANGUAGE == 'fr' else 
                  f"{RED}The 'ollama show' command produced no output or failed.{RESET}")
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
        print(f"{CYAN}Modèle LLM '{LLM_USE}' créé avec succès.{RESET}" if LANGUAGE == 'fr' else 
              f"{CYAN}LLM Model '{LLM_USE}' created successfully.{RESET}")
