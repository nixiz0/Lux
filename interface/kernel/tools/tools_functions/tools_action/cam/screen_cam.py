import cv2
import os
import time

from CONFIG import LANGUAGE, CAM_INDEX_USE
from configuration.select_cam import set_video_device


def screen_with_cam():
    global CAM_INDEX_USE 
    if CAM_INDEX_USE is None:
        set_video_device()
        with open('CONFIG.py', 'r') as file:
            for line in file:
                if line.startswith('CAM_INDEX_USE'):
                    CAM_INDEX_USE = line.split('=')[1].strip()

    if not os.path.exists('photos'):
        os.makedirs('photos')

    cap = cv2.VideoCapture(int(CAM_INDEX_USE))
    ret, frame = cap.read()
    time.sleep(1)
    cv2.imwrite('photos/camera.png', frame)
    cap.release()
    return "Screen de la caméra effectué" if LANGUAGE == 'fr' else "Camera screen taken"