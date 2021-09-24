import numpy as np


infile = np.load('data/dataset.npz', allow_pickle=True)
scenarios = infile['scenarios_dict'].item()
controls = infile['controls_dict'].item()
count = 0
# bad_phrases = ['good', 'na', 'nothing', 'no', 'yes', 'ike', 'none', 'welll']
with open('data/privacy_phrases.txt', 'w') as outfile:
    for _, scenario in scenarios.items():
        for phrase in scenario['privacy_phrase']:
            if len(phrase) > 20:
                outfile.write('{}\n'.format(phrase))
    for _, control in controls.items():
        for phrase in control['privacy_phrase']:
            if len(phrase) > 20:
                outfile.write('{}\n'.format(phrase))