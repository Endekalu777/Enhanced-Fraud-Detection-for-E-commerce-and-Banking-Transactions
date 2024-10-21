import os
import logging
import pandas as pd
from sklearn.model_selection import train_test_split


# Get the current working directory
current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

# Ensure the logging directory exists
log_directory = os.path.join(parent_directory, 'logging')
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

log_file = os.path.join(log_directory, "merge_dataset.log")
logging.basicConfig(filename=log_file,
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filemode='a')

class ModelTraining():
    def __init__(self, file_path1, file_path2):
        logging.info(f"Initializing ModelTraining with datasets {file_path1} and {file_path2}")
        # Load datasets
        try:
            self.credit_df = pd.read_csv(file_path1)
            self.fraud_df = pd.read_csv(file_path2)
            logging.info("Successfully loaded datasets.")
        except FileNotFoundError as e:
            logging.error(f"File not found: {e}")
            raise
        except pd.errors.EmptyDataError as e:
            logging.error(f"Empty data error: {e}")
            raise
        except Exception as e:
            logging.error(f"Error loading datasets: {e}")
            raise

    def data_preparation(self):
        # Feature and Target Separation for Credit Card dataset
        try:
            logging.info("Started data preparation.")
            self.X_creditcard = self.credit_df.drop(columns=['Class'])
            self.y_creditcard = self.credit_df['Class']
            logging.info("Separated features and target for Credit Card dataset.")

            # Feature and Target Separation for Fraud Data dataset
            self.X_fraud = self.fraud_df.drop(columns=['class'])
            self.y_fraud = self.fraud_df['class']
            logging.info("Separated features and target for Fraud Data dataset.")

            # Train-Test Split for both datasets
            self.X_train_cc, self.X_test_cc, self.y_train_cc, self.y_test_cc = train_test_split(
                self.X_creditcard, self.y_creditcard, test_size=0.3, random_state=42
            )
            logging.info("Performed train-test split for Credit Card dataset.")
            self.X_train_fraud, self.X_test_fraud, self.y_train_fraud, self.y_test_fraud = train_test_split(
                self.X_fraud, self.y_fraud, test_size=0.3, random_state=42
            )
            logging.info("Performed train-test split for Fraud Data dataset.")
        except KeyError as e:
            logging.error(f"Missing columns in dataset: {e}")
            raise
        except Exception as e:
            logging.error(f"Error during data preparation: {e}")
            raise