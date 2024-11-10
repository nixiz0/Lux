# Lux-Interface

Interface of Lux assistant which has a speech to text to transcribe your voice into text, a RAG system on tools to use tools according to the user's prompt and finally a voice cloning system allowing you to do text to speech on a customizable voice that you choose (or you can keep the voice that is already cloned and used by default in the kernel).


## Installation

=> Click on Lux-Interface-Installer.exe to download the app (be careful to install the necessary applications in Tech Stack).

=> Afterwards you click on lux-interface.exe to build environment for the app.


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
