import os
from CONFIG import LANGUAGE, LLM_USE
from constant.colors import *
from agent_llm.build_llm.auto_build_llm import build_the_model


def choose_llm_reset():
    while True:
        choice = input(f"{GREEN}\nTapez 1 pour supprimer l'assistant ou 2 pour le conserver : {RESET}" if LANGUAGE == 'fr' else 
                       f"{GREEN}\nType 1 to remove the assistant or 2 to keep it : {RESET}")
        if choice == '1':
            print(f"{CYAN}Vous avez choisi de supprimer l'assistant.{RESET}" if LANGUAGE == 'fr' else 
                  f"{CYAN}You chose to remove the assistant.{RESET}")
            os.system(f"ollama rm {LLM_USE}")
            build_the_model()
            break
        elif choice == '2':
            print(f"{CYAN}Vous avez choisi de garder l'assistant.{RESET}" if LANGUAGE == 'fr' else 
                  f"{CYAN}You chose to keep the assistant.{RESET}")
            break
        else:
            print(f"{RED}Entrée invalide. Veuillez saisir 1 ou 2.{RESET}" if LANGUAGE == 'fr' else 
                  f"{RED}Invalid input. Please type 1 or 2.{RESET}")
