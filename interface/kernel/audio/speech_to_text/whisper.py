import torch
import string
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline


punctuation_keep = "".join([char for char in string.punctuation if char not in ["'", '"', "-"]])
translator = str.maketrans('', '', punctuation_keep)

class SpeechToText:
    def __init__(self):
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
        # Transcribe Speech to Text
        results = self.pipe(audio_output)
        results = results['text'].lower()
        results = results.replace('-', ' ')
        results = results.translate(translator)
        results = results.strip()
        return results
    