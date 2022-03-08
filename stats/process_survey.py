import csv
import os
import numpy as np
from tqdm import tqdm
from difflib import get_close_matches
from src.natural_language import Google_NLP
from data.convert_relationships import CONVERT as RELATIONSHIPS
from data.convert_locations import CONVERT as LOCATIONS
from data.convert_likert import CONVERT as LIKERT, INVERT


def CronbachAlpha(itemscores):
    itemscores = np.asarray(itemscores)
    itemvars = itemscores.var(axis=1, ddof=1)
    tscores = itemscores.sum(axis=0)
    nitems = len(itemscores)
    return nitems / (nitems-1.) * (1 - itemvars.sum() / tscores.var(ddof=1))


infile = open('data/hridatasetsurvey.csv', 'r')
infile = open('data/hri_dataset.csv', 'r')
infile = open('data/batch8.csv', 'r')
scenarios_infile = open('data/privacy_scenarios.txt', 'r')
reader = csv.reader(infile)
index_dict = {}
user_data = {}
controls_metadata = {}
controls_dict = {}
scenarios_metadata = {}
scenarios_dict = {}
privacy_dict = {}
demographics_dict = {}
attention_checks = {}
all_cronbach_data = {}
cronbach_data = {'q1': [], 'q2': [], 'q3': [], 'q4': [], 'q5': [], 'q6': [], 'q7': [], 'q8': [], 'q9': [], 'q10': [], 'q11': [], 'q12': [], 'q13': [], 'q14': []}
privacy_cronbach = {'q1': [], 'q2': [], 'q3': [], 'q4': [], 'q5': [], 'q6': [], 'q7': [], 'q8': []}


for line in scenarios_infile:
    if ':' in line:
        if 'Control' in line:
            control_num = int(line.strip().split(':')[0].replace('Control ', ''))
            controls_metadata[control_num] = {'names': [], 'relationships': [], 'speaker': [], 'text': [], 'all_text': ''}
            control = True
        elif 'Scenario' in line:
            scenario_num = int(line.strip().split(':')[0].replace('Scenario ', ''))
            scenarios_metadata[scenario_num] = {'names': [], 'relationships': [], 'speaker': [], 'text': [], 'all_text': '', 'disclosure_names': [], 'disclosure_relationships': [], 'disclosure_text': [], 'disclosure_speaker': [], 'disclosure_all_text': ''}
            control = False
            disclosure = False
        elif 'Location:' in line:
            location = line.strip().split(': ')[1].lower()
            if "'s " in location:
                location = location.split("'s ")[1]
            if control:
                controls_metadata[control_num]['location'] = location
            else:
                if 'location' in scenarios_metadata[scenario_num]:
                    scenarios_metadata[scenario_num]['disclosure_location'] = location
                    disclosure = True
                else:
                    scenarios_metadata[scenario_num]['location'] = location
        elif 'People:' in line:
            names = line.strip().split(': ')[1].split(', ')
            if not control and len(scenarios_metadata[scenario_num]['names']) > 0:
                for name in names:
                    if '(' in name:
                        split = name.split('(')
                        relationship = split[1].replace(')', '').lower()
                        if "'s " in relationship:
                            rel_split = relationship.split("'s ")
                            source = rel_split[0]
                            relationship = rel_split[1]
                        scenarios_metadata[scenario_num]['disclosure_names'].append(split[0][:-1])
                        scenarios_metadata[scenario_num]['disclosure_relationships'].append((source, relationship))
                    else:
                        scenarios_metadata[scenario_num]['disclosure_names'].append(name)
                        scenarios_metadata[scenario_num]['disclosure_relationships'].append((name, 'source'))
            else:
                for name in names:
                    if '(' in name:
                        split = name.split('(')
                        relationship = split[1].replace(')', '').lower()
                        if "'s " in relationship:
                            rel_split = relationship.split("'s ")
                            source = rel_split[0]
                            relationship = rel_split[1]
                        if control:
                            controls_metadata[control_num]['names'].append(split[0][:-1])
                            controls_metadata[control_num]['relationships'].append((source, relationship))
                        else:
                            scenarios_metadata[scenario_num]['names'].append(split[0][:-1])
                            scenarios_metadata[scenario_num]['relationships'].append((source, relationship))
                    else:
                        if control:
                            controls_metadata[control_num]['names'].append(name)
                            controls_metadata[control_num]['relationships'].append((name, 'source'))
                        else:
                            scenarios_metadata[scenario_num]['names'].append(name)
                            scenarios_metadata[scenario_num]['relationships'].append((name, 'source'))
        elif 'Context:' in line:
            context = line.strip().split(': ')[1]
            if control:
                controls_metadata[control_num]['context'] = context
            else:
                if 'context' in scenarios_metadata[scenario_num]:
                    scenarios_metadata[scenario_num]['disclosure_context'] = context
                else:
                    scenarios_metadata[scenario_num]['context'] = context
        else:
            split = line.strip().split(': ')
            speaker = split[0]
            text = split[1]
            if control:
                controls_metadata[control_num]['speaker'].append(speaker)
                controls_metadata[control_num]['text'].append(text)
                controls_metadata[control_num]['all_text'] += '{} '.format(text)
            else:
                scenarios_metadata[scenario_num]['speaker'].append(speaker)
                scenarios_metadata[scenario_num]['text'].append(text)
                scenarios_metadata[scenario_num]['all_text'] += '{} '.format(text)
                # if disclosure:
                #     scenarios_metadata[scenario_num]['disclosure_speaker'].append(speaker)
                #     scenarios_metadata[scenario_num]['disclosure_text'].append(text)
                #     scenarios_metadata[scenario_num]['disclosure_all_text'] += '{} '.format(text)
                # else:
                #     scenarios_metadata[scenario_num]['speaker'].append(speaker)
                #     scenarios_metadata[scenario_num]['text'].append(text)
                #     scenarios_metadata[scenario_num]['all_text'] += '{} '.format(text)

