from CONFIG import LANGUAGE
from kernel.tools.tools_functions.tools_response.hello_sir import hello
from kernel.tools.tools_functions.pause_system import pause_running
from kernel.tools.tools_functions.exit_system import stop_running
from kernel.tools.tools_functions.tools_action.time import time_in_locale, date_in_locale
from kernel.tools.tools_functions.tools_action.audio_management.audio_gestion import mute, demute, volume_increase, volume_decrease
from kernel.tools.tools_functions.tools_action.code_mode.start_code_mode import use_code_mode
from kernel.tools.tools_functions.tools_action.discussion_mode.start_discussion_mode import use_discussion_mode
from kernel.tools.tools_functions.tools_action.cam.screen_cam import screen_with_cam
from kernel.tools.tools_functions.tools_action.screenshot import screen
from kernel.tools.tools_functions.tools_action.take_note import vocal_note
from kernel.tools.tools_functions.tools_action.vision_mode.start_vision import start_llm_vision
from kernel.tools.tools_functions.tools_action.web_search.search_webs import search_ytb, search_google, search_wikipedia, search_bing, search_gpt


tools = {
    "hello": {"description": "dit bonjour pour saluer" if LANGUAGE == 'fr' else 
              "says hello to greet", 
              "function": hello},

    "pause_running": {"description": "met en pause le système, mode pause" if LANGUAGE == 'fr' else 
                     "pauses the system, pause mode", 
                     "function": pause_running},

    "exit_system": {"description": "arrête le système, met à l'arrêt, stop tout" if LANGUAGE == 'fr' else 
                    "shut down the system, shut down, stop everything", 
                    "function": stop_running},

    "time_in_locale": {"description": "il est quelle heure" if LANGUAGE == 'fr' else 
                       "what time is it", 
                       "function": time_in_locale},

    "date_in_locale": {"description": "quelle est la date actuelle" if LANGUAGE == 'fr' else 
                       "what is the current date", 
                       "function": date_in_locale},

    "mute": {"description": "mute le volume, mute le son, met en mode silence le volume" if LANGUAGE == 'fr' else 
            "mute the volume, mute the sound, mute the volume", 
            "function": mute},

    "demute": {"description": "remet le volume, demute le son" if LANGUAGE == 'fr' else 
               "reset the volume, unmute the sound", 
               "function": demute},

    "volume_increase": {"description": "augmente le volumne, augmente le son" if LANGUAGE == 'fr' else 
                        "increase the volume, increase the sound", 
                        "function": volume_increase},

    "volume_decrease": {"description": "diminue le volumne, diminue le son" if LANGUAGE == 'fr' else 
                        "decrease the volume, decrease the sound", 
                        "function": volume_decrease},

    "use_code_mode": {"description": "mode code qui est un outil pour faire de la programmation, du codage" if LANGUAGE == 'fr' else 
                      "code mode which is a tool for programming, coding", 
                      "function": use_code_mode},

    "use_discussion_mode": {"description": "mode discussion qui permet d'avoir une conversation, une discussion, de discuter" if LANGUAGE == 'fr' else 
                            "discussion mode which allows to have a conversation, a discussion, to discuss", 
                            "function": use_discussion_mode},

    "screen_with_cam": {"description": "screen avec la caméra" if LANGUAGE == 'fr' else 
                        "screen with the camera", 
                        "function": screen_with_cam},

    "screen": {"description": "prends un screenshot, prends une capture d'écran" if LANGUAGE == 'fr' else 
               "take a screenshot", 
               "function": screen},

    "vocal_note": {"description": "prends note" if LANGUAGE == 'fr' else 
                   "take note", 
                   "function": vocal_note},

    "start_llm_vision": {"description": "outil pour utiliser le mode vision" if LANGUAGE == 'fr' else 
                         "tool to use vision mode", 
                         "function": start_llm_vision},

    "search_ytb": {"description": "recherche sur youtube, cherche sur youtube" if LANGUAGE == 'fr' else 
                   "search on youtube", 
                   "function": search_ytb},

    "search_google": {"description": "cherche sur google, recherche sur google" if LANGUAGE == 'fr' else 
                      "search on google", 
                      "function": search_google},

    "search_wikipedia": {"description": "cherche sur wikipédia, recherche sur wikipédia" if LANGUAGE == 'fr' else 
                         "search on wikipedia", 
                         "function": search_wikipedia},

    "search_bing": {"description": "cherche sur bing, recherche sur bing" if LANGUAGE == 'fr' else 
                    "search on bing", 
                    "function": search_bing},

    "search_gpt": {"description": "ouvre chat gpt" if LANGUAGE == 'fr' else 
                   "open chat gpt", 
                   "function": search_gpt},
}