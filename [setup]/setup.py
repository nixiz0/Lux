# [BUILD] Install pyinstaller and run the command (to build .exe file) :
# <= pyinstaller --onefile --icon=interface/ressources/logo-lux-interface.ico [setup]/setup.py => 

import os
import platform
import subprocess


# ---[ANSI COLOR]---
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"

# ---[SCRIPT INSTALLATION LOGIC]---
def start_ollama():
    if platform.system() == 'Windows':
        subprocess.Popen(['start', 'cmd', '/c', 'ollama serve'], shell=True)
    else:
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'ollama serve; exit'], shell=True)

def build_env():
    if not os.path.exists('.env'):
        subprocess.run(['python', '-m', 'venv', '.env'])
        print(f"{CYAN}Virtual environment created.{RESET}")
    else:
        print(f"{CYAN}Virtual environment already exists.{RESET}")

def start_and_install_lib():
    if platform.system() == 'Windows':
        activate_script = '.env\\Scripts\\activate.bat'
        pip_executable = '.env\\Scripts\\pip'
        python_executable = '.env\\Scripts\\python'
    else:
        activate_script = '.env/bin/activate'
        pip_executable = '.env/bin/pip'
        python_executable = '.env/bin/python'

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
        subprocess.run([pip_executable, 'install', 'torch', 'torchaudio', '--index-url', 'https://download.pytorch.org/whl/cu118'])
        subprocess.run([pip_executable, 'install', '-r', 'requirements.txt'])

        if platform.system() == 'Windows':
            subprocess.run(['powershell', '-Command', 'Set-ExecutionPolicy RemoteSigned -scope CurrentUser'], check=True)
            subprocess.run(['powershell', '-Command', 'iwr -useb get.scoop.sh | iex'], check=True)
            subprocess.run(['powershell', '-Command', 'scoop install ffmpeg'], check=True)
        elif platform.system() == 'Linux':
            subprocess.run(['sudo', 'apt', 'update'], check=True)
            subprocess.run(['sudo', 'apt', 'install', '-y', 'ffmpeg'], check=True)
        elif platform.system() == 'Darwin':
            subprocess.run(['/bin/bash', '-c', '$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)'], check=True)
            subprocess.run(['brew', 'install', 'ffmpeg'], check=True)

    # Start the app interface
    subprocess.run([python_executable, '-m', 'streamlit', 'run', 'interface/menu.py'], check=True)

def auto_run():
    start_ollama()
    build_env()
    start_and_install_lib()

if __name__ == "__main__":
    auto_run()