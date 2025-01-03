import os
import sys
import numpy as np
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import RandomizedSearchCV
from src.exception import CustomException
# from src.logger import logging
from sklearn.metrics import (accuracy_score, confusion_matrix, recall_score, 
                             roc_auc_score, roc_curve, classification_report, precision_score, f1_score,
                             ConfusionMatrixDisplay, RocCurveDisplay)

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)

def evaluate_models(x_train, y_train, x_test, y_test, models):
    print("x_test is :->", x_train)
    print("y_test is :->",y_train)    
    try:
        report = {}

        for model_name, model in models.items():
            print(model_name)
            model.fit(x_train, y_train)  # Train model

            y_train_pred = model.predict(x_train)
            y_test_pred = model.predict(x_test)

            train_model_score = accuracy_score(y_train, y_train_pred)
            test_model_score = accuracy_score(y_test, y_test_pred)

            report[model_name] = test_model_score

        return report


    except Exception as e:
        raise CustomException(e, sys)