import numpy as np
from sklearn import tree
from sklearn import naive_bayes
from sklearn import metrics
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_val_predict
from sklearn.externals import joblib


def load_data():
    yn = lambda s: 1 if s == "yes" else 0
    fm = lambda s: 1 if s == "M" else 0
    data = np.loadtxt("pordate.csv", dtype=np.float64, delimiter=",", skiprows=1, converters={0: fm, 4: yn, 5: yn, 6: yn})
    X = np.delete(data, [0, len(data[0]) - 1], axis=1)
    y = data[:, -1]
    return X, y


def test_cros_val(clf, X, y):
    y_pred = cross_val_predict(clf, X, y, cv=10)
    print("Using 10 fold cross validation")
    print(metrics.classification_report(y, y_pred, target_names=["Failing", "Passing", "Doing Well"]))


def train():
    X,y = load_data()
    classifiers = {("Decision Tree", tree.DecisionTreeClassifier(), "decisiontree.pkl"),
                   ("Multinomial Bayes", naive_bayes.MultinomialNB(), "multinomialbayes.pkl"),
                   ("Support Vector Machine", SVC(), "svc.pkl"),
                   ("Multilayer Perceptron", MLPClassifier(), "mlp.pkl")}

    for name, clf, output_file in classifiers:
        print(name)
        test_cros_val(clf, X, y)
        clf = clf.fit(X, y)
        path =  "./trained_models/" + output_file
        joblib.dump(clf, path)
        print(name, " exported to ", path)


if __name__ == '__main__':
    train()