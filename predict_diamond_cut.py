import os
import pickle
import warnings
import pandas as pd

from flask import Flask, request, jsonify
from json import loads, dumps
from io import StringIO
from collections import defaultdict
from ml_framework.data_classification.run_eda_classification import ClassificationEDA
from ml_framework.data_classification.logistic_regression import LogisticRegressionClassifier
from ml_framework.data_classification.knn_classifier import KNN_Classifier
from ml_framework.data_classification.decision_tree_classifier import DecisionTreeClassifier
from ml_framework.data_classification.random_forest_classifier import RandomForestClassifier
from ml_framework.data_classification.support_vector_classifier import SupportVectorClassifier
from ml_framework.data_classification.xgboost_classifier import XGBoostClassifier

# Load the data analyzer for classification of diamnond cut
analyzer_filepath = "Stored_Models/Classification_Analyzer.bin"
target_col_name = "cut"
cut_decoding = {
    0:"Fair",
    1:"Good",
    2:"Very Good",
    3:"Premium",
    4:"Ideal",
}

# List the classifiers
classifiers_ls = [
    "LogisticRegressionClassifier",
    "KNN_Classifier",
    "DecisionTreeClassifier",
    "RandomForestClassifier",
    "XGBoostClassifier",
    "ANN_TF_Classifier",
    "SupportVectorClassifier",
]
classifiers_ls = [
    "LogisticRegressionClassifier",
    "KNN_Classifier",
    "DecisionTreeClassifier",
    "RandomForestClassifier",
    "XGBoostClassifier",
    "SupportVectorClassifier",
]

with open(analyzer_filepath, 'rb') as f_in:
    data_analyzer= pickle.load(f_in)
target_col_name = 'cut'
dummy_data_to_predict = data_analyzer.test_data.iloc[0:10,:].copy()
dummy_data_to_predict = data_analyzer.test_data.iloc[0]
dummy_data_json = dummy_data_to_predict.to_json()


# Name the Flask app
app = Flask('diamond_cut_prediction')

@app.route('/predict_diamond_cut', methods=['POST'])
def predict():
    
    data_to_predict = pd.DataFrame.from_dict([request.get_json()])
    print("data_to_predict.shape:", data_to_predict.shape)

    all_models_predictions = defaultdict(list)
    for classifier_name in classifiers_ls:
        classifier = eval(classifier_name + "(target_col_name, None, None)")
        classifier.load_model("Stored_Models/")

        print("\n********************")
        print(classifier_name)
        classifier.predict(data_to_predict)
        y_pred = int(classifier.get_predicted_values()[0])
        y_pred_decoded = cut_decoding[y_pred]
        print(f"Predicted Diamond Cut: {y_pred_decoded}")
        all_models_predictions[classifier_name].append(y_pred_decoded)
        
    return jsonify(all_models_predictions)

if __name__ == "__main__":

    # diamond_data = {
    #     "carat":2.5359554421,
    #     "cut":000000,
    #     "color":-0.8264133957,
    #     "clarity":-1.8523350869,
    #     "depth":3.5254549522,
    #     "table":-0.2046050915,
    #     "price":1.035543546,
    #     "x":1.8532134098,
    #     "y":1.738404844,
    #     "z":2.3399238012}
    
    # predict(diamond_data)
    warnings.filterwarnings('ignore')
    app.run(debug=True, host='0.0.0.0', port='9696')

    pass