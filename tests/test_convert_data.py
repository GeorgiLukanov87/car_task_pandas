import unittest
import pandas as pd

from car_data_analyzer.data_processing.convert_data import convert_data


class TestConvertData(unittest.TestCase):
    def setUp(self):
        self.test_data = pd.DataFrame({
            'Year': ['1970-01-01', '1971-01-01'],
            'Weight_in_lbs': [3504, 3693],
            'Miles_per_Gallon': [18, 15]
        })

    def test_convert_year(self):
        convert_data(self.test_data)
        self.assertEqual(list(self.test_data['Year']), [1970, 1971])

    def test_convert_weight(self):
        convert_data(self.test_data)
        # 1 pound = 0.45359237 kilograms
        expected_weight_kg = 3504 * 0.45359237
        self.assertAlmostEqual(self.test_data['Weight_in_kg'][0], expected_weight_kg, places=2)

    def test_convert_mpg_to_lp100km(self):
        convert_data(self.test_data)
        self.assertAlmostEqual(self.test_data['Liters_per_100km'][0], 13.067, places=3)


if __name__ == '__main__':
    unittest.main()
