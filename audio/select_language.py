from constant.colors import *


def select_lang():
    choix = ""
    while choix not in ["1", "2"]:
        choix = input(f"{GREEN}Type 1 for French or 2 for English: {RESET}")
        if choix not in ["1", "2"]:
            print(f"{RED}Invalid choice. Please type 1 or 2.{RESET}")
    
    lang = 'fr' if choix == "1" else 'en'
    
    with open("CONFIG.py", "r") as file:
        lines = file.readlines()
    
    with open("CONFIG.py", "w") as file:
        for line in lines:
            if line.startswith("LANGUAGE"):
                file.write(f"LANGUAGE = '{lang}'\n")
            else:
                file.write(line)
    
    print(f"{CYAN}Language chosen: {'french' if lang == 'fr' else 'english'}{RESET}")
