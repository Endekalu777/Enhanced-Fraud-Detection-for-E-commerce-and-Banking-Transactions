import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import logging
from IPython.display import display
import warnings
from datetime import datetime
import os


# Ignore FutureWarnings and UserWarnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

# Get the current working directory
current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

# Ensure the logging directory exists
log_directory = os.path.join(parent_directory, 'logging')
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Create a timestamp for the log file name
def get_log_file_name(filepath):
    dataset_name = os.path.splitext(os.path.basename(filepath))[0]  # Extract dataset name from filepath
    log_file_name = f'data_preprocessing_{dataset_name}.log'
    log_file_path = os.path.join(log_directory, log_file_name)
    return log_file_path

class pre_processing():
    def __init__(self, filepath):
        log_file_path = get_log_file_name(filepath)
        # Configure logging to append if the file exists
        logging.basicConfig(filename=log_file_path,
                            level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            filemode='a')  # Always append to the existing log file

        logging.info(f"Log file opened at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} for dataset {filepath}")

        # Load the CSV file into a DataFrame using pandas
        try:
            self.df = pd.read_csv(filepath)
            logging.info("Data successfully loaded from: %s", filepath)
        except Exception as e:
            logging.error(f"Error loading data from {filepath}: {e}")
            raise

    def data_overview(self):
        """
        Provide an overview of the dataset structure, including shape, preview, 
        data types, and missing values.
        """
        # Shape of the data
        try:
            logging.info("Generating data overview")
            print(f"Shape of the dataset: {self.df.shape}\n")
            logging.info("Successfully retrieved the shape of the dataset.")
        except Exception as e:
            logging.error(f"Error retrieving the shape of the dataset: {e}")

        # Used head to preview first 5 rows
        try:
            logging.info("Displaying the first five rows of the data")
            print("Preview of the first 5 rows:")
            display(self.df.head())
            logging.info("Successfully displayed the first five rows.")
        except Exception as e:
            logging.error(f"Error displaying the first five rows.")

        # Showing the data types in the dataset
        try:
            logging.info("Displaying data types of the dataset")
            print("Data types of the dataset")
            data_types = self.df.dtypes
            display(data_types)
            logging.info("Successfully displayed the data types of the dataset")
        except Exception as e:
            logging.error(f"Error displaying the data types of the dataset {e}")
    
        # Overview of missing values of the dataset
        try:
            print("Missing values of the dataset: ")
            missing_values_count = self.df.isnull().sum() # count missing values 
            total_entries = self.df.shape[0] # Total number of entries
            missing_values_percentage = (missing_values_count / total_entries) * 100 # Calculate percentage

            # create dataframe for missing values
            missing_values_df = pd.DataFrame({
                'Missing Values Count': missing_values_count,
                'Missing Values Percentage (%)': missing_values_percentage
            })
            print("Missing values in the dataset (Count and percentage)")
            display(missing_values_df)
            logging.info("Successfully displayed the missing values")
        except Exception as e:
            logging.error(f"Error displaying the missing values of the dataset: {e}")

    # method to remove duplicates and Correct data types
    def data_cleaning(self):
        logging.info("Starting data cleaning process")
        try:
            # Remove dupliates
            self.df.drop_duplicates(inplace = True)
            logging.info("Completed removing duplicates")

            # Correct data types
            if 'signup_time' in self.df.columns:
                self.df['signup_time'] = pd.to_datetime(self.df['signup_time'])
                logging.info("Converted 'signup_time' to datetime")

            if 'purchase_time' in self.df.columns:
                self.df['purchase_time'] = pd.to_datetime(self.df['purchase_time'])
                logging.info("Converted 'purchase_time' to datetime.")

            if 'ip_address' in self.df.columns:
                self.df['ip_address'] = self.df['ip_address'].astype(int) # Convert IP addresses from float to int for better compatibility
                logging.info("Converted 'ip_address' from float to integer")

        except Exception as e:
            logging.info(f"Error during data cleaning: {e}")





