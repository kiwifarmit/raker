from jsonc_parser.parser import JsoncParser
import numpy as np
import pandas as pd
import random

from utils.pnds import timestamp_to_index

file_path = './config.jsonc'
config = JsoncParser.parse_file(file_path)
dataset_prefix = config['dataset_prefix']

data = pd.read_csv('./{}_training.csv'.format(dataset_prefix))
timestamp_to_index(data)
data['value'] = data['value'] + np.random.randint((-data['value'] // 20) + 1, (data['value'] // 20) + 1, data.shape[0])

data.to_csv('{}_testing.csv'.format(dataset_prefix))