# main.py
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

        df_car_data = pd.DataFrame(self.data)
        convert_data(df_car_data)

        df_car_data.to_csv(self.output_file, index=False)
        self.logger.info(f"Saved data to {self.output_file}")

        visualize_data(df_car_data)

