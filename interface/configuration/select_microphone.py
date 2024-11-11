import streamlit as st
import sounddevice as sd
from CONFIG import LANGUAGE
from configuration.update_config import update_config


def set_micro():
    """
    Configures the microphone for the application.
    """
    devices = sd.query_devices()
    valid_devices = [(i, device['name']) for i, device in enumerate(devices) if device['max_input_channels'] > 0 and device['hostapi'] == 0]

    if not valid_devices:
        st.error("Aucun périphérique d'entrée actif trouvé." if LANGUAGE == 'fr' else "No active input devices found.")
        return None

    device_names = [device[1] for device in valid_devices]
    selected_device_name = st.selectbox("Choisissez le microphone" if LANGUAGE == 'fr' else "Choose the microphone", device_names, key='selectbox_micro')
    selected_device_index = next(index for index, name in valid_devices if name == selected_device_name)

    if st.button("Mettre à jour" if LANGUAGE == 'fr' else "Update", key='btn_set_micro'):
        update_config('MIC_INDEX', selected_device_index)
        st.success(f"Microphone mis à jour en {selected_device_index}" if LANGUAGE == 'fr' else f"Microphone updated to {selected_device_index}")
        return selected_device_index