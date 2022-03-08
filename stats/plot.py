import csv, os
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from data.convert_occupations import CONVERT as OCCUPATIONS


# EDUCATION_CONVERT = {'bachelor\'s degree': 'Bachelor\'s', 'some college': }


def plot_question_answers(infile):
    scenarios = infile['scenarios_dict'].item()
    df_data = {'questions': [], 'answers': []}
    for scenario, questions in scenarios.items():
        for question, answers in questions.items():
            if question != 'privacy_phrase' and question != 'factors':
                for ans in answers:
                    df_data['questions'].append(question)
                    df_data['answers'].append(ans)
        print(scenario)
        break
    plt.tight_layout()
    sns.despine()
    plt.title('Questions and Answers')
    df = pd.DataFrame({'Answers': df_data['answers'], 'Questions': df_data['questions']})
    sns.boxplot(data=df, y='Answers', x='Questions', showfliers=False)
    plt.savefig('data/plots/questions_answers.png', bbox_inches='tight')

def plot_realism(infile):
    scenarios = infile['scenarios_dict'].item()
    df_data = {'scenarios': [], 'answers': []}
    for scenario, questions in scenarios.items():
        for ans in questions['realistic']:
            df_data['scenarios'].append(scenario)
            df_data['answers'].append(ans)
    scenarios = infile['controls_dict'].item()
    for scenario, questions in scenarios.items():
        for ans in questions['realistic']:
            df_data['scenarios'].append(scenario)
            df_data['answers'].append(ans)
    plt.tight_layout()
    sns.despine()
    plt.title('Questions and Answers')
    df = pd.DataFrame({'Answers': df_data['answers'], 'Scenarios': df_data['scenarios']})
    sns.boxplot(data=df, y='Answers', x='Scenarios', showfliers=False)
    plt.savefig('data/plots/realistic.png', bbox_inches='tight')

def plot_question_answers_conditioned(infile):
    scenarios = infile['scenarios_dict'].item()
    df_data = {'questions': [], 'answers': []}
    for scenario, questions in scenarios.items():
        for question, answers in questions.items():
            if question != 'privacy_phrase' and question != 'factors':
                for ans in answers:
                    df_data['questions'].append(question)
                    df_data['answers'].append(ans)
        print(scenario)
        break
    df = pd.DataFrame({'answers': df_data['answers'], 'questions': df_data['questions']})
    sns.boxplot(data=df, y='answers', x='questions', showfliers=False)

def plot_privacy_inclination(infile):
    privacy_dict = infile['privacy_dict'].item()
    df_data = {'questions': [], 'answers': []}
    for user, questions in privacy_dict.items():
        for question, answer in questions.items():
            df_data['questions'].append(question)
            df_data['answers'].append(answer)
    df = pd.DataFrame({'Answers': df_data['answers'], 'Questions': df_data['questions']})
    sns.displot(data=df, y='Questions', hue='Answers', multiple='dodge', hue_order=['0', '1', '2', '3', '4', '5', '6'])
    # plt.ylim(-1, 8)
    plt.tight_layout()
    sns.despine()
    plt.title('Privacy Inclination')
    plt.savefig('data/plots/privacy_inclination.png', bbox_inches='tight')

def plot_age(infile):
    demographics_dict = infile['demographics_dict'].item()
    df_data = {'age': [], 'gender': [], 'ethnicity': [], 'education': [], 'occupation': []}
    for user, questions in demographics_dict.items():
        df_data['age'].append(questions['age'])
    df = pd.DataFrame({'Age': df_data['age']})
    sns.displot(data=df, x='Age')
    plt.tight_layout()
    sns.despine()
    plt.title('Age Distribution')
    plt.savefig('data/plots/age.png', bbox_inches='tight')

def plot_gender(infile):
    demographics_dict = infile['demographics_dict'].item()
    df_data = {'age': [], 'gender': [], 'ethnicity': [], 'education': [], 'occupation': []}
    for user, questions in demographics_dict.items():
        df_data['gender'].append(questions['gender'])
    df = pd.DataFrame({'Gender': df_data['gender']})
    sns.displot(data=df, x='Gender')
    plt.tight_layout()
    sns.despine()
    plt.title('Gender Distribution')
    plt.savefig('data/plots/gender.png', bbox_inches='tight')

def plot_ethnicity(infile):
    demographics_dict = infile['demographics_dict'].item()
    df_data = {'age': [], 'gender': [], 'ethnicity': [], 'education': [], 'occupation': []}
    for user, questions in demographics_dict.items():
        df_data['ethnicity'].append(questions['ethnicity'])
    df = pd.DataFrame({'Ethnicity': df_data['ethnicity']})
    sns.displot(data=df, x='Ethnicity')
    plt.tight_layout()
    sns.despine()
    plt.title('Ethnicity Distribution')
    plt.xticks(rotation=45, horizontalalignment='right')
    plt.savefig('data/plots/ethnicity.png', bbox_inches='tight')

