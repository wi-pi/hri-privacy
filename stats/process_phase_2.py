import csv
import os
import numpy as np
import pandas as pd
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


infile = open('data/phase2.csv', 'r')
reader = csv.reader(infile)
index_dict = {}
user_data = {}
privacy_dict = {}
demographics_dict = {}
attention_checks = {}
mapping = [(1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1), (4, 0), (4, 1), (5, 0), (6, 0), (6, 1), (7, 0), (8, 0),
           (9, 0), (10, 0), (10, 1), (11, 0), (11, 1), (12, 0), (12, 1)]
baseline_controller = {0: 'Baseline', 1: 'Controller'}
scenario_num_map = {1: 'scenario 5', 2: 'scenario 6', 3: 'scenario 9', 4: 'control 1', 5: 'control 7', 6: 'control 10',
                    7: 'control 14', 8: 'control 16', 9: 'control 25', 10: 'control 30', 11: 'control 31', 12: 'control 37'}
cronbach_data = {'q1': [], 'q2': [], 'q3': [], 'q4': [], 'q5': [], 'q6': [], 'q7': [], 'q8': [], 'q9': [], 'q10': [], 'q11': [], 'q12': []}
privacy_cronbach = {'q1': [], 'q2': [], 'q3': [], 'q4': [], 'q5': [], 'q6': [], 'q7': [], 'q8': []}


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
            if j >= 596 and j < 817: # Privacy scenarios
                if 'In responding to this question, please select' in column:
                    attention_checks[column_id] = column.split('"')[1].strip().lower()

    if i == 2:
        continue
    if i > 2:
        user_data[i] = {'attention_check_pass': 0, 'duration': 0, 'scenarios': {}}
        privacy_dict[i] = {}
        demographics_dict[i] = {}
        k = -1
        for j, column in enumerate(user):
            column_id = index_dict[j]
            col = column.strip().lower()
            if j < 360 and 'Please respond to the following statements based on your level of agreement' in column_id:
                k += 1
            if len(column) == 0:
                continue
            if j < 17: # User data
                if j == 5:
                    user_data[i]['duration'] = int(column)
            if j >= 17 and j < 29: # Timings
                pass
            if j >= 29 and j < 360: # Control scenarios
                if 'The robot kept sensitive information private' in column_id:
                    user_data[i]['scenarios'][k] = {'privacy_norms': [], 'trust': [], 'conversational_norms': []}
                    user_data[i]['scenarios'][k]['privacy_norms'].append(LIKERT[col])
                    cronbach_data['q1'].append(LIKERT[col])
                elif 'The robot violated peoples' in column_id:
                    user_data[i]['scenarios'][k]['privacy_norms'].append(INVERT[LIKERT[col]])
                    cronbach_data['q2'].append(INVERT[LIKERT[col]])
                elif 'The robot understands privacy boundaries' in column_id:
                    user_data[i]['scenarios'][k]['privacy_norms'].append(LIKERT[col])
                    cronbach_data['q3'].append(LIKERT[col])
                elif 'The robot appropriately disclosed information' in column_id:
                    user_data[i]['scenarios'][k]['privacy_norms'].append(LIKERT[col])
                    cronbach_data['q4'].append(LIKERT[col])
                elif 'The robot is trustworthy' in column_id:
                    user_data[i]['scenarios'][k]['trust'].append(LIKERT[col])
                    cronbach_data['q5'].append(LIKERT[col])
                elif 'I would feel comfortable sharing sensitive information with the robot' in column_id:
                    user_data[i]['scenarios'][k]['trust'].append(LIKERT[col])
                    cronbach_data['q6'].append(LIKERT[col])
                elif 'I would NOT share information with the robot' in column_id:
                    user_data[i]['scenarios'][k]['trust'].append(INVERT[LIKERT[col]])
                    cronbach_data['q7'].append(INVERT[LIKERT[col]])
                elif "I would feel comfortable having a conversation around the robot" in column_id:
                    user_data[i]['scenarios'][k]['trust'].append(LIKERT[col])
                    cronbach_data['q8'].append(LIKERT[col])
                elif 'responses were appropriate' in column_id:
                    user_data[i]['scenarios'][k]['conversational_norms'].append(LIKERT[col])
                    cronbach_data['q9'].append(LIKERT[col])
                elif 'speech met my expectations' in column_id:
                    user_data[i]['scenarios'][k]['conversational_norms'].append(LIKERT[col])
                    cronbach_data['q10'].append(LIKERT[col])
                elif 'The robot provided the right amount of information' in column_id:
                    user_data[i]['scenarios'][k]['conversational_norms'].append(LIKERT[col])
                    cronbach_data['q11'].append(LIKERT[col])
                elif 'I would NOT want to speak with the robot' in column_id:
                    user_data[i]['scenarios'][k]['conversational_norms'].append(INVERT[LIKERT[col]])
                    cronbach_data['q12'].append(INVERT[LIKERT[col]])
                elif 'In responding to this question, please select' in column_id:
                    if attention_checks[column_id] != col:
                        user_data[i]['attention_check_pass'] += 1

            if j >= 360 and j < 368: # Privacy questionnaire
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
                    privacy_dict[i]['messaging'] = LIKERT[col]
                    privacy_cronbach['q8'].append(LIKERT[col])

            if j >= 368 and j < 381: # Demographics
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
            if j == 381: # MTurk ID
                user_data[i]['mturk_id'] = column