for i, user in enumerate(reader):
    if i == 0:
        continue
    if i == 1:
        k = 0
        for j, column in enumerate(user):
            column_id = '{} {}'.format(j, column)
            print(column_id)
            index_dict[j] = column_id
            if j < 17: # User data
                pass
            if j >= 17 and j < 29: # Timings
                pass
            if j >= 29 and j < 596: # Control scenarios
                if 'Timing - ' in column:
                    pass
                elif 'In responding to this question, please select' in column:
                    attention_checks[column_id] = column.split('"')[1].strip().lower()
                elif 'In responding to this question, please type' in column:
                    attention_checks[column_id] = column.split('"')[1].strip().lower()
            if j >= 596 and j < 817: # Privacy scenarios
                if 'In responding to this question, please select' in column:
                    attention_checks[column_id] = column.split('"')[1].strip().lower()
                elif 'In responding to this question, please type' in column:
                    attention_checks[column_id] = column.split('"')[1].strip().lower()

    if i == 2:
        continue
    if i > 2:
        user_data[i] = {'attention_check_pass': 0, 'duration': 0, 'controls': {}, 'scenarios': {}}
        privacy_dict[i] = {}
        demographics_dict[i] = {}
        k = 0
        for j, column in enumerate(user):
            column_id = index_dict[j]
            col = column.strip().lower()
            if j == 596:
                k = 0
                if k not in all_cronbach_data:
                    all_cronbach_data[k] = {'q1': [], 'q2': [], 'q3': [], 'q4': [], 'q5': [], 'q6': [], 'q7': [], 'q8': [], 'q9': [], 'q10': [], 'q11': [], 'q12': [], 'q13': [], 'q14': []}
            if j < 817 and 'This conversation is realistic' in column_id:
                k += 1
                if k not in all_cronbach_data:
                    all_cronbach_data[k] = {'q1': [], 'q2': [], 'q3': [], 'q4': [], 'q5': [], 'q6': [], 'q7': [], 'q8': [], 'q9': [], 'q10': [], 'q11': [], 'q12': [], 'q13': [], 'q14': []}
            if len(column) == 0:
                continue
            if j < 17: # User data
                if j == 5:
                    user_data[i]['duration'] = int(column)
            if j >= 17 and j < 29: # Timings
                pass
            if j >= 29 and j < 596: # Control scenarios
                if 'This conversation is realistic' in column_id:
                    user_data[i]['controls'][k] = {'realistic': [], 'sensitive': [], 'privacy_violated': [], 'close_comfortable': [],
                                 'distant_comfortable': [], 'close_share': [], 'distant_share': [], 'privacy_phrase': [], 'factors': []}
                    user_data[i]['controls'][k]['realistic'].append(LIKERT[col])
                    all_cronbach_data[k]['q1'].append(LIKERT[col])
                elif 'This conversation contains sensitive content' in column_id:
                    user_data[i]['controls'][k]['sensitive'].append(LIKERT[col])
                    all_cronbach_data[k]['q2'].append(LIKERT[col])
                elif 'I would feel my privacy was violated if someone listening shared this information with someone else' in column_id:
                    user_data[i]['controls'][k]['privacy_violated'].append(LIKERT[col])
                    all_cronbach_data[k]['q3'].append(LIKERT[col])
                elif 'a close relationship' in column_id and 'I would feel comfortable sharing this information with someone else' in column_id:
                    user_data[i]['controls'][k]['close_comfortable'].append(INVERT[LIKERT[col]])
                    all_cronbach_data[k]['q4'].append(INVERT[LIKERT[col]])
                elif 'a distant relationship' in column_id and 'I would feel comfortable sharing this information with someone else' in column_id:
                    user_data[i]['controls'][k]['distant_comfortable'].append(INVERT[LIKERT[col]])
                    all_cronbach_data[k]['q5'].append(INVERT[LIKERT[col]])
                elif 'a close relationship' in column_id and 'not to share personal information with someone else' in column_id:
                    user_data[i]['controls'][k]['close_share'].append(LIKERT[col])
                    all_cronbach_data[k]['q6'].append(LIKERT[col])
                elif 'a distant relationship' in column_id and 'not to share personal information with someone else' in column_id:
                    user_data[i]['controls'][k]['distant_share'].append(LIKERT[col])
                    all_cronbach_data[k]['q7'].append(LIKERT[col])
                elif "What would you say to ensure a listener doesn't share this information with someone else" in column_id:
                    user_data[i]['controls'][k]['privacy_phrase'].append(col)
                elif 'Which factor(s) most influenced your responses for this scenario/conversation' in column_id:
                    user_data[i]['controls'][k]['factors'].append(col)
                elif 'Timing - ' in column_id:
                    pass
                elif 'In responding to this question, please select' in column_id:
                    if attention_checks[column_id] != col:
                        # print(attention_checks[column_id], column, i)
                        user_data[i]['attention_check_pass'] += 1
                elif 'In responding to this question, please type' in column_id:
                    if len(get_close_matches(attention_checks[column_id], [col])) < 1:
                        # print(attention_checks[column_id], column, i)
                        user_data[i]['attention_check_pass'] += 1
            if j >= 596 and j < 817: # Privacy scenarios
                if 'withholding' in column_id or 'withheld' in column_id:
                    user_data[i]['scenarios'][k]['withholding'] = True
                elif 'shared' in column_id:
                    user_data[i]['scenarios'][k]['withholding'] = False
                if 'This conversation is realistic' in column_id:
                    user_data[i]['scenarios'][k] = {'realistic': [], 'sensitive': [], 'privacy_violated': [], 'appropriate_share': [],
                                 'negative_consequences': [], 'comfortable': [], 'trust_share': [], 'privacy_phrase': [], 'factors': []}
                    user_data[i]['scenarios'][k]['realistic'].append(LIKERT[col])
                    all_cronbach_data[k]['q8'].append(LIKERT[col])
                elif 'This conversation contains sensitive content' in column_id:
                    user_data[i]['scenarios'][k]['sensitive'].append(LIKERT[col])
                    all_cronbach_data[k]['q9'].append(LIKERT[col])
                elif 'should not have' in column_id and 'this information' in column_id:
                    if user_data[i]['scenarios'][k]['withholding']:
                        user_data[i]['scenarios'][k]['appropriate_share'].append(INVERT[LIKERT[col]])
                        all_cronbach_data[k]['q10'].append(INVERT[LIKERT[col]])
                    else:
                        user_data[i]['scenarios'][k]['appropriate_share'].append(LIKERT[col])
                        all_cronbach_data[k]['q10'].append(LIKERT[col])
                elif 'privacy has been violated' in column_id:
                    user_data[i]['scenarios'][k]['privacy_violated'].append(LIKERT[col])
                    all_cronbach_data[k]['q11'].append(LIKERT[col])
                elif 'There could be negative consequences to' in column_id:
                    if user_data[i]['scenarios'][k]['withholding']:
                        user_data[i]['scenarios'][k]['negative_consequences'].append(INVERT[LIKERT[col]])
                        all_cronbach_data[k]['q12'].append(INVERT[LIKERT[col]])
                    else:
                        user_data[i]['scenarios'][k]['negative_consequences'].append(LIKERT[col])
                        all_cronbach_data[k]['q12'].append(LIKERT[col])
                elif 'I would feel comfortable sharing personal information with' in column_id:
                    user_data[i]['scenarios'][k]['comfortable'].append(LIKERT[col])
                    all_cronbach_data[k]['q13'].append(LIKERT[col])
                elif 'I would trust' in column_id:
                    user_data[i]['scenarios'][k]['trust_share'].append(LIKERT[col])
                    all_cronbach_data[k]['q14'].append(LIKERT[col])
                elif 'What would you say' in column_id:
                    user_data[i]['scenarios'][k]['privacy_phrase'].append(col)
                elif 'Which factor(s) most influenced your responses for this scenario/conversation' in column_id:
                    user_data[i]['scenarios'][k]['factors'].append(col)
                elif 'Timing - ' in column_id:
                    pass
                elif 'In responding to this question, please select' in column_id:
                    if attention_checks[column_id] != col:
                        # print(attention_checks[column_id], column, i)
                        user_data[i]['attention_check_pass'] += 1
                elif 'In responding to this question, please type' in column_id:
                    if len(get_close_matches(attention_checks[column_id], [col])) < 1:
                        # print(attention_checks[column_id], column, i)
                        user_data[i]['attention_check_pass'] += 1
            if j >= 817 and j < 829: # Privacy questionnaire
                if 'I tell some of my work colleagues about my personal life' in column_id:
                    privacy_dict[i]['colleagues'] = INVERT[LIKERT[col]]
                    privacy_cronbach['q1'].append(INVERT[LIKERT[col]])
                elif 'No organization or person should disseminate personal information about me without my knowledge' in column_id:
                    privacy_dict[i]['disseminate'] = LIKERT[col]
                    privacy_cronbach['q2'].append(LIKERT[col])
                elif 'I worry about the possibility that my conversations will be overheard' in column_id:
                    privacy_dict[i]['overheard'] = LIKERT[col]
                    privacy_cronbach['q3'].append(LIKERT[col])
                elif "I frequently question why I'm providing personal information" in column_id:
                    privacy_dict[i]['questioning'] = LIKERT[col]
                    privacy_cronbach['q4'].append(LIKERT[col])
                elif 'Video cameras should be used in public places to improve public safety and security' in column_id:
                    privacy_dict[i]['videocameras'] = INVERT[LIKERT[col]]
                    privacy_cronbach['q5'].append(INVERT[LIKERT[col]])
                elif "Insurance companies should not have access to people's health records" in column_id:
                    privacy_dict[i]['insurance'] = LIKERT[col]
                    privacy_cronbach['q6'].append(LIKERT[col])
                elif 'Employers should be able to monitor employee email' in column_id:
                    privacy_dict[i]['employers'] = INVERT[LIKERT[col]]
                    privacy_cronbach['q7'].append(INVERT[LIKERT[col]])
                elif 'It is ok to use messaging services even if the messages could in principle be tracked' in column_id:
                    privacy_dict[i]['messaging'] = INVERT[LIKERT[col]]
                    privacy_cronbach['q8'].append(INVERT[LIKERT[col]])
            if j >= 829 and j < 837: # Demographics
                if 'Describe your gender' in column_id:
                    demographics_dict[i]['gender'] = col
                elif 'Describe your race/ethnicity' in column_id:
                    demographics_dict[i]['ethnicity'] = col
                elif 'What is your age in years' in column_id:
                    if int(col) > 200:
                        age = 2021 - int(col)
                    else:
                        age = int(col)
                    demographics_dict[i]['age'] = age
                elif 'Please pick your highest educational qualification' in column_id:
                    demographics_dict[i]['education'] = col
                elif 'What is your occupation' in column_id:
                    demographics_dict[i]['occupation'] = col
            if j == 838: # MTurk ID
                user_data[i]['mturk_id'] = column
