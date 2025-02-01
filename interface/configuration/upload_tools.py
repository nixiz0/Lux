import os
import shutil
import zipfile
import streamlit as st
from CONFIG import LANGUAGE, TOOLS_ACTION_TARGET, TOOLS_RESPONSE_TARGET, TOOLS_LIST_TARGET, \
                   TOOLS_CONFIG_TARGET, TOOLS_REQUIREMENTS_TARGET, TOOLS_MENU_TARGET
from kernel.agent_llm.vectorization_tools import revectorize_tool
from configuration.import_tools.manage_tools_list import manage_tools_list
from configuration.import_tools.manage_select_tool import manage_select_tool
from configuration.import_tools.manage_requirements import manage_requirements
from configuration.import_tools.manage_menu import manage_menu


def copy_contents(src, dst):
    """
    Recursively copies the contents from the source directory to the destination directory.

    This function performs the following tasks:
    1. Checks if the source is a directory.
    2. Creates the destination directory if it does not exist.
    3. Iterates through the items in the source directory and copies them to the destination directory.
    4. Recursively copies contents if the item is a directory.

    Args:
        src (str): The path to the source directory or file.
        dst (str): The path to the destination directory or file.
    """
    if os.path.isdir(src):
        if not os.path.exists(dst):
            os.makedirs(dst)
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                copy_contents(s, d)
            else:
                shutil.copy2(s, d)
    else:
        shutil.copy2(src, dst)

def adding_tool():   
    """
    Manages the process of adding tools by uploading and extracting a zip file containing the tools.

    This function performs the following tasks:
    1. Creates a temporary directory for downloaded tools.
    2. Prompts the user to upload a zip file containing the necessary tools.
    3. Extracts the zip file to the temporary directory.
    4. Copies the contents of specific folders within the extracted files to designated target directories.
    5. Manipulates the tools_list.py file, select_tool.py file, and requirements.txt file.
    6. Adds entries from menu.py file (if present) to the application's menu.py file.
    7. Displays success messages and instructions to the user.
    """

    # Temporary directory for downloaded tools
    temp_dir = "/tmp/uploaded_tools"
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)

    st.write("## **Importer vos Outils**" if LANGUAGE == 'fr' else "## **Import your Tools**")
    
    # Drop a zip file
    uploaded_file = st.file_uploader("Déposez un fichier zip contenant les outils nécessaires" if LANGUAGE == 'fr' else
                                     "Upload a zip file with the necessary tools", type=["zip"])
    
    if uploaded_file is not None:
        # Recover zip name file
        zip_filename = uploaded_file.name

        # Unzip the zip file to a temporary directory
        with zipfile.ZipFile(uploaded_file, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)

        # Retrieve the name of the first folder in the temporary directory
        tool_dir = os.path.join(temp_dir, os.listdir(temp_dir)[0])

        # Browse extracted files and folders
        for root, dirs, files in os.walk(tool_dir):
            for dir_name in dirs:
                if dir_name == "tools_action":
                    # Copy the contents of the tools_action folder
                    src_path = os.path.join(root, dir_name)
                    dst_path = TOOLS_ACTION_TARGET
                    copy_contents(src_path, dst_path)
                elif dir_name == "tools_response":
                    # Copy the contents of the tools_response folder
                    src_path = os.path.join(root, dir_name)
                    dst_path = TOOLS_RESPONSE_TARGET
                    copy_contents(src_path, dst_path)

        # Manipulate the tools_list.py file
        tools_list_file = os.path.join(tool_dir, "tools_list.py")
        manage_tools_list(TOOLS_LIST_TARGET, tools_list_file)

        # Path to the select_tool.py file in the source folder
        source_select_tool_file = os.path.join(tool_dir, "select_tool.py")
        manage_select_tool(TOOLS_CONFIG_TARGET, source_select_tool_file)

        # Path to the requirements.txt file in the source folder
        source_requirements_file = os.path.join(tool_dir, "requirements.txt")
        manage_requirements(TOOLS_REQUIREMENTS_TARGET, source_requirements_file)

        menu_file = os.path.join(tool_dir, "menu.py")
        manage_menu(TOOLS_MENU_TARGET, menu_file)

        st.success(f"L'outil {zip_filename} a correctement été importé dans votre assistant." if LANGUAGE == 'fr' else
                   f"The tool {zip_filename} has been successfully imported into your assistant.")

        st.write("**Après avoir importé vos outils, cliquez sur la croix pour supprimer le fichier upload dans l'application.**" if LANGUAGE == 'fr' else 
                "**After importing your tools, click on the cross to delete the upload file in the application.**")

    if uploaded_file is None:
        # Highlight the instruction text
        st.write("**Une fois que vous avez importé tous les outils que vous voulez, cliquez sur le bouton ci-dessous**" if LANGUAGE == 'fr' else 
                 "**Once you have imported all the tools you want, click the button below**")

        # Change checkbox to button
        if st.button("Ajouter vos outils importés" if LANGUAGE == 'fr' else "Add your imported tools", key='config_revectorize_tools'):
            revectorize_tool()