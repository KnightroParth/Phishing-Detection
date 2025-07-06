"""
Model evaluation utilities.
"""

from sklearn.metrics import classification_report

def evaluate_model(model, X_test, y_test):
    """
    Prints classification metrics for a model.

    Parameters:
        model: Trained classifier
        X_test: Test features
        y_test: Test labels
    """
    y_pred = model.predict(X_test)
    print("\n Model Evaluation Report:\n")
    print(classification_report(y_test, y_pred))

