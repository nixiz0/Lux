import os


def manage_tools_list(tools_list_target, tools_list_file):
    """
    Manages the tools list by updating the target file with content from the source file.

    This function performs the following tasks:
    1. Reads the current content of the target tools list file.
    2. Reads the content of the source tools list file, if it exists.
    3. Extracts 'from' import statements from the source file and ensures they are present in the target file.
    4. Merges the tools dictionaries from both files, handling commas, line breaks, and formatting.
    5. Writes the updated content back to the target tools list file.

    Args:
        tools_list_target (str): The path to the target tools list file.
        tools_list_file (str): The path to the source tools list file.
    """

    if os.path.exists(tools_list_target):
        with open(tools_list_target, 'r') as file:
            current_content = file.read()
            
        if os.path.exists(tools_list_file):
            with open(tools_list_file, 'r') as file:
                new_content = file.read()

            # Extract 'from' imports and add them in the right place
            import_lines = [line for line in new_content.splitlines() if line.startswith("from ")]
            new_tools_dict = new_content.split("tools = {")[1].rsplit("}", 1)[0].strip()
            new_tools_dict = "    " + new_tools_dict.replace("\n", "\n    ")

            for line in import_lines:
                if line not in current_content:
                    current_content = line + '\n' + current_content

            # Recreate the tools dictionary in current content
            if "tools = {" in current_content:
                current_tools_dict = current_content.split("tools = {")[1].rsplit("}", 1)[0].strip()
                current_tools_dict = "    " + current_tools_dict.replace("\n", "\n    ")

                # Merge dictionaries and handle commas and line breaks
                if current_tools_dict and not current_tools_dict.endswith(','):
                    current_tools_dict += ","
                combined_tools_dict = current_tools_dict + "\n\n" + new_tools_dict

                # Reformat the combined dictionary
                formatted_tools_dict = "tools = {\n" + combined_tools_dict + "\n}"

                # Replace tools dictionary content with current content
                current_content = current_content.split("tools = {")[0] + formatted_tools_dict + "\n" + current_content.split("tools = {")[1].rsplit("}", 1)[1]

                with open(tools_list_target, 'w') as file:
                    file.write(current_content)