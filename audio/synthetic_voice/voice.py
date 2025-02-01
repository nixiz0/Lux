import re
import os
import comtypes
comtypes.CoInitialize()
import pyttsx3
import soundfile as sf
import sounddevice as sd
from CONFIG import NARRATOR_VOICE, TEMP_OUTPUT_VOICE_PATH


def split_text_and_code(text):
    # Define a regex pattern for code detection
    pattern = r'(```.*?```)'  # This pattern matches text within triple backticks
    
    # Use regex split to separate text and code
    segments = re.split(pattern, text, flags=re.DOTALL)
    
    return segments

class LuxVoice:
    def __init__(self):
        self.engine = pyttsx3.init()
            
    def speak(self, text):
        # Split the text into text and code segments
        segments = split_text_and_code(text)

        for segment in segments:
            # Check if the segment is code
            if segment.startswith('```') and segment.endswith('```'):
                pass
            else:   
                # Create the directory if it doesn't exist
                os.makedirs(os.path.dirname(TEMP_OUTPUT_VOICE_PATH), exist_ok=True)

                # If the file already exists, remove it
                if os.path.exists(TEMP_OUTPUT_VOICE_PATH):
                    os.remove(TEMP_OUTPUT_VOICE_PATH)

                # Set narrator voice
                self.engine.setProperty('voice', NARRATOR_VOICE)

                # Convert text to speech and save it to a file
                self.engine.save_to_file(segment, TEMP_OUTPUT_VOICE_PATH)

                # Wait for any pending speech to complete
                self.engine.runAndWait()

                # Play the saved audio file using sounddevice and soundfile
                audio_data, samplerate = sf.read(TEMP_OUTPUT_VOICE_PATH, dtype='int16')
                sd.play(audio_data, samplerate)
                sd.wait()