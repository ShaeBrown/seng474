from spyder.utils.qthelpers import action2button

from .forms import GradePredictionForm
from flask import render_template
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from sklearn.naive_bayes import GaussianNB
from sklearn.externals import joblib


app = Flask(__name__)
app.secret_key = 'b\xd9\x8c\xa3\xaa\xf2\x02;q\x90Y\xb1\xf8e\xb7^\xbb(\xb1\x83\xeci\x82\x83\xc7'
csrf = CSRFProtect(app)


def load_classifiers():
    dt = joblib.load("./trained_models/decisiontree.pkl")
    # NB is not fitted and will throw error if chosen in the UI
    return {0: dt, 1: GaussianNB()}


@app.route("/", methods=["GET", "POST"])
def home():
    form = GradePredictionForm()
    clfs = load_classifiers()
    if form.validate_on_submit():
        clf_num = int(form.prediction_model.data)
        clf = clfs[clf_num]
        age = int(form.age.data)
        study_time = int(form.study_time.data)
        failures = int(form.failures.data)
        activities = int(form.activities.data)
        higher_ed = int(form.higher_ed.data)
        family_rel = int(form.family_rel.data)
        rom_rel = int(form.family_rel.data)
        free_time = int(form.free_time.data)
        go_out = int(form.go_out.data)
        absences = int(form.absences.data)
        grade = clf.predict([[age, study_time, failures, activities, higher_ed, rom_rel, family_rel, free_time, go_out, absences]])[0]
        label = {1 : "Failing", 2: "Passing", 3: "Good"}
        return render_template('graderesults.html', grade=label[int(grade)])
    return render_template('gradepredictionform.html', form=form)