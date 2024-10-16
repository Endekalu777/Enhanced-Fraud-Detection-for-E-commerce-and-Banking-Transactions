import pandas as pd
import numpy as np
import logging
import logging
from IPython.display import display
import warnings
import os
import sys

# Ignore FutureWarnings and UserWarnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)


# Ensure the logging directory exists
log_directory = 'logging'
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Configure logging to save in a logging file
logging.basicConfig(filename=os.path.join(log_directory, 'data_preprocessing.log'),
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class pre_processing():
    def __init__(self, filepath):
        logging.info("Started reading the data from: {filepath}")
        self.df = pd.read_csv(filepath)  # Load the CSV file into a DataFrame using pandas
        logging.info("Data succesfully loaded.")

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

