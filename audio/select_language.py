from constant.colors import *
from constant.update_config import update_config


def select_lang():
    """
    Prompts the user to select a language (French or English) and updates the configuration file accordingly.

    The function continuously prompts the user until a valid choice (1 for French, 2 for English) is made.
    It then updates the 'LANGUAGE' setting in the 'CONFIG.py' file and confirms the selected language.
    """
    choix = ""
    while choix not in ["1", "2"]:
        choix = input(f"{GREEN}Type 1 for French or 2 for English: {RESET}")
        if choix not in ["1", "2"]:
            print(f"{RED}Invalid choice. Please type 1 or 2.{RESET}")
    
    lang = 'fr' if choix == "1" else 'en'
    
    # Updates CONFIG.py with the universal update_config function
    update_config('LANGUAGE', f"'{lang}'")

    print(f"{CYAN}Language chosen: {'french' if lang == 'fr' else 'english'}{RESET}")