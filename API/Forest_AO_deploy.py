#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 22:41:10 2019

@author: AndresObando
"""

import pandas as pd
from sklearn.externals import joblib
#import sys
import os

# Year', 'Mileage', 'State', 'Make', 'Model'
def predict_tree(year,mileage,state,make,model):
    
    tree = joblib.load(os.path.dirname(__file__) + '/RandomForest_AO.pkl') 
    
    #Features:
    columns=['Year', 'Mileage', 'State', 'Make', 'Model']
    data = pd.DataFrame(data=[[year,mileage,state,make,model]], columns=columns)

    data['State'] = pd.factorize(data.State)[0]
    data['Make'] = pd.factorize(data.Make)[0]
    data['Model'] = pd.factorize(data.Model)[0]

    # Make prediction
    p1 = tree.predict(data)[0]

    return p1

#Testing
p=predict_tree(2014,31909,'MD','Nissan',0)
print(p)