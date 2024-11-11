import torch
import string
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline


punctuation_keep = "".join([char for char in string.punctuation if char not in ["'", '"', "-"]])
translator = str.maketrans('', '', punctuation_keep)

class SpeechToText:
    """
    A class to handle speech-to-text transcription using a pre-trained Whisper model.

    Attributes:
    device (str): The device to run the model on (GPU if available, otherwise CPU).
    torch_dtype (torch.dtype): The data type for the model (float16 if GPU is available, otherwise float32).
    model_id (str): The identifier for the pre-trained Whisper model.
    model (AutoModelForSpeechSeq2Seq): The pre-trained Whisper model for speech-to-text.
    processor (AutoProcessor): The processor for the Whisper model.
    pipe (pipeline): The pipeline for automatic speech recognition.
    """

    def __init__(self):
        """
        Initializes the SpeechToText class, setting up the model, processor, and pipeline for speech-to-text transcription.
        """
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

        self.model_id = "openai/whisper-large-v3"
        self.model = AutoModelForSpeechSeq2Seq.from_pretrained(
            self.model_id, torch_dtype=self.torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
        )
        self.model.to(self.device)
        self.processor = AutoProcessor.from_pretrained(self.model_id)

        self.pipe = pipeline(
            "automatic-speech-recognition",
            model=self.model,
            tokenizer=self.processor.tokenizer,
            feature_extractor=self.processor.feature_extractor,
            max_new_tokens=128,
            chunk_length_s=30,
            batch_size=64,
            return_timestamps=True,
            torch_dtype=self.torch_dtype,
            device=self.device,
        )

    def transcribe(self, audio_output):
        """
        Transcribes the given audio output to text.

        Parameters:
        audio_output (str): The path to the audio file to be transcribed.

        Returns:
        str: The transcribed text.
        """
        # Transcribe Speech to Text
        results = self.pipe(audio_output)
        results = results['text'].lower()
        results = results.replace('-', ' ')
        results = results.translate(translator)
        results = results.strip()
        return results
    