# print(attention_checks)
temp = user_data.copy()
np.savez('data/issues_dataset.npz', user_data=user_data)
for user, val in user_data.items():
    if user in [19, 61, 74, 75, 99, 54, 165] or val['mturk_id'] in ['A237PUN7791D62', 'A2VK6M2FDMPG54', 'A46PRT7P1Q26Jv', 'A36OFM4AUCL6T9', 'AA0K396OP72HW', 'ABOGAPD5T5L6T', 'A2OVX9UW5WANQE']:
        continue
    if val['attention_check_pass'] >= 1:
        # print(user, val['mturk_id'], val['duration'], val['attention_check_pass'])
        del privacy_dict[user]
        del demographics_dict[user]
        del temp[user]
    elif val['duration'] < 250:
        # print(user, val['mturk_id'], val['duration'], val['attention_check_pass'])
        del privacy_dict[user]
        del demographics_dict[user]
        del temp[user]
user_data = temp

for user, user_dict in user_data.items():
    for block, block_dict in user_dict['controls'].items():
        if block not in controls_dict:
            controls_dict[block] = {}
        for question, answers in block_dict.items():
            if question not in controls_dict[block]:
                controls_dict[block][question] = []
            for i in answers:
                controls_dict[block][question].append(i)
    for block, block_dict in user_dict['scenarios'].items():
        if block not in scenarios_dict:
            scenarios_dict[block] = {}
        for question, answers in block_dict.items():
            if question != 'withholding':
                if question not in scenarios_dict[block]:
                    scenarios_dict[block][question] = []
                for i in answers:
                    scenarios_dict[block][question].append(i)

