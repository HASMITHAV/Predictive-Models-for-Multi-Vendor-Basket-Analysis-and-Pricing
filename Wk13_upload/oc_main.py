# -*- coding: utf-8 -*-
"""oc_main

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1c4OAg5FdyhKQHVaq53y2cFgY6tqpU371
"""

model = "modelo.pkl"
data_path = "dataset_o11.csv"

import pickle
import pandas as pd

import warnings
warnings.filterwarnings("ignore")
import joblib

rf_model = joblib.load(model)

def classify_o(feature):
    pred = rf_model.predict([feature])
    return pred[0]



