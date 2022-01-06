from jsonc_parser.parser import JsoncParser
import pandas as pd
from pycaret.anomaly import *

from utils.models import Models
from utils.pnds import Pnds as pnds
from utils.taxi import Taxi as taxi

file_path = './config.jsonc'
config = JsoncParser.parse_file(file_path)
dataset_prefix = config['dataset_prefix']
models_folder = config['models_folder']
models_names = config['models_names']

data_anomalies = pd.read_csv('./{}_testing.csv'.format(dataset_prefix))
data_anomalies = pnds.timestamp_to_index(data_anomalies)
data_anomalies = taxi.resample_hourly(data_anomalies)
data_anomalies['Outlier'] = 0

data_unseen = pd.read_csv('./{}_testing.csv'.format(dataset_prefix))
data_unseen = pnds.timestamp_to_index(data_unseen)
data_unseen = taxi.features_create(data_unseen)

models = Models(models_folder)
models_names = models.get_names()
# models_names = ['nyc_taxi_abod', 'nyc_taxi_iforest']

for model_name in models_names:
    print(model_name)
    dt_saved = load_model('{}/{}'.format(models_folder, model_name))
    prediction = predict_model(dt_saved, data = data_unseen)
    # print(prediction['Anomaly'].head(5))
    data_anomalies['Outlier'] = data_anomalies['Outlier'] + prediction['Anomaly']

# print(data_anomalies[data_anomalies['Outlier'] == data_anomalies['Outlier'].max()].head(50))  
print(data_anomalies[data_anomalies['Outlier'] > data_anomalies['Outlier'].max() // 2 + 1].head(50))
# print(data_anomalies[data_anomalies['Outlier'] > len(models_names) // 2].head(50))