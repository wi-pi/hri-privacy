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
            if 'wav' in name:
                files.append(name + "\n")
    
    files2 = []
    for f in files:
        if 'wav' in f:
            files2.append(f)

    print(len(files2))
    return files2

def check(verification, f1, f2):

    #f1 = read_audio(f1).squeeze()
    #f2 = read_audio(f2).squeeze()
    score, prediction = verification.verify_files(f1,f2)
    #"speechbrain/spkrec-ecapa-voxceleb/example1.wav", "speechbrain/spkrec-ecapa-voxceleb/example2.flac")

    score = score.cpu().detach().numpy()
    return (score, prediction)



def get_stats(d):
    from numpy import median
    keys = list(d.keys())
    l = []
    for k in keys:
        l.append(len(d[k]))

    print("mean:", sum(l)/len(l))
    min_val = min(l)
    print("min:", min_val)
    median = int(median(l))
    print("median:", median)
    from math import comb
    median = int(median)
    min_val = int(min_val/9)
    output = len(keys) * comb(min_val, 2)
    print("combinations:", output)
    return output

def get_intra_pair(d):
    import random
    keys = list(d.keys())
    rand_key = random.choice(keys)
    vals = d[rand_key]
    f1 = random.choice(vals)
    f2 = random.choice(vals)
    return f1, f2

def get_inter_pair(d):
    import random
    keys = list(d.keys())
    rand_key1 = random.choice(keys)
    rand_key2 = random.choice(keys)
    while rand_key1 == rand_key2:
        rand_key2 = random.choice(keys)
    vals1 = d[rand_key1]
    vals2 = d[rand_key2]
    f1 = random.choice(vals1)
    f2 = random.choice(vals2)
    return f1, f2

def main():
    path = "/Users/briantang/Desktop/robot/hri-privacy/data/wav" 
    verification = SpeakerRecognition.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb", savedir="pretrained_models/spkrec-ecapa-voxceleb")
    files = obtain_files(path)

    d = {}
    for f in files:
        f = f.strip()
        e = f.split("/")
        id = e[-3]
        if id not in d:
            d[id] = [f]
        else:
            d[id].append(f)
        

    output = get_stats(d)
   
    labels = []
    scores = []

    #output = 100
    
    for i in tqdm(range(output)):
        f1, f2 = get_intra_pair(d)
        #print(f1, f2)
        score, _ = check(verification, f1, f2)
        print(score)
        scores.append(score[0])
        labels.append(1)
        f1, f2 = get_inter_pair(d)
        score, _ = check(verification, f1, f2)
        print(score)
        scores.append(score[0])
        labels.append(0)
        #print(f1, f2)

    sc_array = np.asarray(scores)
    labels_array = np.asarray(labels)

    np.save("scores.npy", sc_array)
    np.save("labels.npy", labels_array)

def plot_roc():
    scores = np.load("scores.npy")
    n = scores.shape[0]
    scores = list(scores)
    labels = list(np.load("labels.npy"))
    import sklearn.metrics as metrics
    print(scores)
    print(labels)
    fpr, tpr, threshold = metrics.roc_curve(labels, scores)
    # for f, tp, th in zip(fpr, tpr, threshold):
        # print(f, tp, th)
    # print(fpr)
    roc_auc = metrics.auc(fpr, tpr)

    import matplotlib.pyplot as plt
    plt.title('Receiver Operating Characteristic')
    plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
    plt.legend(loc = 'lower right')
    plt.plot([0, 1], [0, 1],'r--')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.savefig("brian_roc.png")

    '''
    scores.sort()
    for i in range(n):
        thresh = scores[i]
        out = list(np.where(scores >= thresh, 1, 0))
    '''

def custom_plot_roc():
    t_scores = np.load("scores.npy")
    scores = np.load("scores.npy")
    n = scores.shape[0]
    t_scores = list(t_scores)
    y_true = np.load("labels.npy")
    print(y_true)
    exit()
    t_scores.sort()
    print(len(t_scores))
    fpr = []
    tpr = []
    for score in t_scores:
        y_pred = np.where(scores >= score, 1, 0)

        fp = np.sum((y_pred == 1) & (y_true == 0))
        tp = np.sum((y_pred == 1) & (y_true == 1))

        fn = np.sum((y_pred == 0) & (y_true == 1))
        tn = np.sum((y_pred == 0) & (y_true == 0))

        fpr.append(fp / (fp + tn))
        tpr.append(tp / (tp + fn))

    import matplotlib.pyplot as plt
    plt.title('Receiver Operating Characteristic')
    plt.plot(fpr, tpr, 'b')
    #label = 'AUC = %0.2f' % roc_auc)
    plt.legend(loc = 'lower right')
    plt.plot([0, 1], [0, 1],'r--')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.savefig("brian_roc2.png")


if __name__ == "__main__":
    # main()
    plot_roc()
    # custom_plot_roc()
