# -*- coding: utf-8 -*-


import numpy as np
from flask import Flask, request, render_template, url_for,jsonify
import pickle

import util
import math

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method=="POST":
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])
        util.load_saved_artifacts()
        util.get_location_names()
        output = util.get_estimated_price(location,total_sqft,bhk,bath)

        return render_template('index.html', prediction_text='The price would be {}'.format(math.floor(output)))


if __name__ == "__main__":
    app.run()