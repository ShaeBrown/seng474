from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms import SelectField
from wtforms import BooleanField
from wtforms.validators import NumberRange
from sklearn.tree import DecisionTreeClassifier

class GradePredictionForm(FlaskForm):
    # TODO: should you have to fill in all inputs, some inputs , or at least one?
    prediction_model = SelectField(u'Prediction Model', choices=[('0', 'Decision Tree'), ('1', 'Naive Bayes')])
    age = IntegerField('Age',  validators=[NumberRange(0,99)]) # TODO: adjust for min/max age?
    study_time = SelectField(u'Study Time', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')])
    #TODO set the value to what the numbers mean for example: ('1', '10-14 hrs')
    failures = IntegerField('Number of Failures', validators=[NumberRange(0, 99)])
    activities = BooleanField('Extracurricular activities')
    higher_ed = BooleanField('Higher education')
    romantic_rel = BooleanField('Romantic relationship')
    family_rel = SelectField(u'Family relationship', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    #TODO set the value to what the numbers mean for example: ('1', 'Great')
    free_time = SelectField(u'Free time', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    #TODO set the value to what the numbers mean for example: ('1', '10-14 hrs')
    go_out = SelectField(u'Frequency of going out with friends', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    #TODO set the value to what the numbers mean for example: ('1', '5 times a week')
    absences = SelectField(u'Number of absences', choices=[('1', '0-4'), ('2', '5-9'), ('3', '10-14'), ('4', '15-19'), ('5', '20+')])
