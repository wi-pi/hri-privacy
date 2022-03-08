"""
Rather than hard-coding privacy rules from literature, we ideally want the privacy controller to automatically generate and evaluate rules. I'm trying to figure out how we can use something like association rule learning to create general privacy rules.
Sentiment: 5 class
Topic: 27 class
Number of People: 3 class
Location: 2 class
Relationships: 7 class
Speaker Role: 2 class
Privacy Phrase: 2 class
Level of Detail: 3 class

Operations: [<, <=, ==, >=, >, &&, ||]
Rules: Smaller weight the longer a rule is, larger weight the shorter a rule is.
Rules: Weighted sum of all rules should return value between 0 and 1
Privacy Thresholds (Outputs): Low/Mod (e.g. 0.25) and Mod/High (e.g. 0.75)

Example rules:
if topic == medical and location == public:
    Score = 1
if relationship == close and level of detail == high

Metrics for a given rule: Support (x / 58), Confidence (Supp(X and Y) / Supp(Z)), Lift (Supp(X and Y) / Supp(X) * Supp(Y))
    if lift == 1, independent of each other
    if lift > 1, 2 occurrences are dependent on one another
    if lift < 1, items substitute each other (negative effect on presence of another item)

58 scenarios with labels
Create n association rules using the 3 metrics

Apriori algorithm:
[
    scenario1: ['computers', 'negative', 'many people', 'public', 'close', 'low detail'],
    scenario2: ['finances', 'neutral', '2 people', 'private', 'moderate', 'moderate detail']
]
"""


"""
        model = Sequential()
        model.add(Conv1D(filters=64, kernel_size=3, activation='relu', input_shape=[len(rules), 2]))
        model.add(Conv1D(filters=64, kernel_size=3, activation='relu'))
        model.add(Dropout(0.5))
        model.add(MaxPooling1D(pool_size=2))
        model.add(Flatten())
        model.add(Dense(100, activation='relu'))
        model.add(Dense(3, activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    trainX = []
    for sample, _ in enumerate(found_rules):
        trainX.append([])
        for f1, f2 in zip(found_rules[sample], y_preds[sample]):
            trainX[sample].append([f1, f2])
    found_rules = tf.convert_to_tensor(np.array(found_rules)[..., None], dtype=tf.float32)
    y_trues = tf.convert_to_tensor(np.array(y_trues), dtype=tf.float32)
    y_preds = tf.convert_to_tensor(np.array(y_preds)[..., None], dtype=tf.float32)
    trainX = tf.convert_to_tensor(np.array(trainX), dtype=tf.float32)

        score = model.evaluate(trainX, trainY)

"""


import numpy as np
import random
import tensorflow as tf
from scipy import stats
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Conv1D
from tensorflow.keras.layers import MaxPooling1D
from tensorflow.keras.utils import to_categorical
from data.apriori import apriori
from data.metadata import control1, control2, control3, control4, control5, control6, control7
from data.metadata import control8, control9, control10, control11, control12, control13, control14
from data.metadata import control15, control16, control17, control18, control19, control20, control21
from data.metadata import control22, control23, control24, control25, control26, control27, control28
from data.metadata import control29, control30, control31, control32, control33, control34, control35
from data.metadata import control36, control37, control38, control39, control40, control41, control42
from data.metadata import scenario1, scenario2, scenario3, scenario4, scenario5, scenario6, scenario7
from data.metadata import scenario8, scenario9, scenario10, scenario11, scenario12, scenario13, scenario14
from data.metadata import scenario15, scenario16
from data.convert_relationships import CONVERT as RELATIONSHIPS
from data.convert_locations import CONVERT as LOCATION
from data.convert_people import CONVERT as PEOPLE
from data.convert_level import CONVERT as LEVEL


