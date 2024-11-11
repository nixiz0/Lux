# Lux-Interface

Interface of Lux assistant which has a speech to text to transcribe your voice into text, a RAG system on tools to use tools according to the user's prompt and finally a voice cloning system allowing you to do text to speech on a customizable voice that you choose (or you can keep the voice that is already cloned and used by default in the kernel).


## Installation

=> Click on Lux-Interface-Installer.exe to download the app (be careful to install the necessary applications in Tech Stack).

=> Afterwards you click on lux-interface.exe to build environment for the app.


## Tools in Lux-Interface (by default that you can use)

- [Tool hello]: "description: "dit bonjour pour saluer" / "says hello to greet";

- [Tool pause_running]: "description": "met en pause le système, mode pause" / "pauses the system, pause mode";

- [Tool exit_system]: "description": "arrête le système, met à l'arrêt, stop tout"  / "shut down the system, shut down, stop everything";

- [Tool time_in_locale]: "description": "il est quelle heure"  / "what time is it";

- [Tool date_in_locale]: "description": "quelle est la date actuelle"  / "what is the current date";

- [Tool use_code_mode]: "description": "mode code qui est un outil pour faire de la programmation, du codage"  / "code mode which is a tool for programming, coding";

- [Tool use_discussion_mode]: "description": "mode discussion qui permet d'avoir une conversation, une discussion, de discuter"  / "discussion mode which allows to have a conversation, a discussion, to discuss";

- [Tool screen_with_cam]: "description": "screen avec la caméra"  / "screen with the camera";

- [Tool screen]: "description": "prends un screenshot, prends une capture d'écran"  / "take a screenshot";

- [Tool vocal_note]: "description": "prends note"  / "take note";

- [Tool start_llm_vision]: "description": "outil pour utiliser le mode vision"  / "tool to use vision mode";

- [Tool search_ytb]: "description": "recherche sur youtube, cherche sur youtube"  / "search on youtube";

- [Tool search_google]: "description": "cherche sur google, recherche sur google"  / "search on google";

- [Tool search_wikipedia]: "description": "cherche sur wikipédia, recherche sur wikipédia"  / "search on wikipedia";

- [Tool search_bing]: "description": "cherche sur bing, recherche sur bing"  / "search on bing";

- [Tool search_gpt]: "description": "ouvre chat gpt"  / "open chat gpt";


## Tech Stack

[Application you have to install on your computer]

=> Download Ollama : https://ollama.com/download

=> Download Python 3.11 (and add path to your os env variable) : https://www.python.org/downloads/release/python-3117/

=> Download CUDA 11.8 (check that your graphics card is compatible) : https://developer.nvidia.com/cuda-11-8-0-download-archive

*You may need to install (depends on your computer)*
- VS Community (with Dekstop packages) : https://visualstudio.microsoft.com/fr/vs/community/

- scoop : ```powershell -Command "Set-ExecutionPolicy RemoteSigned -scope CurrentUser"``` & ```powershell -Command "iex (new-object net.webclient).downloadstring('https://get.scoop.sh')"```

- ffmpeg (put on path env variable) : ```scoop install ffmpeg``` and go on like C:\Users\your_user_name\scoop\apps\ffmpeg\your_version_of_ffmpeg\bin, copy the absolute path on the url on the top, open your environnement variables, go on 'PATH' in your user on your environnement variables and click on 'new' button and paste the url that you copied


## Author

- [@nixiz0](https://github.com/nixiz0)
