from src.natural_language import Google_NLP
from data.convert_topics import CONVERT
import argparse
import os
import csv


def sentiment(api):
    datapath1 = 'data/sentiment_analysis/aclImdb/test/pos'
    datapath2 = 'data/sentiment_analysis/aclImdb/test/neg'
    outputs = {'total': 0, 'tp': 0, 'tn': 0, 'fp': 0, 'fn': 0}

    def iterate_through(datapath, api, sentiment_type, outputs):
        if api == 'google':
            for file in os.listdir(datapath):
                with open(os.path.join(datapath, file), 'r') as infile:
                    nlp = Google_NLP(infile.read(), verbose=False)
                    infer_sentiment = nlp.get_sentiment().score
                    source_sentiment = file.replace(datapath, '').replace('.txt', '').split('_')[1]
                    if infer_sentiment >= 0 and sentiment_type == 'pos':
                        outputs['tp'] += 1
                    elif infer_sentiment < 0 and sentiment_type == 'pos':
                        outputs['fn'] += 1
                    elif infer_sentiment <= 0 and sentiment_type == 'neg':
                        outputs['tn'] += 1
                    elif infer_sentiment > 0 and sentiment_type == 'neg':
                        outputs['fp'] += 1
                    outputs['total'] += 1
                print(outputs, end='\r')
        elif api == 'textrazor':
            pass
        return outputs

    outputs = iterate_through(datapath1, api, 'pos', outputs)
    outputs = iterate_through(datapath2, api, 'neg', outputs)
    precision = outputs['tp'] / (outputs['tp'] + outputs['fp'])
    recall = outputs['tp'] / (outputs['tp'] + outputs['fn'])
    f1_Score = 2 * (1 / (1 / precision) + (1 / recall))
    print()
    print('Precision: {:.4f}, Recall: {:.4f}, F1 Score: {:.4f}'.format(precision, recall, f1_Score))


def topic(api, dataset):
    datapath = 'data/text_classification/{}'.format(dataset)
    outputs = {'total': 0, 't': 0, 'f': 0}
    confusion_matrix = {}
    classes = []

    for key1, _ in CONVERT[dataset].items():
        confusion_matrix[key1] = {}
        for key2, _ in CONVERT[dataset].items():
            confusion_matrix[key1][key2] = 0

    with open(os.path.join(datapath), 'classes.txt', 'r') as infile:
        for line in infile:
            classes.append(line.strip())

    with open(os.path.join(datapath, 'test.csv'), 'r') as infile:
        reader = csv.reader(infile)
        datas = []
        for row in reader:
            text = ''
            label = int(row[0]) - 1
            for i in range(1, len(row)):
                text += row[i]
            datas.append((label, text))
            iterate_through(datas, api, outputs, confusion_matrix)

    def iterate_through(dataset, api, datas, outputs, confusion_matrix):
        if api == 'google':
            nlp = Google_NLP(datas[1], verbose=False)
            infer_topic = nlp.get_topic()
            source_topic = datas[0]
            if infer_topic in CONVERT[dataset][source_topic]:
                outputs['t'] += 1
                confusion_matrix[source_topic]
            elif infer_topic < 0:
                outputs['f'] += 1
            outputs['total'] += 1
            print(outputs, end='\r')
        elif api == 'textrazor':
            pass
        return outputs

    outputs = iterate_through(datapath1, api, 'pos', outputs)
    outputs = iterate_through(datapath2, api, 'neg', outputs)
    precision = outputs['tp'] / (outputs['tp'] + outputs['fp'])
    recall = outputs['tp'] / (outputs['tp'] + outputs['fn'])
    f1_Score = 2 * (1 / (1 / precision) + (1 / recall))
    print()
    print('Precision: {:.4f}, Recall: {:.4f}, F1 Score: {:.4f}'.format(precision, recall, f1_Score))



parser = argparse.ArgumentParser()
parser.add_argument('--test', type=str, default='sentiment', help='The component of the controller to evaluate on benchmarks',
    choices=['sentiment', 'topic', 'ner', 'transcription', 'diarization', 'intent', 'emotion', 'recognition', 'semantic', 'summarization'])
parser.add_argument('--api', type=str, default='google', help='The NLP API to use',
    choices=['google', 'textrazor'])
parser.add_argument('--dataset', type=str, default='aclImdb', help='The dataset to use',
    choices=['aclImdb', 'yahoo_answers'])
args = parser.parse_args()

if args.test == 'sentiment':
    sentiment(args.api)

elif args.test == 'topic':

    if args.api == 'google':
        pass
    elif args.api == 'textrazor':
        pass
elif args.test == 'ner':

    if args.api == 'google':
        pass
    elif args.api == 'textrazor':
        pass

elif args.test == 'transcription':
    pass

elif args.test == 'diarization':
    pass

elif args.test == 'intent':
    pass

elif args.test == 'emotion':
    pass

elif args.test == 'recognition':
    pass

elif args.test == 'semantic':
    pass

elif args.test == 'summarization':
    pass
