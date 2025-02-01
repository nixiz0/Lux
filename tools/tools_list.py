from CONFIG import LANGUAGE
from tools.tools_functions.tools_response.hello_sir import hello
from tools.tools_functions.pause_system import pause_running
from tools.tools_functions.exit_system import stop_running
from tools.tools_functions.tools_action.time import time_in_locale, date_in_locale


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
}
