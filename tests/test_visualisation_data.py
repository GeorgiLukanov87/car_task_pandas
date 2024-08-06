# tests/test_visualisation_data.py

import unittest
import pandas as pd
from car_data_analyzer.visualization.visualisation_data import visualize_data


class TestVisualizationData(unittest.TestCase):

    def setUp(self):
        self.data = [
            {"Name": "Car1", "Year": "1970", "Weight_in_lbs": 3500, "Liters_per_100km": 20, "Horsepower": 100,
             "Acceleration": 15, "Origin": "USA"},
            {"Name": "Car2", "Year": "1980", "Weight_in_lbs": 2500, "Liters_per_100km": 30, "Horsepower": 120,
             "Acceleration": 10, "Origin": "Europe"}
        ]
        self.df_car_data = pd.DataFrame(self.data)
        self.df_car_data['Weight_in_kg'] = self.df_car_data['Weight_in_lbs'] * 0.453592

    def test_visualize_data(self):
        try:
            visualize_data(self.df_car_data)
            result = True
        except Exception as e:
            print(f"Error occurred during visualization: {str(e)}")
            result = False
        self.assertTrue(result, "Visualization should run without errors")


if __name__ == '__main__':
    unittest.main()
