import os
import re
import queue
import threading
import soundfile as sf
import sounddevice as sd
import torch
from TTS.api import TTS

from CONFIG import *


class LuxVoice:
    """
    A class to handle voice synthesis and playback using a TTS model.

    Attributes:
    device (str): The device to run the TTS model on (GPU if available, otherwise CPU).
    tts (TTS): The TTS model for voice cloning.
    audio_queue (queue.Queue): A queue to manage audio files to be played.
    lock (threading.Lock): A lock to prevent multiple threads from accessing shared resources.
    playing_event (threading.Event): An event to control the audio playback thread.
    """

    def __init__(self):
        """
        Initializes the LuxVoice class, setting up the TTS model, device, and necessary directories and queues.
        """
        # Use GPU if available, otherwise use CPU
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"

        # Import the xtts model for voice cloning
        self.tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

        # Move the model to the detected device
        self.tts.to(self.device)

        # Create the folder for storing generated voices (sentence segments)
        if not os.path.exists(os.path.dirname(TEMP_OUTPUT_VOICE_PATH)):
            os.makedirs(os.path.dirname(TEMP_OUTPUT_VOICE_PATH))

        # Create a queue for audio to be played
        self.audio_queue = queue.Queue()

        # Lock a thread to prevent opening another one
        self.lock = threading.Lock()

        # Event to play the audio
        self.playing_event = threading.Event()

    # Function to play the audio
    def play_audio(self):
        """
        Continuously plays audio files from the queue until a None value is encountered.
        """
        while True:
            file_path = self.audio_queue.get()
            if file_path is None:
                break

            # Read the audio file
            data, samplerate = sf.read(file_path, dtype='float32')

            # Play the filtered audio data
            sd.play(data, samplerate)
            sd.wait()  # Wait until the file is done playing

            self.audio_queue.task_done()
            os.remove(file_path)

        self.playing_event.clear()

    def speak(self, user_text, language=LANGUAGE, speed=SPEED_VOICE):
        """
        Converts the given text to speech and plays it.

        Parameters:
        user_text (str): The text to be converted to speech.
        language (str): The language of the text.
        speed (float): The speed of the speech.
        """
        if user_text is None:
            return

        # Split sentences
        sentences = re.split(r'(?<=[.!?]) +', user_text)
        segments = []
        current_segment = ""

        # Group sentences into segments
        for sentence in sentences:
            # Remove periods after splitting
            sentence = sentence.replace('.', '')
            if len(current_segment) + len(sentence) < 400:
                current_segment += sentence + " "
            else:
                # If a single sentence is too long, split it into smaller parts
                if len(sentence) >= 400:
                    words = sentence.split()
                    temp_segment = ""
                    for word in words:
                        if len(temp_segment) + len(word) < 400:
                            temp_segment += word + " "
                        else:
                            segments.append(temp_segment.strip())
                            temp_segment = word + " "
                    if temp_segment:
                        segments.append(temp_segment.strip())
                else:
                    segments.append(current_segment.strip())
                    current_segment = sentence + " "
        
        if current_segment:
            segments.append(current_segment.strip())

        # Filter out code segments
        segments = [seg for seg in segments if not (seg.startswith('```') and seg.endswith('```'))]

        # Start the audio playback thread if not already started
        if not self.playing_event.is_set():
            self.playing_event.set()
            threading.Thread(target=self.play_audio, daemon=True).start()

        # Generate and queue the audio segments
        for i, segment in enumerate(segments):
            temp_file_path = f"{TEMP_OUTPUT_VOICE_PATH}_{i}.wav"
            self._speak(segment, temp_file_path, AUDIO_VOICE_PATH, language, speed)

            with self.lock:
                self.audio_queue.put(temp_file_path)
    
    def _speak(self, user_text, file_path, speaker_wav, language, speed):
        """
        Generates an audio file from the given text using the TTS model.

        Parameters:
        user_text (str): The text to be converted to speech.
        file_path (str): The path to save the generated audio file.
        speaker_wav (str): The path to the speaker's voice file for cloning.
        language (str): The language of the text.
        speed (float): The speed of the speech.
        """
        # Generate the audio file from the text
        self.tts.tts_to_file(text=user_text, 
                             file_path=file_path,
                             speaker_wav=speaker_wav,
                             language=language,
                             split_sentences=True,
                             speed=speed
                            )