import webbrowser
from CONFIG import LANGUAGE
from kernel.tools.tools_functions.tools_action.web_search.check_connection import is_connected

if is_connected():
    import pywhatkit


def search_ytb(user_prompt):
    # Search on YouTube
    youtube_keywords = ['cherche sur youtube', 'recherche sur youtube', 'rechercher sur youtube', 'find on youtube', 'find in youtube']
    if any(keyword in user_prompt for keyword in youtube_keywords):
        ytb_command = user_prompt.replace('Open YouTube and find', '')
        pywhatkit.playonyt(ytb_command)
        return f"Voici ce que j'ai trouvé monsieur" if LANGUAGE == 'fr' else f"This is what I found sir"
    
def search_wikipedia(user_prompt):
    # Extract last word from user prompt
    search = user_prompt.split()[-1]
    url = "https://fr.wikipedia.org/wiki/" + search
    webbrowser.open(url)
    return f"Voici ce que j'ai trouvé sur Wikipédia {search}" if LANGUAGE == 'fr' else f"Here's what I found on Wikipedia {search}"
        
def search_google(user_prompt):
    # Google
    google_keywords = ['cherche sur google', 'recherche sur google', 'find on google', 'find in google']
    for keyword in google_keywords:
        if keyword in user_prompt:
            search = user_prompt.replace(keyword, '').strip()
            if search.startswith('re '):
                search = search[3:]
            url = "https://www.google.com/search?q=" + search
            webbrowser.open(url)
            return f"Voici ce que j'ai trouvé sur Google {search}" if LANGUAGE == 'fr' else f"This is what I found on Google {search}"

def search_bing(user_prompt):    
    # Bing
    bing_keywords = ['cherche sur bing', 'recherche sur bing', 'find on bing', 'find in bing']
    for keyword in bing_keywords:
        if keyword in user_prompt:
            search = user_prompt.replace(keyword, '').strip()
            if search.startswith('re '):
                search = search[3:]
            url = "https://www.bing.com/search?q=" + search
            webbrowser.open(url)
            return f"Voici ce que j'ai trouvé sur Bing {search}" if LANGUAGE == 'fr' else f"Here's what I found on Bing {search}"
        
def search_gpt():
    # Chat GPT
    url = "https://chat.openai.com/"
    webbrowser.open(url)
    return f"Ouverture de Chat GPT" if LANGUAGE == 'fr' else f"Open Chat GPT"
