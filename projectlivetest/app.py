import os
from flask import Flask,render_template,request,jsonify
import pickle
import numpy as np

app = Flask(__name__, instance_relative_config=True)
model = pickle.load(open('model.pkl','rb'))

"""
#Tell the terminal what application to run
export FLASK_APP=main.py
#Tell the terminal what application to run for windows
set FLASK_APP=main.py
#Run the application
flask run

flask --app app --debug run
"""

@app.route('/')
def home():
    """
    required inputs
        Income	
        Age	
        Experience	
        Married/Single	
        House_Ownership	
        Car_Ownership	
        CURRENT_JOB_YRS	
        CURRENT_HOUSE_YRS	

    """
    return render_template('home.html')



@app.route('/predict',methods=['GET','POST'])
def predict():
    loan_featuers = []
    context = []
    if request.method == "POST":
        for key, val in request.form.items():
            loan_featuers.append(int(val))
            print(key,val)

        
    print(loan_featuers)

    # # convert the values to an array
    # final_features = [np.array(loan_featuers)]
    # print(final_features) # check
    # print("\n")
    prediction = model.predict(loan_featuers)

    print(prediction)
    answer = ''

    if prediction[0] == 0:
        answer = 'No'
    if prediction[0] == 1:
        answer = 'Yes'

    # return render_template('predict.html', prediction_answer = answer)
    return render_template('prediction.html',answer = answer)

if __name__ == '__main__':
    app.run(debug=True)