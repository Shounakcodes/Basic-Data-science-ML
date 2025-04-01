from flask import Flask,redirect, url_for, render_template, flash, request
from forms import Form_pred
import pickle
import numpy as np

titles=['Mr','Mrs']
results=['No Heart attack','Heart attack']
mean= [65,132.63,248.82,139.22]
sd=[28,17.7,65.66,23.75]

model= pickle.load(open("trained_model.pickle",'rb'))
app = Flask(__name__)
app.config['SECRET_KEY']='Key'
@app.route("/")
def home():
    return render_template('home.html', title= 'Home')

@app.route("/signup", methods=['POST','GET'])
def signup():
    form_obj= Form_pred()
    index=0
    if( form_obj.validate_on_submit()):
        form_values= [x for x in request.form.values()]
        form_values= np.array(form_values[2:])
        X_array= form_values[:-1].astype(int)
        X_array= X_array.reshape(1,-1)
        print(X_array)
        for i in range(0,len(X_array[0])):
            if(i==0 or i==3 or i==4 or i==7):
                X_array[0,i]= (X_array[0,i]- mean[index])/sd[index]
                index=index+1

        print(X_array)
        Y_pred=model.predict(X_array)
        flash(f'Thank you for your response {titles[int(form_obj.Gender.data)]} {form_obj.Patient_name.data} you have {results[int(Y_pred)]}')



        return redirect(url_for('home'))
    return render_template("signup.html", title='Signup', form= form_obj)

if __name__== '__main__':
    app.run(debug=True)
