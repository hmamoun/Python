import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.linear_model import LinearRegression

import warnings
warnings.filterwarnings('ignore') # to get rid of warning messages

import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt


df = pd.read_csv('sales.csv' )
df.head()
X = ['sales_in_first_month' , 'sales_in_second_month']
X= df[X]
y = df['sales_in_third_month']
model = LinearRegression().fit(X,y) 



app = Flask(__name__)
#model = pickle.load(open('model.pkl', 'rb'))
@app.route('/')






def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Sales should be $ {}'.format(output))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)