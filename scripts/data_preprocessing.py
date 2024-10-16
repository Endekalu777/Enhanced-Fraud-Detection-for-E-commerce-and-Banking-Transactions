import pandas as pd
import numpy as np
import logging
import warnings
from IPython.display import display
warnings.filterwarnings("ignore")

class pre_processing():
    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)

    def data_overview(self):
        """
        Provide an overview of the dataset structure, including shape, preview, 
        data types, and missing values.
        """
        print(f"Shape of the dataset: {self.df.shape}\n")
        print("Preview of the first 5 rows:")
        display(self.df.head())
        print("Data types of the dataset")
        display(self.df.dtypes)
        print("Missing values of the dataset: ")
        display(self.df.isnull().sum())
