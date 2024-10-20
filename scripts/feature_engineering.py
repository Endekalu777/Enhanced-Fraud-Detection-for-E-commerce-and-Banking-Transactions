import pandas as pd
from sklearn.preprocessing import StandardScaler

class FeatureEngineering:
    def __init__(self, fraud_file, creditcard_file):
        # Load datasets
        self.fraud_df = pd.read_csv(fraud_file)
        self.creditcard_df = pd.read_csv(creditcard_file)
        self.scaler = StandardScaler()