val1 = []
val2 = []
val3 = []
val4 = []

temp = [privacy_cronbach['q1'], privacy_cronbach['q2'], privacy_cronbach['q3'], privacy_cronbach['q4'], privacy_cronbach['q5'], privacy_cronbach['q6'], privacy_cronbach['q7'], privacy_cronbach['q8']]
print(CronbachAlpha(temp))

for k in range(1, 43):
    cronbach_data = all_cronbach_data[k]
    temp = [cronbach_data['q2'], cronbach_data['q3']]
    val1.append(CronbachAlpha(temp))
    temp = [cronbach_data['q2'], cronbach_data['q3'], cronbach_data['q4'], cronbach_data['q5']]
    val2.append(CronbachAlpha(temp))
for k in range(1, 17):
    cronbach_data = all_cronbach_data[k]
    temp = [cronbach_data['q9'], cronbach_data['q11']]
    val3.append(CronbachAlpha(temp))
    temp = [cronbach_data['q9'], cronbach_data['q10'], cronbach_data['q11'], cronbach_data['q12']]
    val4.append(CronbachAlpha(temp))
print(np.median(val1))
print(np.median(val2))
print(np.median(val3))
print(np.median(val4))
val1.extend(val3)
print(np.median(val1))



def joint_sort(list1, list2):
    zipped_lists = zip(list1, list2)
    sorted_pairs = sorted(zipped_lists)

    tuples = zip(*sorted_pairs)
    list1, list2 = [list(t) for t in tuples]
    return list1, list2

