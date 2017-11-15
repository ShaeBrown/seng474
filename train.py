import numpy as np
from sklearn import tree
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib


def load_data():
    yn = lambda s: 1 if s == "yes" else 0
    fm = lambda s: 1 if s == "M" else 0
    data = np.loadtxt("pordate.csv", dtype=np.float64, delimiter=",", skiprows=1, converters={0: fm, 4: yn, 5: yn, 6: yn})
    X = np.delete(data, [0, len(data[0]) - 1], axis=1)
    y = data[:, -1]
    return X, y


def test_cros_val(clf, X, y, test=0.33):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test, random_state=42)
    print("Using  ", test, " of data for testing")
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print(metrics.classification_report(y_test, y_pred))


def train():
    X,y = load_data()
    clf = tree.DecisionTreeClassifier()
    test_cros_val(clf, X, y)
    clf = clf.fit(X, y)
    joblib.dump(clf, "./trained_models/decisiontree.pkl")
    print("Decision tree exported to  trained_models/decisiontree.pkl")


if __name__ == '__main__':
    train()