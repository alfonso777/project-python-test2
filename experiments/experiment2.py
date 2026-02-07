from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
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
    "random_state": 8000,
}
# Enable autologging for scikit-learn
import mlflow
mlflow.set_experiment("MyExperiment2")
mlflow.sklearn.autolog()
# Just train the model normally
lr = LogisticRegression(**hyper_params)
lr.fit(X_train, y_train)
