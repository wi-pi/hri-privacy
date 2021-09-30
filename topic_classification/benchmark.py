from natural_language import Google_NLP
#from convert_topics import CONVERT
import argparse
import os
import csv
import numpy as np
from tqdm import tqdm

CONVERT = {'yahoo_answers': {'People & Society': ['Society & Culture', 'Family & Relationships'], 'Science': ['Science & Mathematics'], 'Health': ['Health'], 'Jobs & Education': ['Education & Reference'], 'Books & Literature': ['Education & Reference'], 'Computers & Electronics': ['Computers & Internet'], 'Sports': ['Sports'], 'Finance': ['Business & Finance'], 'Business & Industrial': ['Business & Finance'], 'Arts & Entertainment': ['Entertainment & Music'], 'Law & Government': ['Politics & Government']}}

def parse(blob):
    elements = blob.split("\n")
    names = []
    confidences = []
    for e in elements:
        if "name" in e:
            t = e.split('/')[1].replace('"','')
            #print(e, t)
            names.append(t)
            #e.strip().split(':')[1].replace('"','').replace('/',' ').replace('\\',''))
        if "confidence" in e:
            confidences.append(float(e.strip().split(':')[1]))

    #print(names, confidences)
    return names, confidences

def iterate_through(dataset, dataset_name, classes, inv_classes, confusion_matrix, label_counts):
    vals = []
    d = CONVERT[dataset_name]
    keys = list(d.keys())
    for k in keys:
        vals.append(d[k][0])

    for _, data in tqdm(enumerate(dataset)):
        nlp = Google_NLP(data[1], verbose=False)
        inferred_topic = str(nlp.get_topic())
        infer_topics, confidences = parse(inferred_topic)
        source_topic = classes[int(data[0])]
        n = len(infer_topics)
        l = data[2]
        for i in range(n):
            infer_topic = infer_topics[i]
            confidence = confidences[i]
            if infer_topic not in inv_classes:
                n = len(vals)
                #print("1:", int(data[0]), n)
                confusion_matrix[int(data[0])][n-1] += 1
            else:
                infer_idx = inv_classes[infer_topic]
                #print("2:",int(data[0]), infer_idx)
                confusion_matrix[int(data[0])][infer_idx] += 1
    
    keys = sorted(list(label_counts.keys()))
    for k in keys:
        v = label_counts[k]
        confusion_matrix[k,:] = confusion_matrix[k,:]/v

    print(confusion_matrix)

    return confusion_matrix

def flip(p):
    import random
    return True if random.random() < p else False

def topic(data_path):
    classes = {}
    inv_classes = {}
    label_counts = {}

    dataset_name = data_path.split('/')[-1]

    with open(os.path.join(data_path, 'classes.txt'), 'r') as infile:
        i = 0
        for line in infile:
            t = line.strip()
            classes[i] = t
            inv_classes[t] = i
            i = i + 1

    confusion_matrix = np.zeros((i,i+1))

    with open(os.path.join(data_path, 'test.csv'), 'r') as infile:
        reader = csv.reader(infile)
        data = []
        for row in reader:
            text = ''
            label = int(row[0]) - 1
            for i in range(1, len(row)):
                text += row[i]
            elements = text.split(' ')
            if len(elements) > 50:
                if flip(0.15) == True:
                    label = int(label)
                    data.append((label, text, len(elements)))
                    if label not in label_counts:
                        label_counts[label] = 1
                    else:
                        label_counts[label] += 1
   
    iterate_through(data, dataset_name, classes, inv_classes, confusion_matrix, label_counts)


if __name__ == "__main__":
    data_path = "/nobackup/varun/robot/hri-privacy/topic_classification/yahoo_answers"
    topic(data_path)