control_levels = {'low': 0, 'moderate': 0, 'high': 0}
scen_num = []
scen_val = []
for num, val in tqdm(controls_dict.items()):
    answer_factors = []
    answer_factors.extend(controls_dict[num]['sensitive'])
    answer_factors.extend(controls_dict[num]['privacy_violated'])
    label_counts = {'low': 0, 'moderate': 0, 'high': 0}
    for i in answer_factors:
        if i < 2:
            label_counts['low'] += 1
        elif i > 4:
            label_counts['high'] += 1
        else:
            label_counts['moderate'] += 1
    pred = max(label_counts, key=label_counts.get)
    # pred = np.median(answer_factors)
    # print(pred)
    # if pred < 3.5:
    #     pred = 'low'
    # elif pred > 4.5:
    #     pred = 'high'
    # else:
    #     pred = 'moderate'
    control_levels[pred] += 1
    print(num, pred)
    scen_num.append(num)
    scen_val.append((pred,))
print(joint_sort(scen_num, scen_val))
print(control_levels)
exit()

np.savez('data/dataset.npz', index_dict=index_dict, user_data=user_data, controls_metadata=controls_metadata, controls_dict=controls_dict,
    scenarios_metadata=scenarios_metadata, scenarios_dict=scenarios_dict, privacy_dict=privacy_dict, demographics_dict=demographics_dict,
    attention_checks=attention_checks)

