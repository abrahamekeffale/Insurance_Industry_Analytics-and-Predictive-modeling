# tests/test_ab_testing.py

import unittest
from scripts.ab_hypothesis_testing import chi_square_test, t_test
import pandas as pd

class TestABTesting(unittest.TestCase):
    
    def setUp(self):
        # Set up a sample dataframe for testing
        self.df = pd.DataFrame({
            'Province': ['A', 'B', 'A', 'B'],
            'StatutoryRiskType': ['High', 'Low', 'Medium', 'Low'],
            'ZipCode': ['12345', '67890', '12345', '67890'],
            'TotalPremium': [100, 200, 150, 220]
        })
    
    def test_chi_square_test(self):
        result = chi_square_test(self.df, 'Province', 'StatutoryRiskType')
        self.assertIn('Reject', result)
    
    def test_t_test(self):
        result = t_test(self.df, 'ZipCode', 'TotalPremium', '12345', '67890')
        self.assertIn('Reject', result)

if __name__ == '__main__':
    unittest.main()
