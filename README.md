# Lux Project

Welcome to the **Lux Project**! This project aims to provide a powerful and flexible assistant for all users (using the version accessible to all who are Lux-Interface) but also for developers (using the Lux-Kernel versions here) allowing developers to use this as a basis to build whatever they want with.


## 🖥️ Lux Interface

The **Lux Interface** is designed for end-users who may not be developers. It provides a user-friendly interface to configure and personalize the assistant without using command lines.

The interface is user-friendly and allow to:
- Configure the system.
- Import different tools.
- Run the asssitant.


## 🛠️ Lux Kernel

The **Lux Kernel** is designed for developers and consists of two main components:

1. **Synthetic Cloned Voice Kernel**: A text-to-speech system using cloned synthetic voices (*requires high-performance hardware to use this system*), here we use *CoquiTTS*.
2. **Synthetic Narrator Voice Kernel**: A text-to-speech system using a windows narrator's voice.

The Lux Kernels also includes:
- **Speech-to-Text**: Convert spoken words into text, using *Whisper large v3*.
- **Intelligent Tool Selection System**: Using a RAG system to select tools based on user prompts, using *sklearn* for similarity & *ChromaDB* for vector database.
- **Inspired by Linux Kernel**: A flexible and small assistant core to allow developers to create various features with it and be able to use it as a base.


## 🚀 Installation

1. **Download the App**:
   - Click on `Lux-Interface-Installer.exe` to download the app.
   - Ensure to install the necessary applications in the *Tech Stack*.

2. **Build the Environment**:
   - Click on `lux-interface.exe` to build the environment for the app.


## 🏗️ System Architecture

<img src="interface/ressources/schema-system-architecture/lux-system-architecture.png" alt="Lux System Architecture" width="800"/>


## Tech Stack

[Application you have to install on your computer]

=> Download Ollama : https://ollama.com/download (version 0.5.4)

=> Download Python 3.11 (and add path to your os env variable) : https://www.python.org/downloads/release/python-3117/

=> Download CUDA 11.8 (check that your graphics card is compatible) : https://developer.nvidia.com/cuda-11-8-0-download-archive

*You may need to install (depends on your computer)*
- VS Community (with Dekstop packages) : https://visualstudio.microsoft.com/fr/visual-cpp-build-tools/

- scoop : ```powershell -Command "Set-ExecutionPolicy RemoteSigned -scope CurrentUser"``` & ```powershell -Command "iex (new-object net.webclient).downloadstring('https://get.scoop.sh')"```

- ffmpeg (put on path env variable) : ```scoop install ffmpeg``` and go on like C:\Users\your_user_name\scoop\apps\ffmpeg\your_version_of_ffmpeg\bin, copy the absolute path on the url on the top, open your environnement variables, go on 'PATH' in your user on your environnement variables and click on 'new' button and paste the url that you copied


## Windows Narrator Voices

If you want to use Windows Narrator Voices instead of cloned voices, you have more synthetic voices available you have to go to the narrator settings and you can download the voices you want.

If this doesn't work and doesn't recognize the voices you have installed on the narrator settings, follow this steps :

- 1-/Open the Registry Editor by pressing the “Windows” and “R” keys simultaneously, then type “regedit” and press Enter.

- 2-/Navigate to the registry key : HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens.

- 3-/Export this key to a REG file (with a right click on the file).

- 4-/Open this file with a text editor and replace all occurrences of HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens with HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SPEECH\Voices\Tokens.

- 5-/Save the modified file and double-click it to import the changes to the registry.


## Author

- [@nixiz0](https://github.com/nixiz0)
