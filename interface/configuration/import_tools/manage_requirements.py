import os
import shutil
import subprocess


def manage_requirements(tools_requirements_target, source_requirements_file):
    """
    Manages the requirements by updating the target file with content from the source file.

    This function performs the following tasks:
    1. Reads the content of the source requirements file, if it exists.
    2. Reads the current requirements from the target file, if it exists.
    3. Adds new libraries from the source file to the target file without duplicates.
    4. Appends each new library below the existing ones.
    5. Writes the updated content back to the target requirements file.
    6. Activates the environment and installs new libraries if they were added.

    Args:
        tools_requirements_target (str): The path to the target requirements file.
        source_requirements_file (str): The path to the source requirements file.
    """
    
    if os.path.exists(source_requirements_file):
        with open(source_requirements_file, 'r') as file:
            new_requirements = file.readlines()

        if os.path.exists(tools_requirements_target):
            with open(tools_requirements_target, 'r') as file:
                current_requirements = file.readlines()

            # Add new lines without duplicates
            new_libraries = [lib for lib in new_requirements if lib not in current_requirements]
            
            # Insert each new library below the existing ones
            for lib in new_libraries:
                current_requirements.append('\n' + lib.strip())

            with open(tools_requirements_target, 'w') as file:
                file.writelines(current_requirements)

            # Get the correct path
            current_directory = os.getcwd()
            env_directory = os.path.join(current_directory, ".env", "Scripts")
            activate_script = os.path.join(env_directory, "activate")

            # Activate env to install new lib if new lib has been written with the requirements
            activate_command = f"{activate_script} && pip install -r {tools_requirements_target}"
            subprocess.run(activate_command, shell=True, check=True)
        else:
            # Copy the requirements.txt file if it doesn't already exist
            shutil.copy(source_requirements_file, tools_requirements_target)