import numpy as np
import pandas as pd
from scipy.stats import chisquare, kstest, zscore


def test_freq_distr(df, attr):
    df1 = df[attr].where(df['Type'] == 'Baseline').dropna()
    df2 = df[attr].where(df['Type'] == 'Controller').dropna()
    df1 = df1.apply(pd.Series.value_counts, bins=[0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6]).sum()
    df2 = df2.apply(pd.Series.value_counts, bins=[0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6]).sum()
    print(df1)
    print(df2)
    print(chisquare(df1, df2))


def get_mean(df, attr):
    df1 = df[attr].where(df['Type'] == 'Baseline').dropna()
    df2 = df[attr].where(df['Type'] == 'Controller').dropna()
    print('Baseline: {}, Controller: {}'.format(np.mean(df1), np.mean(df2)))


def get_accuracy(df, attr):
    total = df.where(df['Type'] == 'Baseline').dropna()
    df = df.where(df['Type'] == 'Baseline').where(df[attr] > 2.5).dropna()
    print(df.size / total.size)
    for scen in [1,2,3,4,5,6,7,8,9,10,11,12]:
        temp = df[attr].where(df['Scenario Num'] == scen).dropna()
        totaltemp = total[attr].where(total['Scenario Num'] == scen).dropna()
        # print(temp.size / totaltemp.size)
# df1 = df['Privacy'].where(df['Type'] == 'Baseline').where(df['Scenario Num'] == 7).dropna()
# df2 = df['Privacy'].where(df['Type'] == 'Controller').where(df['Scenario Num'] == 7).dropna()
# df1 = df1.apply(pd.Series.value_counts, bins=[0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6]).sum()
# df2 = df2.apply(pd.Series.value_counts, bins=[0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6]).sum()
# .636363
# .575757
# .676767

# .272727
# .242424
# .313131
df = pd.read_csv('data/phase2_out.csv')
df = df.where(df['Privacy Inclination'] == 'Non Privacy Conscious').dropna()
get_mean(df, 'Privacy')
get_mean(df, 'Trust')
get_mean(df, 'Social Norms')
get_accuracy(df, 'Privacy')
get_accuracy(df, 'Trust')
get_accuracy(df, 'Social Norms')
test_freq_distr(df, 'Privacy')
test_freq_distr(df, 'Trust')
test_freq_distr(df, 'Social Norms')

# data1 = pd.DataFrame(np.random.uniform(0, 6, 228))
# data2 = pd.DataFrame(np.random.uniform(0, 6, 228))
# data1 = data1.apply(pd.Series.value_counts, bins=[0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6])
# data2 = data2.apply(pd.Series.value_counts, bins=[0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6])
# print(data1)
# print(data2)
# print(chisquare(data1, data2))
