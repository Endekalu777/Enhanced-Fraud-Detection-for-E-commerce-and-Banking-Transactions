import pickle
import pandas as pd

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

# Load your datasets (update with your dataset paths)
fraud_data = pd.read_csv("../data/cleaned_creditcard.csv")
creditcard_data = pd.read_csv("../data/cleaned_merged_fraud.csv")

# Prepare feature matrices (update with your target column)
X_fraud = fraud_data.drop("target_column", axis=1)  
X_creditcard = creditcard_data.drop("target_column", axis=1)