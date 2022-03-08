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


# OR go back to manually assigning weights and cost function
# OR manually order weights by factors
# OR go back to max()

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
# convert logits to probabilities derived from weights
# or create tiny model using matching rules as x input
def cost(weights, y_trues, y_preds, found_rules, labels):
    new_y_preds = found_rules * weights * y_preds
    new_y_preds = tf.math.reduce_mean(new_y_preds, axis=1)
    loss = tf.keras.losses.mean_squared_error(y_trues, new_y_preds)
    print(tf.reduce_sum(loss), end='\r')
    correct = 0
    total = 0
    for i, pred in enumerate(new_y_preds.numpy()):
        if pred < 2.8:
            control_level = 'low'
        elif pred >= 2.8 and pred <= 3.6:
            control_level = 'moderate'
        elif pred > 3.6:
            control_level = 'high'
        if labels[i] == control_level:
            correct += 1
        total += 1
    print(correct / total)
    return loss


def evaluate(rules, weights, x, y, labels, sgd, verbose=False):
    y_preds = []
    y_trues = []
    found_rules = []
    for i, sample in enumerate(x):
        y_preds.append([])
        found_rules.append([])
        y_trues.append(y[i])
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
            else:
                found_rules[i].append(0.)
            for s in rule[1]:
                y_preds[i].append(LEVEL[s])
    loss_fn = lambda: cost(weights, y_trues, y_preds, found_rules, labels)
    # y_trues = tf.convert_to_tensor(np.array(y_trues), dtype=tf.float32)
    # y_preds = tf.convert_to_tensor(np.array(y_preds), dtype=tf.float32)
    for _ in range(20000):
        # print(tf.shape(found_rules))
        # print(tf.shape(weights))
        # print(tf.shape(y_preds))
        # print(tf.shape(y_trues))

        # masked_weights = found_rules
        # trainY = y_trues
        preds = sgd.minimize(loss_fn, var_list=[weights])



# all_scenarios = [control1, control2, control3, control4, control5, control6, control7, control8, control9, control10, control11, control12, control13, control14, control15, control16, control17, control18, control19, control20, control21, control22, control23, control24, control25, control26, control27, control28, control29, control30, control31, control32, control33, control34, control35, control36, control37, control38, control39, control40, control41, control42, ]
train = [control2, control3, control4, control5, control6, control8, control9, control11, control12, control13, control15, control17, control18, control19, control20, control21, control22, control23, control24, control26, control27, control28, control29, control32, control33, control34, control35, control36, control38, control39, control40, control41, control42, scenario1, scenario2, scenario3, scenario4, scenario7, scenario8, scenario10, scenario11, scenario12, scenario13, scenario14, scenario15, scenario16]
test = [control1, control7, control10, control14, control16, control25, control30, control31, control37, scenario5, scenario6, scenario9]
itemset = []
x_train = []
y_train = []
x_test = []
y_test = []
train_labels = []
test_labels = []
for scenario in train:
    if len(scenario.topics) == 0:
        topic = 'none'
    else:
        topic = scenario.topics[0]
    itemset.append([LOCATION[scenario.location], scenario.sentiment_value, topic, RELATIONSHIPS[scenario.relationships[1]], PEOPLE[len(scenario.listeners)], scenario.detail, scenario.control_level])
    x_train.append([LOCATION[scenario.location], scenario.sentiment_value, topic, RELATIONSHIPS[scenario.relationships[1]], PEOPLE[len(scenario.listeners)], scenario.detail])
    y_train.append([scenario.mean_label])
    train_labels.append([scenario.control_level])

for scenario in test:
    if len(scenario.topics) == 0:
        topic = 'none'
    else:
        topic = scenario.topics[0]
    x_test.append([LOCATION[scenario.location], scenario.sentiment_value, topic, RELATIONSHIPS[scenario.relationships[1]], PEOPLE[len(scenario.listeners)]])
    y_test.append([scenario.mean_label])
    test_labels.append([scenario.control_level])
# itemset = [['eggs', 'bacon', 'soup', 'low'],
#            ['eggs', 'bacon', 'apple', 'high'],
#            ['soup', 'bacon', 'banana', 'low']]
# print(itemset)
for i in [1, 2, 4]:
    # for j in [1, 2, 4, 8, 16]:
    for j in [1]:
        sup = i / 42
        conf = j / 42
        # print(sup, conf)
        frequencyset, rules = apriori(itemset, minSup=sup, minConf=conf)
        # print(rules)
    # print(frequencyset)
    # print(rules)
    # for rule in rules:
    #     if 'low' in rule[1]:
    #         print(rule)

        sgd = tf.keras.optimizers.SGD(learning_rate=0.1, momentum=0.9)

        weights = tf.Variable([random.uniform(0, 1)] * len(rules), dtype=tf.float32)
        # for _ in range(100):
        weights = evaluate(rules, weights, x_train, y_train, train_labels, sgd, verbose=False)
        # evaluate(rules, weights, x_test, y_test, sgd, verbose=True)
        exit()
