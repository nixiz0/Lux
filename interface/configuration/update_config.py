def update_config(key, value):
    """
    Updates the configuration file with a new value for a specified key.

    Parameters:
    key (str): The configuration key to update.
    value (any): The new value to set for the specified key.
    """
    with open('interface/CONFIG.py', 'r') as file:
        lines = file.readlines()

    with open('interface/CONFIG.py', 'w') as file:
        for line in lines:
            if line.startswith(key):
                file.write(f"{key} = {value}\n")
            else:
                file.write(line)