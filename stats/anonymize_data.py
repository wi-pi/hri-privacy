import numpy as np
import pandas as pd


np.savez('data/dataset.npz', index_dict=index_dict, user_data=user_data, controls_metadata=controls_metadata, controls_dict=controls_dict,
    scenarios_metadata=scenarios_metadata, scenarios_dict=scenarios_dict, privacy_dict=privacy_dict, demographics_dict=demographics_dict,
    attention_checks=attention_checks)

infile = np.load('data/dataset.npz', allow_pickle=True)
index_dict = infile['index_dict'].item()
# demographics_dict = infile['demographics_dict'].item()
user_data = infile['user_data'].item()
privacy_dict = infile['privacy_dict'].item()
controls_metadata = infile['controls_metadata'].item()
controls_dict = infile['controls_dict'].item()
scenarios_metadata = infile['scenarios_metadata'].item()
scenarios_dict = infile['scenarios_dict'].item()

df_data = {'uid': [], 'scenario': [], 'scenario_num': [], 'baseline': [], 'privacy_norms': [], 'trust': [], 'conversational_norms': [], 'privacy_inclination': []}
for user, user_dict in user_data.items():
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


df = pd.DataFrame({'PID': df_data['uid'], 'Scenario': df_data['scenario'], 'Scenario Num': df_data['scenario_num'], 'Type': df_data['baseline'], 'Privacy': df_data['privacy_norms'],
                   'Trust': df_data['trust'], 'Social Norms': df_data['conversational_norms'], 'Privacy Inclination': df_data['privacy_inclination']})
df.to_csv('data/anonymous_study1.csv')
