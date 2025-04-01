from flask import Flask, redirect, url_for, render_template, flash, request
from forms import Signupform
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)
app.config['SECRET_KEY']='Key'
Results=['Cancer','No_cancer']
Addressal=['Mr','Mrs']
model= pickle.load(open('Final_model.pickle','rb'))
mean, sd= 62.67313915857605,8.210301387885995

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html", title= "About", texts=None)

@app.route("/signup", methods=['GET','POST'])
def signup():
    form_obj= Signupform()
    if(form_obj.validate_on_submit()):
        
        values_net= [x for x in request.form.values()]

        final_features= np.array(values_net)[2:]
        test_features=np.array(final_features[:-1].astype('float'))
        test_feature=test_features.reshape(1,-1)
        test_feature[0,1]= (test_feature[0,1]-mean)/sd
        print('age is',test_feature[0,1])
        Y_pred= model.predict(test_feature)
        flash(f"{Addressal[int(test_features[0])]} {values_net[1]} You have {Results[int(Y_pred)]}")
        return render_template("preds.html", title= 'Results')

    return render_template("signup.html", title='Sign_up', form= form_obj)

@app.route("/Predictions")
def predictions():
    pass

if __name__== "__main__":
    app.run(debug= True)