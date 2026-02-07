import cloudpickle
# lambda function( standard pickle doesn't always support well)
mi_lambda = lambda x: x ** 2

# Serializing
squared_serialized = cloudpickle.dumps(mi_lambda)
# Loading
nueva_lambda = cloudpickle.loads(squared_serialized)
print(nueva_lambda(5))
# Output: 25
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
# load data and train model
X, y = load_iris(return_X_y=True)
model = RandomForestClassifier()
model.fit(X, y)

import pickle
with open('iris_model.pkl', 'wb') as f:
    pickle.dump(model, f)

#with open('iris_model.pkl', 'rb') as f:
#    loaded_model_pickle = pickle.load(f)
