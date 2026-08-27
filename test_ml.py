import pytest
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from ml.model import train_model, inference
import numpy as np

# TODO: implement the first test. Change the function name and input as needed
def test_model_algo():
    """
    # This test ensures that train_model returns a Random Forest Classifier
    """
    X_train = [[0,1], [1,2], [2,3], [3,4]]
    y_train = [0, 0, 1, 1]

    model = train_model(X_train, y_train)
    
    assert isinstance(model, RandomForestClassifier)


# TODO: implement the second test. Change the function name and input as needed
def test_split_data():
    """
    # This test verifies the data is split into 80% training and 20% testing
    """
    data = list(range(100))
    train, test = train_test_split(data, test_size=.2)

    assert len(train) == 80
    assert len(test) == 20


# TODO: implement the third test. Change the function name and input as needed
def test_inference_type():
    """
    # This test verifies the inference returns a NumPy array
    """
    X_train = [[0,1], [1,2], [2,3], [3,4]]
    y_train = [0, 0, 1, 1]

    model = train_model(X_train, y_train)
    preds = inference(model, X_train)

    assert isinstance(preds, np.ndarray)