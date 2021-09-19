from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from tqdm import tqdm

from numpy import dot
from numpy.linalg import norm

model = SentenceTransformer('sentence-transformers/paraphrase-MiniLM-L6-v2')

def cos_sim(a,b):
    a = a.reshape((-1,))
    b = b.reshape((-1,))
    cos_sim = dot(a, b)/(norm(a)*norm(b))
    return cos_sim

def match(model, s1, s2):
    #create model once and pass in as parameter as the time to do initialize model is a lot
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
    
