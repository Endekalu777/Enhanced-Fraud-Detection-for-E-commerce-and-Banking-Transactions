import pickle

# Load your models
model_names = [
    "random_forest_fraud_model.pkl",
    "decision_tree_fraud_model.pkl",
    "random_forest_creditcard_model.pkl",
    "decision_tree_creditcard_model.pkl"
]

models = {}
for model_name in model_names:
    with open(model_name, 'rb') as file:
        models[model_name] = pickle.load(file)