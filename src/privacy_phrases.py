import numpy as np


# infile = np.load('data/dataset.npz', allow_pickle=True)
# scenarios = infile['scenarios_dict'].item()
# controls = infile['controls_dict'].item()
# count = 0
# # bad_phrases = ['good', 'na', 'nothing', 'no', 'yes', 'ike', 'none', 'welll']
# with open('data/privacy_phrases.txt', 'w') as outfile:
#     for _, scenario in scenarios.items():
#         for phrase in scenario['privacy_phrase']:
#             if len(phrase) > 20:
#                 outfile.write('{}\n'.format(phrase))
#     for _, control in controls.items():
#         for phrase in control['privacy_phrase']:
#             if len(phrase) > 20:
#                 outfile.write('{}\n'.format(phrase))




infile = np.load('data/dataset.npz', allow_pickle=True)
scenarios = infile['scenarios_dict'].item()
controls = infile['controls_dict'].item()
ultimate_dict = {}
count = 0
realistic = []
for num, scenario in scenarios.items():
    # for answer in scenario['factors']:
    #     for ans in answer.split(','):
    #         if ans not in ultimate_dict:
    #             ultimate_dict[ans] = 0
    #         ultimate_dict[ans] += 1
    #     count += 1
    ultimate_dict[num] = []
    for answer in scenario['realistic']:
        ultimate_dict[num].append(answer)
        realistic.append(answer)


for num, scenario in controls.items():
    # for answer in scenario['factors']:
    #     for ans in answer.split(','):
    #         if ans not in ultimate_dict:
    #             ultimate_dict[ans] = 0
    #         ultimate_dict[ans] += 1
    #     count += 1
    ultimate_dict[num] = []
    for answer in scenario['realistic']:
        ultimate_dict[num].append(answer)
        realistic.append(answer)

print(ultimate_dict)
print(count)
print(np.mean(realistic))




infile = np.load('data/dataset.npz', allow_pickle=True)
user_data = infile['demographics_dict'].item()
count = 0
female = 0
age = []
gender = {}
for key, val in user_data.items():
    age.append(val['age'])
    count += 1
    if val['gender'] not in gender:
        gender[val['gender']] = 0
    gender[val['gender']] += 1

print(count)
print(np.mean(age))
print(np.std(age))
print(min(age))
print(max(age))
print(gender)


confusion_matrix = [[0.80530973, 0.00221239, 0.01327434, 0.05752212, 0., 0.00221239, 0.00884956, 0.09734513, 0., 0.01327434],
                    [0.15736041, 0.55329949, 0.07614213, 0.06091371, 0.01269036, 0.00761421, 0.07360406, 0.05583756, 0., 0.00253807],
                    [0.26386233, 0.00382409, 0.69216061, 0.00382409, 0., 0.00764818, 0.00382409, 0.0210325 , 0., 0.00382409],
                    [0.17451524, 0.        , 0.02770083, 0.63157895, 0.02493075, 0., 0.04155125, 0.07202216, 0., 0.02770083],
                    [0.03649635, 0.05596107, 0.00243309, 0.02919708, 0.78832117, 0., 0.01703163, 0.07055961, 0., 0.],
                    [0.11484594, 0.        , 0.00840336, 0.00280112, 0.00280112, 0.79271709, 0.00280112, 0.07282913, 0., 0.00280112],
                    [0.20157068, 0.01570681, 0.02879581, 0.13612565, 0.04188482, 0.0052356, 0.42670157, 0.08376963, 0., 0.06020942],
                    [0.14769231, 0.00615385, 0.01230769, 0.03076923, 0.02153846, 0.00615385, 0., 0.77230769, 0.        , 0.00307692],
                    [0.13866667, 0.        , 0.02933333, 0.00533333, 0.00533333, 0., 0.00266667, 0.25866667, 0.55733333, 0.00266667],
                    [0.32638889, 0.00694444, 0.00694444, 0.0462963 , 0.00231481, 0.00462963, 0.04398148, 0.05092593, 0., 0.51157407]]

matches = []
for i, row in enumerate(confusion_matrix):
    for j, col in enumerate(row):
        if i == j:
            matches.append(col)
print(np.mean(matches))