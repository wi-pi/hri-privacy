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


classifier = EncoderClassifier.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb", savedir="pretrained_models/spkrec-ecapa-voxceleb")

def create_embedding(classifier, fil):
    try:
        signal, fs = torchaudio.load(fil)
    except:
        print("torch audio issue")
        return None
    emb = classifier.encode_batch(signal)
    
    #manually clear links
    files = os.listdir('.')
    audio_files = []
    for f in files:
        if 'wav' in f:
            audio_files.append(f)

    for f in audio_files:
        os.unlink(f)
    
    e = emb.cpu().detach().numpy()
    e = e.reshape((1, -1))
    return emb

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
            if 'wav' in name:
                files.append(name + "\n")
                #print(name)
        '''
        tmp_fils = os.listdir(name)
        tmp_files = [name+'/'+i for i in tmp_fils]
        files.extend(tmp_files)
        '''
    files2 = []
    for f in files:
        if 'wav' in f:
            files2.append(f)

    print(len(files2))
    return files2

def save_file(array, i):
    f_name = 'output/'+str(i)+'.npy'
    f = open(f_name, 'w')
    np.save(f_name, array)
    print("saving to:", f_name)
    f.close()

if __name__ == "__main__":
    path = "/mnt/b/varun/audio_data/Voxceleb/VoxCeleb1/wav"
    files = obtain_files(path)
    f = open('filenames.txt', 'w')
    flag = False
    '''
    n = len(files)
    batch_size = 20
    num_batches = int(n/batch_size)
    for i in range(num_batches):
        start = i * batch_size
        if i != num_batches - 1:
            end = start + batch_size
        else:
            end = n
        fil2 = files[start:end]
        fil = [str(f.strip()) for f in fil2]
    '''
    for i, fil in enumerate(files):
        fil = str(fil.strip())
        #print(str(fil))
        #exit()
        e = create_embedding(classifier, fil)
        #e = 1
        if e != None:
            f.write(fil + "\n")
            if i == 0 or flag == True:
                final = e
                flag = False
            else:
                final = np.vstack((final, e))

        if (i != 0 and i % 5000 == 0) or i == len(files)-1:
            save_file(final, i)
            flag = True
    f.close()

#emb = verification.encode_batch("speechbrain/spkrec-ecapa-voxceleb/example1.wav")
#print(emb)