counts = {'relationship': 450, 'emotion': 329, 'number_people': 281, 'detail': 325, 'topic': 504, 'location': 206, 'none': 36, 'total': 870}
mappings = {'direct_family': 'relationship', 'distant_family': 'relationship', 'close': 'relationship', 'moderate': 'relationship', 'professional_sensitive': 'relationship', 'professional': 'relationship', 'distant': 'relationship',
            'negative': 'emotion', 'slightly_negative': 'emotion', 'neutral': 'emotion', 'slightly_positive': 'emotion', 'positive': 'emotion',
            'few': 'number_people', 'some': 'number_people', 'many': 'number_people',
            'Adult': 'topic', 'Arts & Entertainment': 'topic', 'Autos & Vehicles': 'topic', 'Beauty & Fitness': 'topic', 'Books & Literature': 'topic', 'Business & Industrial': 'topic', 'Computers & Electronics': 'topic', 'Finance': 'topic', 'Food & Drink': 'topic', 'Games': 'topic', 'Health': 'topic', 'Hobbies & Leisure': 'topic', 'Home & Garden': 'topic', 'Internet & Telecom': 'topic', 'Jobs & Education': 'topic', 'Law & Government': 'topic', 'News': 'topic', 'Online Communities': 'topic', 'People & Society': 'topic', 'Pets & Animals': 'topic', 'Real Estate': 'topic', 'Reference': 'topic', 'Science': 'topic', 'Sensitive Subjects': 'topic', 'Shopping': 'topic', 'Sports': 'topic', 'Travel': 'topic', 'none': 'topic',
            'non_domestic': 'location', 'domestic': 'location',
            'short': 'detail', 'medium': 'detail', 'long': 'detail',
            'doctor\'s office': 'location', 'office': 'location', 'courthouse': 'location', 'school graduation event': 'location', 'classroom': 'location', 'hospital elevator': 'location', 'production studio': 'location', 'medical lab': 'location', 'ticket booth': 'location', 'car shop': 'location', 'coffee shop': 'location', 'school choir room': 'location', 'gym': 'location', 'restaurant': 'location', 'public library': 'location', 'park': 'location', 'bar': 'location',
            'living room': 'location', 'kitchen': 'location', 'dining room': 'location', 'apartment': 'location', 'home': 'location', 'front yard': 'location', 'house': 'location', 'bedroom': 'location', 'university dorm': 'location', 'garage': 'location', 'apartment lobby': 'location', 'home birthday party': 'location'
}


def evaluate(rules, x, y, verbose=False):
    correct = 0
    total = 0
    y_preds = []
    y_preds_items = []
    y_trues = []
    found_rules = []
    for i, sample in enumerate(x):
        y_preds.append([])
        y_preds_items.append({'low': 0, 'moderate': 0, 'high': 0})
        found_rules.append([])
        for r, rule in enumerate(rules):
            found = True
            rules_items = []
            for item in rule[0]:
                if item not in sample:
                    found = False
                else:
                    rules_items.append(mappings[item])
            if found:
                found_rules[i].append(1.)
                for s in rule[1]:
                    y_preds[i].append(s)
                avg = 0
                for item in rules_items:
                    avg += counts[item]
                avg /= (len(rules_items) * counts['total'])
                y_preds_items[i][s] += avg
            else:
                found_rules[i].append(0.)
        pred = max(y_preds_items[i], key=y_preds_items[i].get)
        if verbose:
            print(pred, y[i][0])
        total += 1
        if y[i][0] == pred:
            correct += 1
    print(correct / total)

