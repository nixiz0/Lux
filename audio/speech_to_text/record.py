import sounddevice as sd
import wave
import numpy as np
import os
import collections

from constant.colors import *
from CONFIG import *


def record_audio(language=LANGUAGE, filename=TEMP_AUDIO_PATH, device_index=MIC_INDEX,
                 rate=AUDIO_RATE, chunk=AUDIO_CHUNK, threshold=AUDIO_THRESHOLD, pre_recording_buffer_length=AUDIO_BUFFER_LENGTH):
    
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))

    print(f"{CYAN}Écoute..{RESET}" if language == 'fr' else f"{CYAN}Listen..{RESET}")
    frames = collections.deque(maxlen=int(rate / chunk * pre_recording_buffer_length))  # buffer to store 2 seconds of audio
    recording_frames = []
    recording = False
    silence_count = 0

    def callback(indata, frame_count, time_info, status):
        nonlocal recording, silence_count, frames, recording_frames
        if status:
            print(status)
        rms = np.linalg.norm(indata) / np.sqrt(len(indata))
        frames.append(indata.copy())
        if rms >= threshold:
            if not recording:  # start recording
                recording = True
                recording_frames.extend(frames)  # add the buffered audio
            silence_count = 0
        elif recording and rms < threshold:
            silence_count += 1
            if silence_count > rate / chunk * 2:  # if 2 seconds of silence, stop recording
                raise sd.CallbackStop
        if recording:
            recording_frames.append(indata.copy())

    with sd.InputStream(samplerate=rate, channels=1, dtype='int16', callback=callback, device=device_index, blocksize=chunk):
        while True:
            sd.sleep(int(1000 * chunk / rate))  # sleep for the duration of one chunk
            if recording and silence_count > rate / chunk * 2:
                break  # exit the loop if recording has stopped due to silence

    # Only create the file if there is audio data
    if recording_frames:
        print(f"{YELLOW}Transcription en cours..{RESET}" if language == 'fr' else f"{YELLOW}Transcription in progress..{RESET}")
        wf = wave.open(filename, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 2 bytes for int16
        wf.setframerate(rate)
        wf.writeframes(b''.join(recording_frames))
        wf.close()
        return True
    else:
        print(f"{RED}Pas d'audio détecté{RESET}" if language == 'fr' else f"{RED}No audio detected.{RESET}")
        return False