controls_count = {'low': 0, 'moderate': 0, 'high': 0}
labels = []

for num, val in tqdm(controls_metadata.items()):
    outdir = 'data/control{}'.format(num)
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    with open('data/metadata/control{}.py'.format(num), 'w') as metadata_file:
        metadata_file.write('from datetime import datetime, timedelta\n')
        metadata_file.write('from src.conversation import Information\n\n\n')
        metadata_file.write('speakers = {')
        for i, text in enumerate(val['text']):
            with open(os.path.join(outdir, '{}.txt'.format(i + 1)), 'w') as outfile:
                outfile.write(text)
            metadata_file.write("{}: '{}', ".format(i + 1, val['speaker'][i]))
        metadata_file.write('}\n')
        metadata_file.write('listeners = [')
        for name in val['names']:
            metadata_file.write("'{}', ".format(name))
        metadata_file.write(']\n')
        metadata_file.write('relationships = [')
        for relationship in val['relationships']:
            metadata_file.write("'{}', ".format(relationship[1]))
        metadata_file.write(']\n')
        metadata_file.write('topics = [')
        nlp = Google_NLP(text=val['all_text'], verbose=False)
        response = nlp.get_topic()
        topics = response.categories
        for topic in topics:
            metadata_file.write("'{}', ".format(topic.name.split('/')[1]))
        metadata_file.write(']\n')
        response = nlp.get_sentiment()
        metadata_file.write('sentiment_score = {}\n'.format(response.score))
        metadata_file.write('sentiment_magnitude = {}\n'.format(response.magnitude))
        sentiment = response.score * response.magnitude
        if sentiment < -0.6:
            sentiment_value = 'negative'
        elif sentiment < -0.3:
            sentiment_value = 'slightly_negative'
        elif sentiment >= -0.3 and sentiment <= 0.3:
            sentiment_value = 'neutral'
        elif sentiment > 0.6:
            sentiment_value = 'positive'
        elif sentiment > 0.3:
            sentiment_value = 'slightly_positive'
        metadata_file.write("sentiment_value = '{}'\n".format(sentiment_value))
        metadata_file.write("location = '{}'\n".format(val['location']))
        if len(val['all_text']) < 300:
            detail = 'short'
        elif len(val['all_text']) < 500:
            detail = 'medium'
        elif len(val['all_text']) >= 500:
            detail = 'long'
        metadata_file.write("detail = '{}'\n".format(detail))
        means = []
        realistic = 0
        for question, answers in controls_dict[num].items():
            # if question == 'sensitive' or question == 'privacy_violated':
            if question != 'factors' and question != 'privacy_phrase' and question != 'realistic' and question != 'close_share' and question != 'distant_share':
                means.append(np.mean(answers))
            if question == 'realistic':
                realistic = np.mean(answers)
        mean_label = np.mean(means)
        labels.append(mean_label)
        metadata_file.write('mean_label = {}\n'.format(mean_label))
        if mean_label < 2.3:
            control_level = 'low'
            controls_count['low'] += 1
        elif mean_label >= 2.3 and mean_label <= 3.1:
            control_level = 'moderate'
            controls_count['moderate'] += 1
        elif mean_label > 3.1:
            control_level = 'high'
            controls_count['high'] += 1
        # if mean_label < 3.0:
        #     control_level = 'low'
        #     controls_count['low'] += 1
        # elif mean_label >= 3.0 and mean_label <= 4.0:
        #     control_level = 'moderate'
        #     controls_count['moderate'] += 1
        # elif mean_label > 4.0:
        #     control_level = 'high'
        #     controls_count['high'] += 1
        metadata_file.write("control_level = '{}'\n".format(control_level))
        metadata_file.write('realistic_label = {}\n\n'.format(realistic))
        metadata_file.write('timestamps = {\n')
        delta = 0
        for i, speaker in enumerate(val['speaker']):
            metadata_file.write('    {}: datetime.utcnow() + timedelta(seconds={}),\n'.format(i + 1, delta))
            delta += 5
        metadata_file.write('}\n\n')
        metadata_file.write('INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)\n')

