from speechbrain.pretrained import SpeakerRecognition
import os
from speechbrain.dataio.dataio import read_audio
from tqdm import tqdm
import numpy as np

def obtain_files(path):
    import glob
    sub_dirs = []
    files = []
    for name in glob.glob(path+'/*'):
        sub_dirs.append(name)

    sub_sub_dirs = []
    for sub_dir in sub_dirs:
        for name in glob.glob(sub_dir + '/*'):
            sub_sub_dirs.append(name)

    for sub_sub_dir in sub_sub_dirs:
        for name in glob.glob(sub_sub_dir + '/*'):
            #if 'wav' in name:
            if 'm4a' in name:
                files.append(name + "\n")
    
    files2 = []
    for f in files:
        #if 'wav' in f:
        if 'm4a' in f:
            files2.append(f)

    print(len(files2))
    return files2


def gen_shell(files):
    f = open("convert.sh", "w")
    for inp in files:
        inp = inp.strip()
        out = inp.replace("m4a", "wav")
        st = "ffmpeg -i "+inp+" "+out+"\n"
        f.write(st)
    f.close()


if __name__ == "__main__":
    path = "/mnt/b/varun/audio_data/Voxceleb/VoxCeleb2/dev/aac"
    files = obtain_files(path)
    gen_shell(files)
