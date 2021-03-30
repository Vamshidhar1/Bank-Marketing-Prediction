import numpy as np
from flask import Flask,request,render_template
import pandas as pd
import joblib

#init Flask
app=Flask(__name__)

#loading model
model=joblib.load("customercampaginmodel.pkl")

#to launch home page
@app.route('/')
def home():
    #loading a HTML page
    return render_template('index.html')

#prediction page
@app.route('/y_predict',methods=['post'])
def y_predict():
    x_col=['age','job','marital','education','housing','loan','contact','duration','campaign','previous']
    data=[[x for x in request.form.values()]]
    print(data)
    data=pd.DataFrame(data,columns=x_col)
    prediction=model.predict(data)
    print(prediction)
    if prediction=="yes":
        text="Customer Subscribed"
    else:
        text="Customer Not Subscribed"
    #l=['Not Subscribed','Subscribed']
    #text=l[prediction[0]]
    return render_template('index.html',prediction_text=text)

if __name__=="__main__":
    app.run(debug=True)
