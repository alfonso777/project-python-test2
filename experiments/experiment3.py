import mlflow
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the Iris dataset
X, y = datasets.load_iris(return_X_y=True)
# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# Define the model hyperparameters
hyper_params = {
    "solver": "lbfgs",
    "max_iter": 500,
    #"multi_class": "auto",
    "random_state": 8888,
}
mlflow.set_experiment("MyExperiment2")
with mlflow.start_run():
    # Log the hyperparameters
    mlflow.log_params(hyper_params)
    # Train the model
    lr = LogisticRegression(**hyper_params)
    lr.fit(X_train, y_train)
    # Log the model
    model_info = mlflow.sklearn.log_model(sk_model=lr, name="iris_model")
    # Predict on the test set, compute and log the loss metric
    y_pred = lr.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    mlflow.log_metric("accuracy", accuracy)
    # Optional: Set a tag that we can use to remind ourselves what this run was for
    mlflow.set_tag("Training Info", "Basic LR model for iris data")
