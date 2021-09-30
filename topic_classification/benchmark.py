from natural_language import Google_NLP
from convert_topics import CONVERT
import argparse
import os
import csv


def parse(blob):
    elements = blob.split("\n")
    names = []
    confidences = []
    for e in elements:
        if "name" in e:
            names.append(e.strip())
        if "confidence" in e:
            confidences.append(e.strip())

    print(names, confidences)
    return names, confidences

def iterate_through(dataset, dataset_name, classes, inv_classes, confusion_matrix):
    vals = []
    d = CONVERT[dataset_name]
    keys = list(d.keys())
    for k in keys:
        vals.append(d[k])

    for data in dataset:
        nlp = Google_NLP(data[1], verbose=False)
        inferred_topic = str(nlp.get_topic())
        infer_topics, confidence = parse(inferred_topic)
        source_topic = classes[int(data[0])]
        n = len(infer_topics)
        for i in range(n):
            infer_topic = infer_topics[i]
            confidence = confidences[i]
            infer_idx = inv_classes[infer_topic]
            confusion_matrix[int(data[0])][infer_idx] += 1
            if infer_topic not in vals:
                n = len(vals)
                confusion_matrix[int(data[0])][n] += 1
    
    print(confusion_matrix)
    return confusion_matrix

def topic(data_path):
    classes = {}
    inv_classes = {}

    dataset_name = data_path.split('/')[-1]

    with open(os.path.join(datapath, 'classes.txt'), 'r') as infile:
        i = 0
        for line in infile:
            t = line.strip()
            classes[i] = t
            inv_classes[t] = i
            i = i + 1

    confusion_matrix = np.zeros((i-1,i))

    with open(os.path.join(datapath, 'test.csv'), 'r') as infile:
        reader = csv.reader(infile)
        data = []
        for row in reader:
            text = ''
            label = int(row[0]) - 1
            for i in range(1, len(row)):
                text += row[i]
            data.append((label, text))
    
    iterate_through(data, dataset_name, classes, inv_classes, confusion_matrix)


if __name__ == "__main__":
    data_path = "/nobackup/varun/robot/hri-privacy/topic_classification/yahoo_answers"
    topic(data_path)


