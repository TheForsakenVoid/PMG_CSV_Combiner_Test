import csv
import io
import os
import sys
import unittest
import generatetestfixtures
from Csv_Combiner import combine_csv

class TestCSVCombiner(unittest.TestCase):
    def setUp(self):
        self.files = ['./test_fixtures/clothing_test.csv', './test_fixtures/accessories_test.csv', './test_fixtures/household_cleaners_test.csv']
        generatetestfixtures.main()

    def test_combine_csv(self):
        # Capture the output of combine_csv
        captured_output = io.StringIO()
        sys.stdout = captured_output

        combine_csv(self.files)
        output = captured_output.getvalue().strip()

        # Reset sys.stdout
        sys.stdout = sys.__stdout__

        # Compare the output with the contents of the generated test fixtures
        for file in self.files:
            with open(file, 'r') as f:
                self.assertIn(f.read(), output)