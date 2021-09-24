'''
from speechbrain.pretrained import SpeakerRecognition

verification = SpeakerRecognition.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb", savedir="pretrained_models/spkrec-ecapa-voxceleb")
f1 = "/mnt/b/varun/audio_data/Voxceleb/VoxCeleb1/wav/id10001/1zcIwhmdeo4/00001.wav"
f2 = "/mnt/b/varun/audio_data/Voxceleb/VoxCeleb1/wav/id10001/1zcIwhmdeo4/00002.wav"
#score, prediction = verification.verify_files("speechbrain/spkrec-ecapa-voxceleb/example1.wav", "speechbrain/spkrec-ecapa-voxceleb/example2.flac")
score, prediction = verification.verify_files(f1, f2)

print(prediction, score)
'''

from speechbrain.pretrained import EncoderClassifier
import torchaudio
import os
from tqdm import tqdm
import numpy as np


os.environ["CUDA_VISIBLE_DEVICES"]="1"


#classifier = EncoderClassifier.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb", savedir="pretrained_models/spkrec-ecapa-voxceleb")

verification = SpeakerRecognition.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb", savedir="pretrained_models/spkrec-ecapa-voxceleb")

def check(verification, f1, f2):

    score, prediction = verification.verify_files(f1,f2)

    #manually clear links
    files = os.listdir('.')
    audio_files = []
    for f in files:
        if 'wav' in f:
            audio_files.append(f)

    for f in audio_files:
        os.unlink(f)

    score = score.cpu().detach().numpy() #this is the cosine similarity b/w 2 files; inputs should be pre-processed s.t. they are in .wav format
    return (score, prediction)


