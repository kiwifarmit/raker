from jsonc_parser.parser import JsoncParser
import pandas as pd
from pycaret.anomaly import *

from utils.pnds import Pnds as pnds
from utils.taxi import Taxi as taxi

file_path = './config.jsonc'
config = JsoncParser.parse_file(file_path)
dataset_prefix = config['dataset_prefix']
models_folder = config['models_folder']
models_names = config['models_names']

data = pd.read_csv('./{}_training.csv'.format(dataset_prefix))
data = pnds.timestamp_to_index(data)
data = taxi.features_create(data)

for model_name in models_names:
    s = setup(data, session_id = 123, silent=True)
    model_current = create_model(model_name) #, fraction = 0.1)
    model_results = assign_model(model_current)
    save_model(model_current, '{}/{}_{}'.format(models_folder, dataset_prefix, model_name))