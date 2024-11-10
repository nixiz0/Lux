import os
import subprocess
import platform


# Install pyinstaller and run the command :
# <= pyinstaller --onefile [setup]/setup.py => to build the .exe file

def start_app():
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
    print("Virtual environment activated.")

    # Check if required libraries are installed
    try:
        subprocess.run([pip_executable, 'show', 'torch'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run([pip_executable, 'show', 'torchaudio'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("Required libraries are already installed.")
    except subprocess.CalledProcessError:
        print("Installing required libraries...")
        subprocess.run([pip_executable, 'install', 'torch', 'torchaudio', '--index-url', 'https://download.pytorch.org/whl/cu118'])
        subprocess.run([pip_executable, 'install', '-r', 'requirements.txt'])

    if platform.system() == 'Windows':
        subprocess.Popen(['start', 'cmd', '/k', 'ollama serve'], shell=True)
    else:
        subprocess.Popen(['gnome-terminal', '--', 'ollama serve'], shell=True)

    # Check for any missing libraries and install them
    try:
        subprocess.run([python_executable, 'main.py'], check=True)
    except subprocess.CalledProcessError:
        print("Errors detected. Reinstalling libraries from requirements.txt...")
        subprocess.run([pip_executable, 'install', '-r', 'requirements.txt'])
        subprocess.run([python_executable, 'main.py'])

def auto_run_and_install():
    if not os.path.exists('.env'):
        subprocess.run(['python', '-m', 'venv', '.env'])
        print("Virtual environment created.")
    else:
        print("Virtual environment already exists.")
    start_app()

if __name__ == "__main__":
    auto_run_and_install()
