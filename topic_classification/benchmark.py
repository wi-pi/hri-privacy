from natural_language import Google_NLP
from convert_topics import CONVERT
import argparse
import os
import csv
import numpy as np
from tqdm import tqdm

#CONVERT = {'yahoo_answers': {'People & Society': ['Society & Culture', 'Family & Relationships'], 'Science': ['Science & Mathematics'], 'Health': ['Health'], 'Jobs & Education': ['Education & Reference'], 'Books & Literature': ['Education & Reference'], 'Computers & Electronics': ['Computers & Internet'], 'Sports': ['Sports'], 'Finance': ['Business & Finance'], 'Business & Industrial': ['Business & Finance'], 'Arts & Entertainment': ['Entertainment & Music'], 'Law & Government': ['Politics & Government']}}


def joint_sort(list1, list2):
    zipped_lists = zip(list1, list2)
    sorted_pairs = sorted(zipped_lists)

    tuples = zip(*sorted_pairs)
    list1, list2 = [list(t) for t in tuples]
    return list1, list2

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

    l_n, l_c = len(names), len(confidences)
    if l_n > 0 and l_c > 0:
        names, confidences = joint_sort(names, confidences)
        #print(names, confidences)
        return [names[-1]], [confidences[-1]]
    else:
        return None, None

def iterate_through(dataset, dataset_name, classes, inv_classes, confusion_matrix, label_counts):
    vals = []
    d = CONVERT[dataset_name]
    keys = list(d.keys())
    for k in keys:
        vals.append(d[k][0])

    len_d = {}

    M = len(dataset)
    returned_list = []
    for i in tqdm(range(M)):
        data = dataset[i]
        nlp = Google_NLP(data[1], verbose=False)
        inferred_topic = str(nlp.get_topic())
        infer_topics, confidences = parse(inferred_topic)
        #print(infer_topics, confidences)
        #exit()


        if infer_topics != None and confidences != None:
            source_topic = classes[int(data[0])]
            N = len(infer_topics)
            l = data[2]
            for i in range(N):
                infer_topic = infer_topics[i]
                returned_list.append(infer_topic)
                confidence = confidences[i]
                if infer_topic in d:
                    infer_topic_vals = d[infer_topic]
                    if source_topic in infer_topic_vals:
                        n = len(vals)
                        #print("1:", int(data[0]), n)
                        #confusion_matrix[int(data[0])][n-1] += 1
                        confusion_matrix[int(data[0])][int(data[0])] += 1
                    else:
                        #infer_idx = inv_classes[infer_topic]
                        #print("2:",int(data[0]), infer_idx)
                        infer_idx = inv_classes[infer_topic_vals[0]]
                        confusion_matrix[int(data[0])][infer_idx] += 1
                else:
                    confusion_matrix[int(data[0])][n-1] += 1
                
                if int(data[0]) not in len_d:
                    len_d[int(data[0])] = 1
                else:
                    len_d[int(data[0])] += 1

    returned_list = list(set(returned_list))
    

    keys = sorted(list(len_d.keys()))
    for k in keys:
        v = len_d[k]
        confusion_matrix[k,:] = confusion_matrix[k,:]/v

    print(confusion_matrix)

    f = open('returned_labels.txt', 'w')
    for e in returned_list:
        f.write(e + "\n")

    f.close()

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
   
    c_matrix = iterate_through(data, dataset_name, classes, inv_classes, confusion_matrix, label_counts)
    with open('confusion_matrix.npy', 'wb') as f:
        np.save(f, c_matrix)


if __name__ == "__main__":
    data_path = "/nobackup/varun/robot/hri-privacy/topic_classification/yahoo_answers"
    topic(data_path)


