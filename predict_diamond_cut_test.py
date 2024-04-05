import requests
import pickle
import pandas as pd

from ml_framework.data_classification.run_eda_classification import ClassificationEDA

# Load test diamon data from stored data analyzer
analyzer_filepath = "Stored_Models/Classification_Analyzer.bin"
with open(analyzer_filepath, 'rb') as f_in:
    data_analyzer= pickle.load(f_in)


test_data_idx = 30

data_to_predict = data_analyzer.test_data

diamond_data = {
    "carat":data_to_predict.iloc[test_data_idx,0],
    "cut":data_to_predict.iloc[test_data_idx,1],
    "color":data_to_predict.iloc[test_data_idx,2],
    "clarity":data_to_predict.iloc[test_data_idx,3],
    "depth":data_to_predict.iloc[test_data_idx,4],
    "table":data_to_predict.iloc[test_data_idx,5],
    "price":data_to_predict.iloc[test_data_idx,6],
    "x":data_to_predict.iloc[test_data_idx,7],
    "y":data_to_predict.iloc[test_data_idx,8],
    "z":data_to_predict.iloc[test_data_idx,9],
}

print(diamond_data)

url = "http://192.168.4.20:9696/predict_diamond_cut"
url = "http://172.30.176.211:9696/predict_diamond_cut"
url = "http://0.0.0.0:9696/predict_diamond_cut"

diamond_cut_predictions = requests.post(url, json=diamond_data).json()

print("\nDiamond Cut Predictions:")
for k,v in diamond_cut_predictions.items():
    print(k,v)



