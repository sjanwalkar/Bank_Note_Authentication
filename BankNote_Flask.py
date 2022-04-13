#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 19:34:53 2022

@author: sachin
"""

from flask import Flask, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
pickle_in =open('RF_classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return 'Welcome All'

@app.route('/predict')
def bank_note_authentication():
    variance = request.args.get('var')
    skewness = request.args.get('skew')
    curtosis = request.args.get('cur')
    entropy = request.args.get('ent')
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    return 'The Predcited value is '+str(prediction)

@app.route('/predict_file', methods=['POST'])
def predict_note_file():
    df_test = pd.read_csv(request.files.get('file'))
    prediction = classifier.predict(df_test)
    return 'The predicted values for csv is '+str(list(prediction))

if __name__ == '__main__':
    app.run() 