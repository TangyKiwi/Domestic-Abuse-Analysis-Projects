from pyannote.audio import Pipeline
from pydub import AudioSegment
import os
pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization")


def split_diarize_audio(file, name):
    audio = AudioSegment.from_file(file, format="wav")
    splices = audio[::30000]
    i = 0
    for splice in splices:
        file = "Audio/" + name + "_chunk{0}.wav".format(i)
        splice.export(file, bitrate ='16k', format ="wav")
        # apply pretrained pipeline
        diarization = pipeline("Audio/" + name + "_chunk{0}.wav".format(i))

        # print the result
        for turn, _, speaker in diarization.itertracks(yield_label=True):
            print(f"start={turn.start:.1f}s stop={turn.end:.1f}s speaker_{speaker}")
        i += 1

    for i in range(i - 1, -1, -1):
        os.remove("Audio/" + name + "_chunk{0}.wav".format(i))


split_diarize_audio("Audio/nypd_weinstein.wav", "nypd_weinstein")

# start=2.5s stop=5.2s speaker_SPEAKER_02
# start=5.6s stop=6.2s speaker_SPEAKER_02
# start=6.2s stop=7.2s speaker_SPEAKER_00
# start=7.2s stop=7.4s speaker_SPEAKER_05
# start=7.4s stop=8.0s speaker_SPEAKER_00
# start=8.0s stop=9.4s speaker_SPEAKER_05
# start=9.4s stop=9.4s speaker_SPEAKER_00
# start=9.4s stop=9.4s speaker_SPEAKER_05
# start=9.4s stop=9.9s speaker_SPEAKER_00
# start=13.5s stop=17.3s speaker_SPEAKER_04
# start=16.0s stop=21.7s speaker_SPEAKER_03
# start=21.7s stop=29.4s speaker_SPEAKER_01
# start=29.4s stop=29.5s speaker_SPEAKER_03
# start=0.5s stop=1.0s speaker_SPEAKER_00
# start=1.0s stop=7.0s speaker_SPEAKER_01
# start=7.0s stop=15.1s speaker_SPEAKER_00
# start=15.1s stop=18.8s speaker_SPEAKER_01
# start=18.8s stop=26.6s speaker_SPEAKER_00
# start=26.6s stop=29.2s speaker_SPEAKER_01
# start=29.2s stop=29.4s speaker_SPEAKER_00
# start=29.4s stop=29.4s speaker_SPEAKER_01
# start=29.4s stop=29.5s speaker_SPEAKER_00