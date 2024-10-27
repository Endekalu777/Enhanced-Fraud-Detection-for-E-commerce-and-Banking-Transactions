from flask import Flask, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load data
df = pd.read_csv('../data/Fraud_Data.csv')
df['purchase_time'] = pd.to_datetime(df['purchase_time'])
df['month_year'] = df['purchase_time'].dt.strftime('%b %Y')

@app.route('/api/summary', methods=['GET'])
def get_summary():
    total_transactions = len(df)
    total_fraud_cases = len(df[df['class'] == 1])
    fraud_percentage = (total_fraud_cases / total_transactions) * 100
    
    return jsonify({
        'total_transactions': total_transactions,
        'total_fraud_cases': total_fraud_cases,
        'fraud_percentage': round(fraud_percentage, 2)
    })