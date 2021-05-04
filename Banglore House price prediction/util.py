# -*- coding: utf-8 -*-
"""
Created on Tue May  4 19:45:28 2021

@author: Icon
"""

import json
import numpy as np
import pickle

__locations = None
__data_columns = None
__model = None


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk
        
    global __model
    if __model is None:
        
        with open('./artifacts/model.pkl','rb') as f:
            __model=pickle.load(f)
            
    print("loading saved artifacts...done")
def get_location_names():
    return __locations

def get_estimated_price(location,sqft,bhk,bath):

    loc_index = __data_columns.index(location.lower())
    

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)



if __name__ == '__main__':
    load_saved_artifacts()
    get_location_names() # list of locations
    
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))