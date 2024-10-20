import os
import logging
import pandas as pd

# Get the current working directory
current_directory = os.getcwd()

# Ensure the logging directory exists
log_directory = os.path.join(current_directory, 'logging')
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

log_file = os.path.join(log_directory, "merge_dataset.log")
logging.basicConfig(filename=log_file,
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filemode='a')


class MergeDataset:
    def __init__(self, file_path1, file_path2):
        try:
            logging.info(f"Loading datasets from {file_path1} and {file_path2}")
            self.df1 = pd.read_csv(file_path1)
            self.df2 = pd.read_csv(file_path2)
            logging.info("Successfully loaded the datasets")
        except FileNotFoundError as e:
            logging.error(f"File not found: {e}")
            raise
        except pd.errors.EmptyDataError as e:
            logging.error(f"Empty data error: {e}")
            raise
        except Exception as e:
            logging.error(f"Error loading datasets: {e}")
            raise

    def merge_df(self):
        # Merge the dataframes and log the operation
        logging.info("Merging datasets.")
        try:
            merged_data = pd.concat([self.df1, self.df2], ignore_index=True)
            logging.info("Datasets merged successfully")
            return merged_data
        except Exception as e:
            logging.error(f"Error merging datasets: {e}")
            raise

    def save_merged_data(self, save_location):
        # Save the merged DataFrame to a CSV file and log the operation
        try:
            merged_data = self.merge_df()
            merged_data.to_csv(save_location, index=False)
            logging.info(f"Merged data saved to {save_location}.")
            print(f"Merged data saved to {save_location}")
        except Exception as e:
            logging.error(f"Error saving merged data: {e}")
            raise


if __name__ == "__main__":
    file_path1 = "data/Processed_Fraud_Data.csv"
    file_path2 = "data/Processed_IpAddress_data.csv"
    save_location = "data/Merged_FIp_data.csv"

    try:
        merge_dataset = MergeDataset(file_path1, file_path2)
        merge_dataset.save_merged_data(save_location)
    except Exception as e:
        print(f"An error occurred: {e}")
