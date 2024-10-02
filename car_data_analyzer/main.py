
from typing import Dict, Any
import pandas as pd
import json
import os
from car_data_analyzer.utils.logger import setup_logger
from car_data_analyzer.data_processing.convert_data import convert_data
from car_data_analyzer.visualization.visualisation_data import visualize_data


class CarDataAnalyzer:
    def __init__(self, input_json_file: str, output_file: str):
        self.input_json_file = input_json_file
        self.output_file = output_file
        self.data: Dict[str, Any] = {}
        self.logger = setup_logger()
        self.df_car_data = None

    def load_data(self) -> None:
        """Load data from JSON file."""
        if not os.path.exists(self.input_json_file):
            self.logger.error(f"File not found: {self.input_json_file}")
            raise FileNotFoundError(f"File not found: {self.input_json_file}")

        try:
            with open(self.input_json_file, 'r') as file:
                self.data = json.load(file)
            self.logger.info(f"Successfully loaded data from {self.input_json_file}")
        except json.JSONDecodeError as e:
            self.logger.error(f"JSON decoding error in {self.input_json_file}: {str(e)}")
            raise
        except Exception as e:
            self.logger.error(f"Unexpected error when loading {self.input_json_file}: {str(e)}")
            raise

    def analyze_data(self) -> None:
        if not self.data:
            self.logger.error("No data loaded.")
            return

        self.df_car_data = pd.DataFrame(self.data)
        convert_data(self.df_car_data)

        self.df_car_data.to_csv(self.output_file, index=False)
        self.logger.info(f"Saved data to {self.output_file}")

        # Calculate and print averages
        averages = self.calculate_averages()
        print("Average values:")
        for col, avg in averages.items():
            print(f"{col}: {avg:.2f}")

        # Get and print top and bottom 5 cars by horsepower
        top_bottom_cars = self.get_top_bottom_cars('Horsepower')
        print("\nTop 5 cars by horsepower:")
        print(top_bottom_cars['top'])
        print("\nBottom 5 cars by horsepower:")
        print(top_bottom_cars['bottom'])

        visualize_data(self.df_car_data)

    def calculate_averages(self) -> Dict[str, float]:
        """Calculate average values for numerical columns."""
        if self.df_car_data is None:
            self.logger.error("Data not loaded. Please run load_data() first.")
            return {}

        numerical_columns = ['Horsepower', 'Weight_in_kg', 'Liters_per_100km', 'Acceleration']
        averages = {col: self.df_car_data[col].mean() for col in numerical_columns}

        self.logger.info("Calculated average values")
        return averages

    def get_top_bottom_cars(self, column: str, top_n: int = 5) -> Dict[str, pd.DataFrame]:
        """Get top and bottom N cars for a specific column."""
        if self.df_car_data is None:
            self.logger.error("Data not loaded. Please run load_data() first.")
            return {}

        if column not in self.df_car_data.columns:
            self.logger.error(f"Column '{column}' not found in the data.")
            return {}

        top_cars = self.df_car_data.nlargest(top_n, column)[['Name', column]]
        bottom_cars = self.df_car_data.nsmallest(top_n, column)[['Name', column]]

        self.logger.info(f"Retrieved top and bottom {top_n} cars for {column}")
        return {'top': top_cars, 'bottom': bottom_cars}

    def filter_by_year(self, start_year: int, end_year: int) -> pd.DataFrame:
        """Filter cars by year range."""
        if self.df_car_data is None:
            self.logger.error("Data not loaded. Please run load_data() first.")
            return pd.DataFrame()

        filtered_data = self.df_car_data[
            (self.df_car_data['Year'] >= start_year) & (self.df_car_data['Year'] <= end_year)]
        self.logger.info(f"Filtered data from year {start_year} to {end_year}")
        return filtered_data

    def sort_by_column(self, column: str, ascending: bool = True) -> pd.DataFrame:
        """Sort cars by specified column."""
        if self.df_car_data is None:
            self.logger.error("Data not loaded. Please run load_data() first.")
            return pd.DataFrame()

        if column not in self.df_car_data.columns:
            # print(self.df_car_data.columns)
            self.logger.error(f"Column '{column}' not found in the data.")
            return pd.DataFrame()

        sorted_data = self.df_car_data.sort_values(by=column, ascending=ascending)
        self.logger.info(f"Sorted data by {column} ({'ascending' if ascending else 'descending'})")
        return sorted_data


if __name__ == "__main__":
    input_json_file = "data/cars.json"
    output_result_file = "data/car_data_result_output.csv"

    analyzer = CarDataAnalyzer(input_json_file, output_result_file)

    try:
        analyzer.load_data()
        analyzer.analyze_data()

    except Exception as err:
        print(f"An error occurred: {str(err)}")