def plot_education(infile):
    demographics_dict = infile['demographics_dict'].item()
    df_data = {'age': [], 'gender': [], 'ethnicity': [], 'education': [], 'occupation': []}
    for user, questions in demographics_dict.items():
        df_data['education'].append(questions['education'])
    df = pd.DataFrame({'Education': df_data['education']})
    sns.displot(data=df, x='Education', row_order=['some high school', 'high school', 'some college', 'associate\'s degree', 'bachelor\'s degree', 'graduate degree'])
    plt.tight_layout()
    sns.despine()
    plt.title('Education Distribution')
    plt.xticks(rotation=45, horizontalalignment='right')
    plt.savefig('data/plots/education.png', bbox_inches='tight')

def plot_occupation(infile):
    demographics_dict = infile['demographics_dict'].item()
    df_data = {'age': [], 'gender': [], 'ethnicity': [], 'education': [], 'occupation': []}
    for user, questions in demographics_dict.items():
        for key, val in OCCUPATIONS.items():
            if questions['occupation'] in val:
                df_data['occupation'].append(key)
    df = pd.DataFrame({'Occupation': df_data['occupation']})
    sns.displot(data=df, x='Occupation')
    plt.tight_layout()
    sns.despine()
    plt.title('Occupation Distribution')
    plt.xticks(rotation=45, horizontalalignment='right')
    plt.savefig('data/plots/occupation.png', bbox_inches='tight')

def plot_scenario_factors(infile):
    scenarios = infile['scenarios_dict'].item()
    df_data = {'scenarios': [], 'answers': []}
    for scenario, questions in scenarios.items():
        for answers in questions['factors']:
            for ans in answers.split(','):
                df_data['scenarios'].append(scenario)
                df_data['answers'].append(ans)
    df = pd.DataFrame({'scenarios': df_data['scenarios'], 'Answers': df_data['answers']})
    sns.displot(data=df, y='Answers', hue='scenarios', multiple='dodge')
    plt.tight_layout()
    sns.despine()
    plt.title('Factors Distribution')
    plt.savefig('data/plots/factors.png', bbox_inches='tight')

def plot_duration(infile):
    datas = infile['user_data'].item()
    df_data = {'duration': []}
    for user, data in datas.items():
        df_data['duration'].append(data['duration'])
    df = pd.DataFrame({'duration': df_data['duration']})
    sns.boxplot(data=df, x='duration', showfliers=False)
    plt.tight_layout()
    sns.despine()
    plt.title('Duration')
    plt.savefig('data/plots/duration.png', bbox_inches='tight')

def plot_phase2_privacy(df):
    sns.displot(data=df, y='Privacy', x='Scenario Num', col='Type', binwidth=(0.95, 0.5), cbar=True)
    plt.tight_layout()
    plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
    sns.despine()
    # plt.title('Factors Distribution')
    plt.savefig('data/plots/phase2_privacy.png', bbox_inches='tight')

def plot_phase2_trust(df):
    sns.displot(data=df, y='Trust', x='Scenario Num', col='Type', binwidth=(0.95, 0.5), cbar=True)
    plt.tight_layout()
    plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
    sns.despine()
    # plt.title('Factors Distribution')
    plt.savefig('data/plots/phase2_trust.png', bbox_inches='tight')

def plot_phase2_social_norms(df):
    sns.displot(data=df, y='Social Norms', x='Scenario Num', col='Type', binwidth=(0.95, 0.5), cbar=True)
    plt.tight_layout()
    plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
    sns.despine()
    # plt.title('Factors Distribution')
    plt.savefig('data/plots/phase2_social_norms.png', bbox_inches='tight')

sns.set(font_scale=1.3, style='ticks')
plt.style.use('seaborn-muted')
# MUTED=["#4878D0", "#EE854A", "#6ACC64", "#D65F5F", "#956CB4", "#8C613C", "#DC7EC0", "#797979", "#D5BB67", "#82C6E2", "#AED4C9", "#59599C"]
# sns.color_palette(MUTED)
infile = np.load('data/dataset2.npz', allow_pickle=True)
plot_duration(infile)
df = pd.read_csv('data/phase2_out.csv')
df = df.where(df['Privacy Inclination'] == 'Privacy Conscious').dropna()
plot_phase2_privacy(df)
plot_phase2_trust(df)
plot_phase2_social_norms(df)

# plt.tight_layout()
# sns.despine()
# plt.legend(frameon=False)
# g.legend().frameon = False
# g.fig.get_axes()[0].set_title('')
# g.fig.get_axes()[1].set_title('')
# plt.title('ECDF {} {} {}'.format(params['folder'].upper(), params['attribute'].capitalize(), samediff))
# plt.ylim(0, 0.15)
# plt.xlim(0, 6)
# plt.savefig('data/testplot.png', bbox_inches='tight')
