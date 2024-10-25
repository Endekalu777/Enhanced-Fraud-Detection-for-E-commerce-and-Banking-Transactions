import pickle
import pandas as pd
import shap
import lime
import lime.lime_tabular
import matplotlib.pyplot as plt

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

# Function to perform SHAP analysis
def shap_analysis(model, X, model_name):
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X)
    
    # Summary Plot
    print(f"SHAP Summary Plot for {model_name}")
    shap.summary_plot(shap_values, X)
    
    # Force Plot for a single prediction (first instance)
    shap.initjs()
    print(f"SHAP Force Plot for {model_name} (first instance)")
    shap.force_plot(explainer.expected_value, shap_values[0], X.iloc[0])
    
    # Dependence Plot for a specific feature (update with feature_name)
    feature_name = "feature_name" 
    print(f"SHAP Dependence Plot for {feature_name} in {model_name}")
    shap.dependence_plot(feature_name, shap_values[1], X)

# Function to perform LIME analysis
def lime_analysis(model, X, model_name):
    lime_explainer = lime.lime_tabular.LimeTabularExplainer(
        training_data=np.array(X),
        feature_names=X.columns,
        class_names=['Class 0', 'Class 1'],  
        mode='classification'
    )

    # Explain a specific prediction (first instance)
    instance_to_explain = X.iloc[0]
    exp = lime_explainer.explain_instance(
        data_row=instance_to_explain,
        predict_fn=model.predict_proba
    )
    
    # Feature Importance Plot
    print(f"LIME Feature Importance Plot for {model_name} (first instance)")
    exp.as_pyplot_figure()
    plt.title(f'LIME Feature Importance for {model_name}')
    plt.show()