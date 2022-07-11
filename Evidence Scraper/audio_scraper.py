# Wav2Vec audio transcription
import librosa
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer

tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

def wav2vec_audio(file, name):
    audio, rate = librosa.load(file, sr = 16000)
    input_values = tokenizer(audio, return_tensors="pt").input_values
    logits = model(input_values).logits
    prediction = torch.argmax(logits, dim=-1)
    with open("Data/w2v_" + name + ".txt", "w") as f:
        f.write(tokenizer.batch_decode(prediction)[0])


wav2vec_audio("Audio/farrow_weinstein1.wav", "farrow_weinstein1")
wav2vec_audio("Audio/farrow_weinstein2.wav", "farrow_weinstein2")


# Speech Recognition Library
# https://github.com/Uberi/speech_recognition#readme
import speech_recognition as sr
r = sr.Recognizer()


def sr_audio(file, name):
    with sr.AudioFile(file) as source:
        audio = r.record(source)
        with open("Data/sr_" + name + ".txt", "w") as f:
            f.write(r.recognize_google(audio))


sr_audio("Audio/farrow_weinstein1.wav", "farrow_weinstein1")
sr_audio("Audio/farrow_weinstein2.wav", "farrow_weinstein2")


# pydub to manipulate audio files
# https://github.com/jiaaro/pydub
from pydub import AudioSegment
import os # for file cleanup
import speech_recognition as sr
r = sr.Recognizer()


def split_audio(file, name):
    audio = AudioSegment.from_file(file, format="wav")
    splices = audio[::30000] # 30 second splices
    i = 0
    for splice in splices:
        file = "Audio/" + name + "_chunk{0}.wav".format(i)
        splice.export(file, bitrate ='192k', format ="wav")
        with sr.AudioFile(file) as source:
            audio = r.record(source)
            with open("Data/sr_" + name + ".txt", "a") as f:
                f.write(r.recognize_google(audio) + " ")

        i += 1

    # to remove all chunks
    for i in range(i - 1, -1, -1):
        os.remove("Audio/" + name + "_chunk{0}.wav".format(i))


split_audio("Audio/nypd_weinstein.wav", "nypd_weinstein")