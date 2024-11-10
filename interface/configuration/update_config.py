def update_config(key, value):
    with open('interface/CONFIG.py', 'r') as file:
        lines = file.readlines()

    with open('interface/CONFIG.py', 'w') as file:
        for line in lines:
            if line.startswith(key):
                file.write(f"{key} = {value}\n")
            else:
                file.write(line)