temp = user_data.copy()
for user, val in user_data.items():
    if user in [19, 61, 74, 75, 99, 54, 165] or val['mturk_id'] in ['A237PUN7791D62', 'A2VK6M2FDMPG54', 'A46PRT7P1Q26Jv', 'A36OFM4AUCL6T9', 'AA0K396OP72HW', 'ABOGAPD5T5L6T', 'A2OVX9UW5WANQE']:
        continue
    if val['attention_check_pass'] >= 1:
        print(user, val['mturk_id'], val['duration'], val['attention_check_pass'])
        del privacy_dict[user]
        del demographics_dict[user]
        del temp[user]
    elif val['duration'] < 250:
        print(user, val['mturk_id'], val['duration'], val['attention_check_pass'])
        del privacy_dict[user]
        del demographics_dict[user]
        del temp[user]
user_data = temp

count = 0
privacy_count = 0
df_data = {'uid': [], 'scenario': [], 'scenario_num': [], 'baseline': [], 'privacy_norms': [], 'trust': [], 'conversational_norms': [], 'privacy_inclination': []}
for user, user_dict in user_data.items():
    count += 1
    privacy_scores = []
    for question, answer in privacy_dict[user].items():
        privacy_scores.append(answer)
    privacy_score = np.mean(privacy_scores)
    print(privacy_score)
    if privacy_score >= 3.5:
        privacy_count += 1
    for scenario, scenario_dict in user_dict['scenarios'].items():
        df_data['uid'].append(user)
        tup = mapping[scenario]
        df_data['scenario'].append(scenario_num_map[tup[0]])
        df_data['scenario_num'].append(tup[0])
        df_data['baseline'].append(baseline_controller[tup[1]])
        df_data['privacy_norms'].append(np.mean(scenario_dict['privacy_norms']))
        df_data['trust'].append(np.mean(scenario_dict['trust']))
        df_data['conversational_norms'].append(np.mean(scenario_dict['conversational_norms']))
        if privacy_score < 3.5:
            df_data['privacy_inclination'].append('Non Privacy Conscious')
        else:
            df_data['privacy_inclination'].append('Privacy Conscious')
        if tup[0] == 5 or tup[0] == 7 or tup[0] == 8 or tup[0] == 9:
            df_data['uid'].append(user)
            df_data['scenario'].append(scenario_num_map[tup[0]])
            df_data['scenario_num'].append(tup[0])
            df_data['baseline'].append(baseline_controller[1])
            df_data['privacy_norms'].append(np.mean(scenario_dict['privacy_norms']))
            df_data['trust'].append(np.mean(scenario_dict['trust']))
            df_data['conversational_norms'].append(np.mean(scenario_dict['conversational_norms']))
            if privacy_score < 3.5:
                df_data['privacy_inclination'].append('Non Privacy Conscious')
            else:
                df_data['privacy_inclination'].append('Privacy Conscious')
print(count, privacy_count)
temp = [cronbach_data['q1'], cronbach_data['q2'], cronbach_data['q3'], cronbach_data['q4']]
print(CronbachAlpha(temp))
temp = [cronbach_data['q5'], cronbach_data['q6'], cronbach_data['q7'], cronbach_data['q8']]
print(CronbachAlpha(temp))
temp = [cronbach_data['q9'], cronbach_data['q10'], cronbach_data['q11'], cronbach_data['q12']]
print(CronbachAlpha(temp))
# temp = [cronbach_data['q1'], cronbach_data['q2'], cronbach_data['q3'], cronbach_data['q4'], cronbach_data['q5'], cronbach_data['q6'], cronbach_data['q7'], cronbach_data['q8'], cronbach_data['q9'], cronbach_data['q10'], cronbach_data['q11'], cronbach_data['q12']]
# print(CronbachAlpha(temp))
temp = [privacy_cronbach['q1'], privacy_cronbach['q2'], privacy_cronbach['q3'], privacy_cronbach['q4'], privacy_cronbach['q5'], privacy_cronbach['q6'], privacy_cronbach['q7'], privacy_cronbach['q8']]
print(CronbachAlpha(temp))
temp = [privacy_cronbach['q2'], privacy_cronbach['q3'], privacy_cronbach['q4'], privacy_cronbach['q6'], privacy_cronbach['q8']]
print(CronbachAlpha(temp))
temp = [privacy_cronbach['q1'], privacy_cronbach['q2'], privacy_cronbach['q3'], privacy_cronbach['q4']]
print(CronbachAlpha(temp))
temp = [privacy_cronbach['q5'], privacy_cronbach['q6'], privacy_cronbach['q7'], privacy_cronbach['q8']]
print(CronbachAlpha(temp))

df = pd.DataFrame({'PID': df_data['uid'], 'Scenario': df_data['scenario'], 'Scenario Num': df_data['scenario_num'], 'Type': df_data['baseline'], 'Privacy': df_data['privacy_norms'],
                   'Trust': df_data['trust'], 'Social Norms': df_data['conversational_norms'], 'Privacy Inclination': df_data['privacy_inclination']})
df.to_csv('data/phase2_out.csv')

np.savez('data/dataset2.npz', index_dict=index_dict, user_data=user_data, privacy_dict=privacy_dict, demographics_dict=demographics_dict,
    attention_checks=attention_checks)