scenarios_count = {'low': 0, 'moderate': 0, 'high': 0}

for num, val in tqdm(scenarios_metadata.items()):
    outdir = 'data/scenario{}'.format(num)
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    with open('data/metadata/scenario{}.py'.format(num), 'w') as metadata_file:
        metadata_file.write('from datetime import datetime, timedelta\n')
        metadata_file.write('from src.conversation import Information\n\n\n')
        metadata_file.write('speakers = {')
        for i, text in enumerate(val['text']):
            with open(os.path.join(outdir, '{}.txt'.format(i + 1)), 'w') as outfile:
                outfile.write(text)
            metadata_file.write("{}: '{}', ".format(i + 1, val['speaker'][i]))
        metadata_file.write('}\n')
        metadata_file.write('listeners = [')
        for name in val['names']:
            metadata_file.write("'{}', ".format(name))
        metadata_file.write(']\n')
        metadata_file.write('relationships = [')
        for relationship in val['relationships']:
            metadata_file.write("'{}', ".format(relationship[1]))
        metadata_file.write(']\n')
        metadata_file.write('topics = [')
        nlp = Google_NLP(text=val['all_text'], verbose=False)
        response = nlp.get_topic()
        topics = response.categories
        for topic in topics:
            metadata_file.write("'{}', ".format(topic.name.split('/')[1]))
        metadata_file.write(']\n')
        response = nlp.get_sentiment()
        metadata_file.write('sentiment_score = {}\n'.format(response.score))
        metadata_file.write('sentiment_magnitude = {}\n'.format(response.magnitude))
        sentiment = response.score * response.magnitude
        if sentiment < -0.6:
            sentiment_value = 'negative'
        elif sentiment < -0.3:
            sentiment_value = 'slightly_negative'
        elif sentiment >= -0.3 and sentiment <= 0.3:
            sentiment_value = 'neutral'
        elif sentiment > 0.6:
            sentiment_value = 'positive'
        elif sentiment > 0.3:
            sentiment_value = 'slightly_positive'
        metadata_file.write("sentiment_value = '{}'\n".format(sentiment_value))
        metadata_file.write("location = '{}'\n".format(val['location']))
        metadata_file.write("detail = '{}'\n".format(detail))
        means = []
        realistic = 0
        for question, answers in scenarios_dict[num].items():
            # if question == 'sensitive' or question == 'privacy_violated':
            if question != 'factors' and question != 'privacy_phrase' and question != 'realistic' and question != 'trust_share' and question != 'comfortable':
                means.append(np.mean(answers))
            if question == 'realistic':
                realistic = np.mean(answers)
        mean_label = np.mean(means)
        labels.append(mean_label)
        metadata_file.write('mean_label = {}\n'.format(mean_label))
        if mean_label < 2.3:
            control_level = 'low'
            scenarios_count['low'] += 1
        elif mean_label >= 2.3 and mean_label <= 3.1:
            control_level = 'moderate'
            scenarios_count['moderate'] += 1
        elif mean_label > 3.1:
            control_level = 'high'
            scenarios_count['high'] += 1
        # if mean_label < 3.0:
        #     control_level = 'low'
        #     scenarios_count['low'] += 1
        # elif mean_label >= 3.0 and mean_label <= 4.0:
        #     control_level = 'moderate'
        #     scenarios_count['moderate'] += 1
        # elif mean_label > 4.0:
        #     control_level = 'high'
        #     scenarios_count['high'] += 1
        metadata_file.write("control_level = '{}'\n".format(control_level))
        metadata_file.write('realistic_label = {}\n\n'.format(realistic))
        metadata_file.write('timestamps = {\n')
        delta = 0
        for i, speaker in enumerate(val['speaker']):
            metadata_file.write('    {}: datetime.utcnow() + timedelta(seconds={}),\n'.format(i + 1, delta))
            delta += 5
        metadata_file.write('}\n\n')
        metadata_file.write('INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)\n')
print(controls_count)
print(scenarios_count)
print(max(labels))
print(np.mean(labels))
print(np.median(labels))
print(min(labels))
# print(scenarios_dict)
# print(user_data)
# for key, val in demographics_dict.items():
#     print(key, val)
