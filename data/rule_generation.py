"""
Rather than hard-coding privacy rules from literature, we ideally want the privacy controller to automatically generate and evaluate rules. I’m trying to figure out how we can use something like association rule learning to create general privacy rules.
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


import numpy as np
import random
import tensorflow as tf
from scipy import stats
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
from data.convert_detail import CONVERT as DETAIL
from data.convert_level import CONVERT as LEVEL


def cost(weights, y_trues, y_preds):
    


def evaluate(rules, weights, x, y, sgd, cce, verbose=False):
    correct = 0
    total = 0
    y_preds = []
    y_trues = []
    for i, sample in enumerate(x):
        pred_y = []
        present_rules = []
        for r, rule in enumerate(rules):
            found = True
            for item in rule[0]:
                if item not in sample:
                    found = False
            if found:
                for s in rule[1]:
                    pred_y.append(s)
                    present_rules.append(r)
        # Can improve this to be better than just max(), maybe add some weights and train for n-iterations
        # Should also improve after adding privacy scenarios
        # pred = max(pred_y, key=pred_y.count)
        pred = 0
        for r, rule in enumerate(present_rules):
            pred += weights[rule] * LEVEL[pred_y[r]]
        pred /= len(present_rules)
        if verbose:
            print(pred, y[i][0], len(pred_y))
        if pred < 0.33:
            pred = 'low'
            y_preds.append([1., 0., 0.])
        elif pred >= 0.33 and pred <= 0.66:
            pred = 'moderate'
            y_preds.append([0., 1., 0.])
        elif pred > 0.66:
            pred = 'high'
            y_preds.append([0., 0., 1.])
        if pred == y[i][0]:
            correct += 1
        total += 1
        if y[i][0] == 'low':
            y_trues.append([1., 0., 0.])
        elif y[i][0] == 'moderate':
            y_trues.append([0., 1., 0.])
        elif y[i][0] == 'high':
            y_trues.append([0., 0., 1.])
    loss_fn = lambda: cost(weights, y_trues, y_preds)
    y_trues = tf.convert_to_tensor(np.array(y_trues))
    y_preds = tf.convert_to_tensor(np.array(y_preds))
    print(cce(y_trues, y_preds))
    sgd.minimize(cce, var_list=[weights])
    print(correct / total)


# all_scenarios = [control1, control2, control3, control4, control5, control6, control7, control8, control9, control10, control11, control12, control13, control14, control15, control16, control17, control18, control19, control20, control21, control22, control23, control24, control25, control26, control27, control28, control29, control30, control31, control32, control33, control34, control35, control36, control37, control38, control39, control40, control41, control42, ]
train = [control2, control3, control4, control5, control6, control8, control9, control11, control12, control13, control15, control17, control18, control19, control20, control21, control22, control23, control24, control26, control27, control28, control29, control32, control33, control34, control35, control36, control38, control39, control40, control41, control42, scenario1, scenario2, scenario3, scenario4, scenario7, scenario8, scenario10, scenario11, scenario12, scenario13, scenario14, scenario15, scenario16]
test = [control1, control7, control10, control14, control16, control25, control30, control31, control37, scenario5, scenario6, scenario9]
itemset = []
x_train = []
y_train = []
x_test = []
y_test = []
for scenario in train:
    if len(scenario.topics) == 0:
        topic = 'none'
    else:
        topic = scenario.topics[0]
    itemset.append([scenario.location, scenario.sentiment_value, topic, RELATIONSHIPS[scenario.relationships[1]], PEOPLE[len(scenario.listeners)], scenario.control_level])
    x_train.append([scenario.location, scenario.sentiment_value, topic, RELATIONSHIPS[scenario.relationships[1]], PEOPLE[len(scenario.listeners)]])
    y_train.append([scenario.control_level])

for scenario in test:
    if len(scenario.topics) == 0:
        topic = 'none'
    else:
        topic = scenario.topics[0]
    x_test.append([scenario.location, scenario.sentiment_value, topic, RELATIONSHIPS[scenario.relationships[1]], PEOPLE[len(scenario.listeners)]])
    y_test.append([scenario.control_level])
# itemset = [['eggs', 'bacon', 'soup', 'low'],
#            ['eggs', 'bacon', 'apple', 'high'],
#            ['soup', 'bacon', 'banana', 'low']]
# print(itemset)
for i in [1, 2, 4]:
    for j in [1, 2, 4, 8, 16]:
        sup = i / 42
        conf = j / 42
        print(sup, conf)
        frequencyset, rules = apriori(itemset, minSup=sup, minConf=conf)
        # print(rules)
    # print(frequencyset)
    # print(rules)
    # for rule in rules:
    #     if 'low' in rule[1]:
    #         print(rule)
        sgd = tf.keras.optimizers.SGD(learning_rate=0.1, momentum=0.9)
        cce = tf.keras.losses.CategoricalCrossentropy(from_logits=True)
        weights = tf.Variable([random.uniform(0, 1)] * len(rules))
        for _ in range(100):
            evaluate(rules, weights, x_train, y_train, sgd, cce, verbose=False)
            evaluate(rules, weights, x_test, y_test, sgd, cce, verbose=False)
