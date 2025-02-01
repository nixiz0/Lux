def update_config(key, value, default_path_config='interface/CONFIG.py'):
    """
    Updates the configuration file with a new value for a specified key.

    Parameters:
    key (str): The configuration key to update.
    value (any): The new value to set for the specified key.
    default_path_config (str optional): Put path of CONFIG file to update.
    """
    with open(default_path_config, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(default_path_config, 'w', encoding='utf-8') as file:
        for line in lines:
            if line.startswith(key):
                file.write(f"{key} = {value}\n")
            else:
                file.write(line)