# -*- coding: utf-8 -*-
"""cc_main

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19AMtqg-v8SuMfUJol7bPjvgBh69k7pKv
"""

import pickle
import pandas as pd

import warnings
warnings.filterwarnings("ignore")
import numpy as np
from sklearn.metrics import accuracy_score
import joblib

from google.colab import drive
drive.mount('/content/drive')

model = "modelc.pkl"
files_path = "c0.csv"

model = joblib.load(model)

def classify_c(value):
    class_label = model.predict([[value]])[0]
    return class_label

acc = test_model_accuracy()
print("Accuracy:", acc)