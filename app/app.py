from flask import Flask, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load data
df = pd.read_csv('../data/Fraud_Data.csv')
df['purchase_time'] = pd.to_datetime(df['purchase_time'])
df['month_year'] = df['purchase_time'].dt.strftime('%b %Y')