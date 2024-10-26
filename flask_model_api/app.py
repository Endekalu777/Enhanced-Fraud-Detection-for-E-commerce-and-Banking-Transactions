from flask import Flask
import pickle

app = Flask(__name__)

# Load models
with open('../models/random_forest_fraud_model.pkl', 'rb') as f:
    fraud_model = pickle.load(f)

