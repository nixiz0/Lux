import streamlit as st
import cv2
from CONFIG import LANGUAGE
from configuration.update_config import update_config


def list_video_devices():
    """
    Lists all available video capture devices.

    Iterates through possible video capture device indices and checks if they are available.
    Returns a list of tuples containing the index and name of each available device.

    Returns:
    list: A list of tuples where each tuple contains the index and name of a video capture device.
    """
    index = 0
    devices = []
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            devices.append((index, f"Caméra {index}"))
        cap.release()
        index += 1
    return devices

def set_video_device():
    """
    Sets the video capture device for the application.

    Lists available video devices and allows the user to select one. Provides options to test the selected device
    and update the configuration with the selected device index.

    Returns:
    int or None: The index of the selected video capture device, or None if no devices are found.
    """
    devices = list_video_devices()
    if not devices:
        st.error("Aucun périphérique de capture vidéo trouvé." if LANGUAGE == 'fr' else "No video capture devices found.")
        return None

    device_names = [device[1] for device in devices]
    selected_device_name = st.selectbox("Choisissez la caméra" if LANGUAGE == 'fr' else "Choose the camera", device_names, key='video_select')
    selected_device_index = next(index for index, name in devices if name == selected_device_name)

    if st.button("Tester la caméra" if LANGUAGE == 'fr' else "Test the camera", key='test_video'):
        cap = cv2.VideoCapture(selected_device_index)
        ret, frame = cap.read()
        if ret:
            st.image(frame, channels="BGR")
        else:
            st.error("Impossible de lire la caméra sélectionnée." if LANGUAGE == 'fr' else "Unable to read the selected camera.")
        cap.release()

    if st.button("Mettre à jour la caméra" if LANGUAGE == 'fr' else "Update the camera", key='update_video'):
        update_config('CAM_INDEX_USE', selected_device_index)
        st.success(f"Caméra mise à jour en {selected_device_index}" if LANGUAGE == 'fr' else f"Camera updated to {selected_device_index}")
        return selected_device_index