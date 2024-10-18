import pandas as pd
import unittest
import numpy as np
import matplotlib.pyplot as plt
from scripts.data_preprocessing import *

class TestPreProcessing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Run once before all tests."""
        # Mock dataset to use in tests
        cls.mock_data = pd.DataFrame({
            'user_id': [1, 2, 2, 4],  
            'signup_time': ['2023-01-01 10:00:00', '2023-02-01 12:00:00', 
                            '2023-02-01 12:00:00', '2023-03-01 14:00:00'], 
            'purchase_time': ['2023-01-01 11:00:00', '2023-02-01 13:00:00', 
                              '2023-02-01 13:00:00', '2023-03-01 15:00:00'],  
            'purchase_value': [34.0, 16.0, 15.0, 44.0], 
            'Amount': [50.0, 20.5, 20.5, np.nan], 
            'Class': [0, 1, 1, 0],  
            'lower_bound_ip_address': [123456, 67890, np.nan, 90123],
            'upper_bound_ip_address': [16777471, 16777727, np.nan, 16779263],
            'country': ['USA', 'Canada', 'USA', 'Canada']  
        })

        # Create a temporary CSV file for testing
        cls.test_file = 'test_dataset.csv'
        cls.mock_data.to_csv(cls.test_file, index=False)

        # Initialize the pre_processing object with the test file
        cls.processor = pre_processing(cls.test_file)

        # Turn off interactive plotting
        plt.ioff()

    @classmethod
    def tearDownClass(cls):
        """Run once after all tests."""
        # Remove the test file after tests complete
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)

    def test_data_loading(self):
        """Test if data is loaded correctly without errors."""
        self.assertIsInstance(self.processor.df, pd.DataFrame)
        self.assertEqual(self.processor.df.shape, (4, 9)) 

    def test_data_overview(self):
        """Test if the data overview methods execute without errors."""
        try:
            self.processor.data_overview()
        except Exception as e:
            self.fail(f"data_overview() raised an exception: {e}")




