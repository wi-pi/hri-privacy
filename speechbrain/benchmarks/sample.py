from speechbrain.pretrained import SpeakerRecognition
import os
from speechbrain.dataio.dataio import read_audio

def check(verification, f1, f2):

    #f1 = read_audio(f1).squeeze()
    #f2 = read_audio(f2).squeeze()
    score, prediction = verification.verify_files(f1,f2)
    #"speechbrain/spkrec-ecapa-voxceleb/example1.wav", "speechbrain/spkrec-ecapa-voxceleb/example2.flac")

    print(prediction, score)


if __name__ == "__main__":
    verification = SpeakerRecognition.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb", savedir="pretrained_models/spkrec-ecapa-voxceleb")
    path = "/mnt/b/varun/audio_data/Voxceleb/VoxCeleb1/wav/id10001/"
    dirs = os.listdir(path)
    files = []
    for dir in dirs:
        dir_path = os.path.join(path, dir)
        t = os.listdir(dir_path)
        t1 = [dir_path + '/' + i for i in t]
        files.extend(t1)

    n = len(files)
    for i in range(0, n):
        for j in range(i+1, n):
            print(files[i], files[j])
            check(verification, files[i], files[j])
