import os


def save_to_txt(text, filename="code_generated.txt"):
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    file_path = os.path.join(desktop_path, filename)
    
    base, extension = os.path.splitext(file_path)
    counter = 1
    while os.path.exists(file_path):
        file_path = f"{base}_{counter}{extension}"
        counter += 1
    
    with open(file_path, "a") as file:
        if isinstance(text, list):
            for entry in text:
                file.write(entry + "\n")
        else:
            file.write(text + "\n")