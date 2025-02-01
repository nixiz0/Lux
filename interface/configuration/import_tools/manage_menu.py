import os
import ast


def manage_menu(tools_menu_target, menu_file):
    """
    Manages the menu by updating the target menu file with content from the source menu file.

    This function performs the following tasks:
    1. Reads the content of the source menu file, if it exists.
    2. Extracts the new tool entry from the source menu content.
    3. Reads the current menu content from the target file.
    4. Adds the new tool entry to the current tools list in the target menu file.
    5. Writes the updated menu content back to the target menu file.

    Args:
        tools_menu_target (str): The path to the target menu file.
        menu_file (str): The path to the source menu file.
    """

    if os.path.exists(menu_file):
        with open(menu_file, 'r', encoding='utf-8') as file:
            menu_content = file.read()
        new_tool_entry = ast.literal_eval(menu_content)
        interface_menu_file = tools_menu_target
        with open(interface_menu_file, 'r', encoding='utf-8') as file:
            current_menu_content = file.read()

        # Find the start and end of the tools list
        tools_list_start = current_menu_content.find("tools = [") + len("tools = [")
        tools_list_end = current_menu_content.find("]", tools_list_start)

        if tools_list_start != -1 and tools_list_end != -1:
            current_tools_list = current_menu_content[tools_list_start:tools_list_end].strip()
            if current_tools_list and current_tools_list[-1] != ',':
                current_tools_list += ",\n    " + repr(new_tool_entry).strip('()')
            elif not current_tools_list:
                current_tools_list = "    " + repr(new_tool_entry).strip('()')
            else:
                current_tools_list += "\n    " + repr(new_tool_entry).strip('()')

            updated_menu_content = current_menu_content[:tools_list_start] + current_tools_list + current_menu_content[tools_list_end:]
            with open(interface_menu_file, 'w', encoding='utf-8') as file:
                file.write(updated_menu_content)