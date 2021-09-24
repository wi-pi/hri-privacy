import os
import numpy as np

def load_arrays(path):
    labels = list(np.load(os.path.join(path, "labels.npy")))
    scores = list(np.load(os.path.join(path, "scores.npy")))
    return labels, scores

def load_pairs(path):
    f = open(os.path.join(path, 'pairs.txt'))
    lines = f.readlines()
    pairs = []
    for line in lines:
        line = line.strip()
        e = tuple(line.split(' '))
        f1 = e[0]
        f2 = e[1]
        f1_split = f1.split('/')
        f2_split = f2.split('/')
        id1 = f1_split[-3]
        id2 = f2_split[-3]
        pairs.append((id1,id2,f1,f2))
    return pairs
        

def print_stats(labels, scores, path_pairs, thresh):
    n = len(labels)
    assert n == len(scores)
    assert n == len(path_pairs)
    for i in range(n):
        if scores[i] >= thresh:
            if labels[i] == 0:
                print(path_pairs[i])
            '''
            truth = int(path_pairs[i][0] == path_pairs[i][1])
            if truth != labels[i]:
                print("whammy")
            '''
if __name__ == "__main__":
    path = "/u/c/h/chandrasekaran/Desktop/speechbrain/vc1"
    labels, scores = load_arrays(path)
    path_pairs = load_pairs(path)
    thresh = 0.99
    print_stats(labels, scores, path_pairs, thresh)
