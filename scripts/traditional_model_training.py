import os
import logging
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score


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

    def train_creditcard_models(self):
        logging.info("Starting model training on Credit Card dataset...")
        print("Training models on Credit Card dataset...")
        models = {
            'Logistic Regression': LogisticRegression(max_iter=1000),
            'Decision Tree': DecisionTreeClassifier(),
            'Random Forest': RandomForestClassifier()
        }

        # Hyperparameter grids
        param_grids = {
            'Logistic Regression': {
                'C': [0.001, 0.01, 0.1, 1, 10],
                'solver': ['liblinear', 'saga']
            },
            'Decision Tree': {
                'max_depth': [None, 5, 10, 15, 20],
                'min_samples_split': [2, 5, 10]
            },
            'Random Forest': {
                'n_estimators': [50, 100, 200],
                'max_depth': [None, 5, 10, 15, 20]
            }
            
        }

        for name, model in models.items():
            logging.info(f"Training {name} with GridSearchCV...")
            try:
                print(f"Training {name} with GridSearchCV...")
                grid_search = GridSearchCV(model, param_grids[name], cv=5, n_jobs=-1)
                grid_search.fit(self.X_train_cc, self.y_train_cc)
                best_model = grid_search.best_estimator_
                y_pred = best_model.predict(self.X_test_cc)
                accuracy = accuracy_score(self.y_test_cc, y_pred)
                logging.info(f"{name} Best Accuracy: {accuracy:.4f} with parameters {grid_search.best_params_}")
                print(f"{name} Best Accuracy on Credit Card Dataset: {accuracy:.4f} with parameters {grid_search.best_params_}")
            except Exception as e:
                logging.error(f"Error training {name}: {e}")
                raise