
import pytest
import numpy as np
import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

def test_model_training():
    assert model is not None, "Model training failed!"

def test_model_accuracy():
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    assert accuracy > 0.8, "Model accuracy is too low!"

def test_prediction_shape():
    sample = X_test[:5]

    predictions = model.predict(sample)

    assert len(predictions) == 5, "Prediction output size mismatch!"

def test_model_prediction():
    predictions = model.predict(X_train)

    assert predictions.shape[0] == X_train.shape[0], "Prediction shape is incorrect!"
    assert set(np.unique(predictions)).issubset(set(np.unique(y_train))), "Invalid class labels in predictions!"

from pathlib import Path

def test_model_prediction():

    # Check model file exists
    assert Path("iris.pkl").exists(), "Model file iris.pkl not found!"

    # Load model
    with open("iris.pkl", "rb") as f:
        model = pickle.load(f)

    # Load sample Iris data
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Select one sample
    sample = X[0].reshape(1, -1)

    # Predict
    prediction = model.predict(sample)

    # Check prediction shape
    assert len(prediction) == 1, "Prediction output size is incorrect!"

    # Check valid class label
    assert prediction[0] in np.unique(y), "Invalid prediction label!"




def test_wrong_input_shape_fails():
    with open("iris.pkl", "rb") as f:
        model = pickle.load(f)

    bad_input = [[5.1, 3.5]]  # only 2 features instead of 4

    with pytest.raises(ValueError):
        model.predict(bad_input)
