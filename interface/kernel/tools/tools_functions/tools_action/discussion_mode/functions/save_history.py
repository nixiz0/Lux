import os
import csv
import nltk
from CONFIG import LANGUAGE
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def extract_main_words(text, number_of_words=7):
    # Download necessary nltk resources
    nltk.download('punkt')
    nltk.download('punkt_tab')
    nltk.download('stopwords')

    words = word_tokenize(text)
    if LANGUAGE == 'fr':
        main_words = [word for word in words if word.lower() not in stopwords.words('french') and word.isalpha()]
    else:
        main_words = [word for word in words if word.lower() not in stopwords.words('english') and word.isalpha()]
    return main_words[:number_of_words]

def create_filename(conversation_history):
    if isinstance(conversation_history, list):
        main_words = []
        for entry in conversation_history[1:]:  # Ignore the first entry
            if "Assistant:" in entry:
                entry = entry.split("Assistant:")[1]
                main_words.extend(extract_main_words(entry))
                if len(main_words) >= 7:
                    break
        filename = "_".join(main_words[:7]) + ".csv"
    else:
        main_words = extract_main_words(conversation_history)
        filename = "_".join(main_words[:7]) + ".txt"
    return filename

def save_history(conversation_history):
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    filename = create_filename(conversation_history)
    file_path = os.path.join(desktop_path, filename)
    
    base, extension = os.path.splitext(file_path)
    counter = 1
    while os.path.exists(file_path):
        file_path = f"{base}_{counter}{extension}"
        counter += 1
    
    if isinstance(conversation_history, list):
        with open(file_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for entry in conversation_history:
                writer.writerow([entry])
    else:
        with open(file_path, mode='a', encoding='utf-8') as file:
            file.write(conversation_history + "\n")
