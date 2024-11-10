import os

from CONFIG import LANGUAGE


def vocal_note(user_prompt):
    # Gets the user's download path
    download_path = os.path.join(os.path.expanduser("~"), 'Downloads')
    file_path = os.path.join(download_path, 'vocal_note.txt')
    
    # Checks if the file is empty or not
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        # If the file is not empty, append what the user said to the end of the file
        with open(file_path, 'a', encoding="utf-8") as f:
            f.write('\n' + user_prompt)
    else:
        # If the file is empty, writes what the user said to the file
        with open(file_path, 'a', encoding="utf-8") as f:
            f.write(user_prompt)

    return "C'est noté dans votre dossier de téléchargement" if LANGUAGE == 'fr' else "It's noted in your download folder"