from flask_wtf import FlaskForm
from wtforms import ( StringField, SelectField, SubmitField, IntegerField)
from wtforms.validators import (DataRequired, Length, Email)

class Signupform(FlaskForm):
    Username= StringField("Patient_name", validators=[DataRequired(), Length(2,30)])
    Gender= SelectField("Gender 0:male, 1:female", choices=[0,1])
    Age= IntegerField("Age", validators=[DataRequired()])
    list_names=['SMOKING','YELLOW_FINGERS','PEER_PRESSURE','CHRONIC DISEASE', 'FATIGUE ', 'ALLERGY ', 'WHEEZING',
       'ALCOHOL CONSUMING', 'COUGHING', 'SHORTNESS OF BREATH',
       'SWALLOWING DIFFICULTY', 'CHEST PAIN']
    for field in list_names:
        locals()[field]= SelectField(field,choices=[1,2], validators=[DataRequired()])
    submit= SubmitField('submit')


       
