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
        logging.info(f"Loading datasets from {file_path1} and {file_path2}")
        self.df1 = pd.read_csv(file_path1)
        self.df2 = pd.read_csv(file_path2)
        logging.info(f"Successfully loaded the dataset")

    def merge_df(self):
        # Merge the dataframes and log the operation
        logging.info("Merging datasets.")
        merged_data = pd.concat([self.df1, self.df2], ignore_index = True)
        logging.info("Datasets merged successfully")
        return merged_data
    
    def save_merged_data(self, save_location):
        # Save the merged DataFrame to a CSV file and log the operation
        merged_data = self.merge_df()
        merged_data.to_csv(save_location, index = False)
        logging.info(f"Merged data saved to {save_location}.")
        print(f"Merged data saved to {save_location}")

    