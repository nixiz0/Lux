import os 
import pyautogui

from CONFIG import LANGUAGE


def screen():
    download_dir = str('photos/')
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    base_filename = 'screenshot'
    extension = '.png'
    filename = f"{base_filename}{extension}"
    screenshot = pyautogui.screenshot()
    screenshot.save(os.path.join(download_dir, filename))
    
    return "Capture d'écran effectuée" if LANGUAGE == 'fr' else "Screenshot taken"