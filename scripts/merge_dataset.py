import os
import logging

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


