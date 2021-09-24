import numpy as np


infile = np.load('data/issues_dataset.npz', allow_pickle=True)
user_data = infile['user_data'].item()

mturk_id = 'A2OVX9UW5WANQE'
user_id = 165
if user_data[user_id]['mturk_id'] == mturk_id:
    print(user_data[user_id])
