import os
from flask import Flask,render_template,request,jsonify
import pickle
import numpy as np

app = Flask(__name__, instance_relative_config=True)
# model = pickle.load(open('.pkl','rb'))

"""
#Tell the terminal what application to run
export FLASK_APP=main.py
#Tell the terminal what application to run for windows
set FLASK_APP=main.py
#Run the application
flask run
"""

@app.route('/')
def home():
    """
    required inputs
    []
    """
    return render_template('home.html')



@app.route('/predict', methods=['POST'])
def predict():

    # convert featuers entered into int

    int_featuers = [float(x) for x in request.form.values()]
    print(int_featuers)
    # convert the values to an array
    # final_features = [np.array(int_featuers)]

    # prediction = model.predict(final_features)


    # return render_template('predict.html', prediction_answer = answer)
    return render_template('prediction.html')

if __name__ == '__main__':
    app.run(debug=True)