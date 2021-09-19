from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from tqdm import tqdm

d = {'NEUTRAL':1, 'CONTRADICTION':0, 'ENTAILMENT':1}

from numpy import dot
from numpy.linalg import norm

def cos_sim(a,b):
    a = a.reshape((-1,))
    b = b.reshape((-1,))
    cos_sim = dot(a, b)/(norm(a)*norm(b))
    return cos_sim

def match(model, s1, s2):
    from scipy import spatial
    embedding1 = model.encode(s1).reshape((-1,1))
    embedding2 = model.encode(s2).reshape((-1,1))

    #e1 = list(embedding1)
    #e2 = list(embedding2)

    e1 = embedding1
    e2 = embedding2

    cs = cos_sim(e1, e2)
    #cos_sim = 1 - spatial.distance.cosine(e1, e2)
    #cos_sim = cosine_similarity(embedding1, embedding2)
    #print(cos_sim)
    return cs

def get_sentence_pairs(path):
    f = open(path, "r")
    lines = f.readlines()
    lines = lines[1:]
    pairs = []
    labels = []
    sem_scores = []
    for l in lines:
        e = l.split('\t')
        pair = (e[1], e[2])
        label = e[3]
        sem_score = float(e[4])
        pairs.append(pair)
        labels.append(d[label])
        ss = 1 if sem_score >= 2.5 else 0
        sem_scores.append(ss)

    return pairs, labels, sem_scores
    
def save(scores, labels, sem_scores):
    scores = np.asarray(scores)
    labels = np.asarray(labels)
    sem_scores = np.asarray(sem_scores)
    np.save("scores.npy", scores)
    np.save("labels.npy", labels)
    np.save("sem_scores.npy", sem_scores)

def plot_roc(label_file = "labels.npy"):
    scores = np.load("scores.npy")
    n = scores.shape[0]
    import seaborn as sns
    scores = list(scores)
    print(min(scores), max(scores))
    labels = list(np.load(label_file))
    import sklearn.metrics as metrics
    fpr, tpr, threshold = metrics.roc_curve(labels, scores)
    #write_to_file(fpr, tpr, threshold, "roc.txt")
    roc_auc = metrics.auc(fpr, tpr)

    import matplotlib.pyplot as plt
    plt.clf()
    sns.set_style("darkgrid")
    #plt.title('Receiver Operating Characteristic')
    plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
    plt.legend(loc = 'lower right')
    plt.legend(frameon=False)
    plt.plot([0, 1], [0, 1],'r--')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    if "labels" in label_file:
        plt.savefig("figures/labels_roc.png")
    else:
        plt.savefig("figures/sem_scores_roc.png")



if __name__ == "__main__":

    '''
    path = "/u/c/h/chandrasekaran/Desktop/huggingface/SICK.txt"
    sentence_pairs, labels, sem_scores = get_sentence_pairs(path)
    model = SentenceTransformer('sentence-transformers/paraphrase-MiniLM-L6-v2')
    n = len(sentence_pairs)
    cs_list = []
    for i, pair in tqdm(enumerate(sentence_pairs)):
        label = labels[i]
        s1 = pair[0]
        s2 = pair[1]
        cs = match(model, s1, s2)
        cs_list.append(cs)

    save(cs_list, labels, sem_scores)
    '''
    plot_roc()
    plot_roc("sem_scores.npy")

    #print(cs.shape)
