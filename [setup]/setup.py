# [BUILD] Install pyinstaller and run the command (to build .exe file) :
# <= pyinstaller --onefile --icon=interface/ressources/logo-lux-interface.ico [setup]/setup.py => 

import os
import subprocess


# ---[ANSI COLOR]---
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"


# ---[UPDATE FILES FUNCTIONS (for voice)]---
def update_start_kernel(choice):
    with open('interface/kernel/start_kernel.py', 'r') as file:
        lines = file.readlines()
    with open('interface/kernel/start_kernel.py', 'w') as file:
        for line in lines:
            if 'from interface.kernel.audio.synthetic_voice' in line:
                if choice == '1':
                    file.write('from interface.kernel.audio.synthetic_voice.narrator_voice import LuxVoice\n')
                else:
                    file.write('from interface.kernel.audio.synthetic_voice.synthetic_voice import LuxVoice\n')
            else:
                file.write(line)

def update_requirements(choice):
    with open('requirements.txt', 'r') as file:
        lines = file.readlines()
    with open('requirements.txt', 'w') as file:
        for line in lines:
            file.write(line)
        if choice == '1':
            file.write('comtypes==1.4.5\n')
            file.write('pyttsx3==2.90\n')
        else:
            file.write('TTS==0.22.0\n')

def update_configuration_voice_import(choice):
    config_file = 'interface/pages/1_configuration.py'
    with open(config_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Find the last line that contains 'from configuration.audio'
    last_index = -1
    for i, line in enumerate(lines):
        if 'from configuration.audio' in line:
            last_index = i

    # If the line exists, replace it
    if last_index != -1:
        if choice == '1':
            lines[last_index] = 'from configuration.audio.select_narrator_voice import manage_voice\n'
        else:
            lines[last_index] = 'from configuration.audio.change_synthetic_voice import manage_voice\n'

    # Write updated lines to file
    with open(config_file, 'w', encoding='utf-8') as file:
        file.writelines(lines)

# ---[SCRIPT INSTALLATION LOGIC]---
def start_ollama():
    subprocess.Popen(['start', 'cmd', '/c', 'ollama serve'], shell=True)

def choose_voice():
    if not os.path.exists('.env'):
        choice = input("Type 1 to use narrator or 2 to use synthetic voice: ")

        if choice not in ['1', '2']:
            print("Invalid choice. Please type 1 or 2.")
            return

        update_start_kernel(choice)
        update_requirements(choice)
        update_configuration_voice_import(choice)

def build_env():
    if not os.path.exists('.env'):
        subprocess.run(['python', '-m', 'venv', '.env'])
        print(f"{CYAN}Virtual environment created.{RESET}")
    else:
        print(f"{CYAN}Virtual environment already exists.{RESET}")

def start_and_install_lib():
    activate_script = '.env\\Scripts\\activate.bat'
    pip_executable = '.env\\Scripts\\pip'
    python_executable = '.env\\Scripts\\python'

    # Activate the virtual environment
    subprocess.run(activate_script, shell=True)
    print(f"{CYAN}Virtual environment activated.{RESET}")

    # Check if required libraries are installed
    try:
        subprocess.run([pip_executable, 'show', 'torchaudio'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run([pip_executable, 'show', 'streamlit'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"{CYAN}Required libraries are already installed.{RESET}")
    except subprocess.CalledProcessError:
        print(f"{CYAN}Installing required libraries...{RESET}")
        subprocess.run([pip_executable, 'install', 'torch==2.3.1', 'torchaudio==2.3.1', '--index-url', 'https://download.pytorch.org/whl/cu118'])
        subprocess.run([pip_executable, 'install', '-r', 'requirements.txt'])

        subprocess.run(['powershell', '-Command', 'Set-ExecutionPolicy RemoteSigned -scope CurrentUser'], check=True)
        subprocess.run(['powershell', '-Command', 'iwr -useb get.scoop.sh | iex'], check=True)
        subprocess.run(['powershell', '-Command', 'scoop install ffmpeg'], check=True)

    # Start the app interface
    subprocess.run([python_executable, '-m', 'streamlit', 'run', 'interface/menu.py'], check=True)

def auto_run():
    start_ollama()
    choose_voice()
    build_env()
    start_and_install_lib()

if __name__ == "__main__":
    auto_run()