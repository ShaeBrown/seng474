from .forms import GradePredictionForm
from flask import render_template, redirect, url_for
from flask import Flask
from flask_wtf.csrf import CSRFProtect
import os
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)
app.secret_key = 'b\xd9\x8c\xa3\xaa\xf2\x02;q\x90Y\xb1\xf8e\xb7^\xbb(\xb1\x83\xeci\x82\x83\xc7'
csrf = CSRFProtect(app)

def loadClassifiers():
	# load trained classifiers
	# an option would to train a classifier in train.py, export it using pickle and load it here
	# place holder untrained classifiers
	return {0 : GaussianNB(), 1 : DecisionTreeClassifier()}

@app.route("/", methods=["GET", "POST"])
def home():
	form = GradePredictionForm()
	clfs = loadClassifiers()
	if form.validate_on_submit():
		clf_num = int(form.prediction_model.data)
		clf = clfs[clf_num]
		age = int(form.age.data)
		study_time = int(form.study_time.data)
		failures  = int(form.failures.data)
		activities = int(form.activities.data)
		higher_ed = int(form.higher_ed.data)
		family_rel = int(form.family_rel.data)
		free_time = int(form.free_time.data)
		go_out = int(form.go_out.data)
		absences = int(form.absences.data)
		# grade = clf.predict([age, study_time, failures, activies, heigher_ed, family_rel, free_time, go_out, absences])
		grade = 88
		return render_template('graderesults.html', grade=grade)
	return render_template('gradepredictionform.html', form=form)