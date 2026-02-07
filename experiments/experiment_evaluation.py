import mlflow
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from mlflow.models import infer_signature
# Load dataset
X, y = load_breast_cancer(return_X_y=True, as_frame=True)
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.3, random_state=42)
# Train model
model = xgb.XGBClassifier().fit(X_train, y_train)
# Create evaluation dataset
eval_data = X_test.copy()
eval_data["label"] = y_test

mlflow.set_experiment("breast_cancer_classification")
with mlflow.start_run():
    # Log model
    signature = infer_signature(X_test, model.predict(X_test))
    model_info = mlflow.sklearn.log_model(model, name="model", signature=signature)
    # Evaluate
    result = mlflow.models.evaluate(
        model_info.model_uri,
        eval_data,
        targets="label",
        model_type="classifier",
        evaluator_config= {
            "log_explainer": True,
            "explainers": ["exact"]
        }
    )
    print(f"Accuracy: {result.metrics['accuracy_score']:.3f}")
    print(f"F1 Score: {result.metrics['f1_score']:.3f}")
    print(f"ROC AUC: {result.metrics['roc_auc']:.3f}")
