import librosa
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer

tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

def process_audio(file, name):
    audio, rate = librosa.load(file, sr = 16000)
    input_values = tokenizer(audio, return_tensors="pt").input_values
    logits = model(input_values).logits
    prediction = torch.argmax(logits, dim=-1)
    with open("Data/" + name + ".txt", "w") as f:
        f.write(tokenizer.batch_decode(prediction)[0])

process_audio("Audio/farrow_weinstein1.wav", "farrow_weinstein1")
process_audio("Audio/farrow_weinstein2.wav", "farrow_weinstein2")
