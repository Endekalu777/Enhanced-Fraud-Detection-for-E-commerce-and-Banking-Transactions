import pandas as pd
from sklearn.preprocessing import StandardScaler

class FeatureEngineering:
    def __init__(self, fraud_file, creditcard_file):
        # Load datasets
        self.fraud_df = pd.read_csv(fraud_file)
        self.creditcard_df = pd.read_csv(creditcard_file)
        self.scaler = StandardScaler()

    def compute_transaction_features(self):
        # Transaction frequency: Count of transactions per user
        self.fraud_df['transaction_frequency'] = self.fraud_df.groupby('user_id')['user_id'].transform('count')

        # Transaction velocity: Time difference between consecutive transactions for each user
        self.fraud_df = self.fraud_df.sort_values(['user_id', 'purchase_time'])  
        self.fraud_df['time_diff'] = self.fraud_df.groupby('user_id')['purchase_time'].diff().dt.total_seconds().fillna(0)

        # Extract hour of the day and day of the week
        self.fraud_df['hour_of_day'] = self.fraud_df['purchase_time'].dt.hour
        self.fraud_df['day_of_week'] = self.fraud_df['purchase_time'].dt.weekday

    def scale_features(self):
        # Features to scale in fraud_df
        features_to_scale_fraud = ['purchase_value', 'transaction_frequency', 'time_diff', 'hour_of_day']
        self.fraud_df[features_to_scale_fraud] = self.scaler.fit_transform(self.fraud_df[features_to_scale_fraud])

        # Scale Amount in creditcard_df
        self.creditcard_df['Amount'] = self.scaler.fit_transform(self.creditcard_df[['Amount']])

    def encode_categorical_features(self):
        # One-hot encode categorical columns in fraud_df
        self.fraud_df = pd.get_dummies(self.fraud_df, columns=['browser', 'sex', 'country'], drop_first=True)

        