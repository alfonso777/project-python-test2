import pickle

with open('iris_model.pkl', 'rb') as f:
    loaded_model_pickle = pickle.load(f)
    print(loaded_model_pickle)
