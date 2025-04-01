from flask_wtf import FlaskForm
from wtforms import SearchField, IntegerField, SelectField, StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class Form_pred(FlaskForm):
    Patient_name= StringField("Patient_name", validators=[DataRequired()])
    Gender= SelectField("Gender: 0: for male, 1: for female", choices=[0,1], validators=[DataRequired()])
    Age= IntegerField('Age', validators=[DataRequired(), NumberRange(min=1)])
    list_names= ['cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
       'exang']

    for field_names in list_names:
        locals()[field_names]= FloatField(field_names,validators=[DataRequired()] )
    submit= SubmitField('submit')    



       
