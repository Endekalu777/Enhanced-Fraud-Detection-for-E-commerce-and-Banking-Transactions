import os
import logging
import pandas as pd

# Get the current working directory
current_directory = os.getcwd()

# Ensure the logging directory exists
log_directory = os.path.join(current_directory, 'logging' )
if not os.path.exist(log_directory):
    os.makedirs(log_directory)

log_file = os.path.join(log_directory, "merge_dataset.log")
logging.basicConfig(filename=log_file,
                            level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            filemode='a')

class merge_dataset():
    def init(self, file_path1, file_path2):
        self.df1 = pd.read_csv(file_path1)
        self.df2 = pd.read_csv(file_path2)

    