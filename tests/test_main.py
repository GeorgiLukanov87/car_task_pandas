import unittest
from car_data_analyzer.main import CarDataAnalyzer
import os


class TestCarDataAnalyzer(unittest.TestCase):

    def setUp(self):
        self.input_file = 'data/test_cars.json'
        self.output_file = 'data/test_car_data_result_output.csv'

        if not os.path.exists('logs'):
            os.makedirs('logs')
        if not os.path.exists('data'):
            os.makedirs('data')

        self.analyzer = CarDataAnalyzer(self.input_file, self.output_file)

        with open(self.input_file, 'w') as file:
            file.write('''
            [
                {"Name": "Car1", "Year": "1970", "Weight_in_lbs": 3500, 
                "Miles_per_Gallon": 20, "Horsepower": 100, "Acceleration": 15, "Origin": "USA"},
                {"Name": "Car2", "Year": "1980", "Weight_in_lbs": 2500,
                 "Miles_per_Gallon": 30, "Horsepower": 120, "Acceleration": 10, "Origin": "Europe"}
            ]
            ''')

    def tearDown(self):
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_load_data(self):
        self.analyzer.load_data()
        self.assertTrue(len(self.analyzer.data) > 0, "Data should be loaded")

    def test_analyze_data(self):
        self.analyzer.load_data()
        self.analyzer.analyze_data()
        self.assertTrue(os.path.exists(self.output_file), "Output file should be created")


if __name__ == '__main__':
    unittest.main()
