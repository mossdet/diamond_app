FROM python:3.11.8-slim

RUN pip install poetry

WORKDIR /app
COPY ["ml_framework-0.1.0-py3-none-any.whl", "pyproject.toml", "poetry.lock", "./"]

# Copy stored models
COPY ["Stored_Models/Classification_Analyzer.bin", "Stored_Models/"]
COPY ["Stored_Models/Regression_Analyzer.bin", "Stored_Models/"]
COPY ["Stored_Models/XGBoostClassifierSavedModel", "Stored_Models/"]
COPY ["Stored_Models/XGBoostRegressorSavedModel", "Stored_Models/"]
COPY ["Stored_Models/ANN_TF_ClassifierSavedModel.keras", "Stored_Models/"]
COPY ["Stored_Models/ANN_TF_RegressorSavedModel.keras", "Stored_Models/"]
COPY ["Stored_Models/DecisionTreeClassifier_SavedModel.bin", "Stored_Models/"]
COPY ["Stored_Models/DecisionTreeRegressor_SavedModel.bin", "Stored_Models/"]
COPY ["Stored_Models/KNN_Classifier_SavedModel.bin", "Stored_Models/"]
COPY ["Stored_Models/KNN_Regressor_SavedModel.bin", "Stored_Models/"]
COPY ["Stored_Models/LinearRegressor_SavedModel.bin", "Stored_Models/"]
COPY ["Stored_Models/LogisticRegressionClassifier_SavedModel.bin", "Stored_Models/"]
COPY ["Stored_Models/RandomForestClassifier_SavedModel.bin", "Stored_Models/"]
COPY ["Stored_Models/RandomForestRegressor_SavedModel.bin", "Stored_Models/"]
COPY ["Stored_Models/SupportVectorClassifier_SavedModel.bin", "Stored_Models/"]
COPY ["Stored_Models/SupportVectorRegressor_SavedModel.bin", "Stored_Models/"]

# Copy web service App
COPY ["predict_diamond_cut.py", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict_diamond_cut:app"]

RUN poetry config virtualenvs.create false
RUN poetry install

