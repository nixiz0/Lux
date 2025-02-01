import os
import ast
import streamlit as st


def manage_select_tool(tools_config_target, source_select_tool_file):
    """
    Manages the selection of tools by updating the configuration file with content from the source file.

    This function performs the following tasks:
    1. Reads the content of the source select tool file, if it exists.
    2. Extracts the list of tools from the new content.
    3. Safely converts the extracted string to a list.
    4. Reads the current configuration content from the target file.
    5. Finds and updates the PARAMS_LIST_TOOLS in the configuration file.
    6. Merges the current and new tools lists without duplicates.
    7. Writes the updated content back to the configuration file.

    Args:
        tools_config_target (str): The path to the target configuration file.
        source_select_tool_file (str): The path to the source select tool file.
    """

    if os.path.exists(source_select_tool_file):
        with open(source_select_tool_file, 'r') as file:
            new_content = file.read()

        # Find the list of tools in the new content
        start_index = new_content.find("[")
        end_index = new_content.find("]") + 1
        if start_index != -1 and end_index != -1:
            new_tools_list_str = new_content[start_index:end_index]
            try:
                new_tools_list = ast.literal_eval(new_tools_list_str)  # Convert string to list safely
            except (SyntaxError, ValueError) as e:
                st.error(f"Syntax error in select_tool.py content: {e}")
                return

            # Update the CONFIG.py file
            if os.path.exists(tools_config_target):
                with open(tools_config_target, 'r') as file:
                    config_content = file.read()

                # Find and update PARAMS_LIST_TOOLS
                start_index = config_content.find("PARAMS_LIST_TOOLS = [")
                end_index = config_content.find("]", start_index) + 1
                if start_index != -1 and end_index != -1:
                    current_tools_list_str = config_content[start_index: end_index]
                    try:
                        # Extract only the list part
                        current_tools_list = ast.literal_eval(current_tools_list_str.split(" = ", 1)[1])
                    except (SyntaxError, ValueError) as e:
                        st.error(f"Syntax error in CONFIG.py content: {e}")
                        return
                    updated_tools_list = list(set(current_tools_list + new_tools_list))  # Merge lists without duplicates

                    # Update the contents of the CONFIG.py file
                    config_content = config_content[:start_index] + "PARAMS_LIST_TOOLS = " + str(updated_tools_list) + config_content[end_index:]
                    with open(tools_config_target, 'w') as file:
                        file.write(config_content)