all_train = [control2, control3, control4, control5, control6, control8, control9, control11, control12, control13, control15, control17, control18, control19, control20, control21, control22, control23, control24, control26, control27, control28, control29, control32, control33, control34, control35, control36, control38, control39, control40, control41, control42, scenario1, scenario2, scenario3, scenario4, scenario7, scenario8, scenario10, scenario11, scenario12, scenario13, scenario14, scenario15, scenario16, control1, control7, control10, control14, control16, control25, control30, control31, control37, scenario5, scenario6, scenario9]
all_train_labels = [('low',), ('high',), ('high',), ('low',), ('moderate',), ('low',), ('moderate',), ('low',), ('low',), ('moderate',), ('low',), ('moderate',), ('high',), ('moderate',), ('low',), ('moderate',), ('low',), ('high',), ('moderate',), ('moderate',), ('low',), ('moderate',), ('high',), ('high',), ('high',), ('high',), ('low',), ('moderate',), ('high',), ('moderate',), ('moderate',), ('low',), ('low',), ('high',), ('moderate',), ('moderate',), ('high',), ('moderate',), ('high',), ('moderate',), ('low',), ('low',), ('moderate',), ('moderate',), ('moderate',), ('moderate',), ('high',), ('moderate',), ('high',), ('low',), ('high',), ('high',), ('low',), ('high',), ('moderate',), ('moderate',), ('moderate',), ('high',)]
train = [control2, control3, control4, control5, control6, control8, control9, control11, control12, control13, control15, control17, control18, control19, control20, control21, control22, control23, control24, control26, control27, control28, control29, control32, control33, control34, control35, control36, control38, control39, control40, control41, control42, scenario1, scenario2, scenario3, scenario4, scenario7, scenario8, scenario10, scenario11, scenario12, scenario13, scenario14, scenario15, scenario16]
test = [control1, control7, control10, control14, control16, control25, control30, control31, control37, scenario5, scenario6, scenario9]
new_train_labels = [('low',), ('high',), ('high',), ('low',), ('moderate',), ('low',), ('moderate',), ('low',), ('low',), ('moderate',), ('low',), ('moderate',), ('high',), ('moderate',), ('low',), ('moderate',), ('low',), ('high',), ('moderate',), ('moderate',), ('low',), ('moderate',), ('high',), ('high',), ('high',), ('high',), ('low',), ('moderate',), ('high',), ('moderate',), ('moderate',), ('low',), ('low',), ('high',), ('moderate',), ('moderate',), ('high',), ('moderate',), ('high',), ('moderate',), ('low',), ('low',), ('moderate',), ('moderate',), ('moderate',), ('moderate',)]
new_test_labels = [('high',), ('moderate',), ('high',), ('low',), ('high',), ('high',), ('low',), ('high',), ('moderate',), ('moderate',), ('moderate',), ('high',)]
indices = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57]
new_test_set = []
new_new_test_labels = []
random_indices = []
for i in random.sample(indices, 12):
    new_test_set.append(all_train[i])
    new_new_test_labels.append(all_train_labels[i])
    random_indices.append(i)
random_indices.sort(reverse=True)
for i in random_indices:
    all_train.pop(i)
    all_train_labels.pop(i)
train = all_train
test = new_test_set
itemset = []
x_train = []
y_train = all_train_labels
x_test = []
y_test = new_new_test_labels
for i, scenario in enumerate(train):
    if len(scenario.topics) == 0:
        topic = 'none'
    else:
        topic = scenario.topics[0]
    # itemset.append([LOCATION[scenario.location], scenario.sentiment_value, topic, RELATIONSHIPS[scenario.relationships[1]], PEOPLE[len(scenario.listeners)], scenario.detail, scenario.control_level])
    itemset.append([LOCATION[scenario.location], scenario.sentiment_value, topic, RELATIONSHIPS[scenario.relationships[1]], PEOPLE[len(scenario.listeners)], scenario.detail, all_train_labels[i][0]])
    x_train.append([LOCATION[scenario.location], scenario.sentiment_value, topic, RELATIONSHIPS[scenario.relationships[1]], PEOPLE[len(scenario.listeners)], scenario.detail])
    # y_train.append([scenario.control_level])
for scenario in test:
    if len(scenario.topics) == 0:
        topic = 'none'
    else:
        topic = scenario.topics[0]
    x_test.append([LOCATION[scenario.location], scenario.sentiment_value, topic, RELATIONSHIPS[scenario.relationships[1]], PEOPLE[len(scenario.listeners)]])
    # y_test.append([scenario.control_level])

conf = 1 / 46
rules = []
for i in [1, 2, 3, 4, 5, 6]:
    sup = i / 46
    frequencyset, new_rules = apriori(itemset, minSup=sup, minConf=conf)
    rules.extend(new_rules)
evaluate(rules, x_train, y_train, verbose=False)
evaluate(rules, x_test, y_test, verbose=False)
