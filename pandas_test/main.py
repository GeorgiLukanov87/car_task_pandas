import pandas as pd
import json
from logger import setup_logger


class CarDataAnalyzer:
    def __init__(self, input_json_file, output_file):
        self.input_json_file = input_json_file
        self.output_file = output_file
        self.data = None
        self.logger = setup_logger()

    # Create method to read the input json file
    def load_data(self):
        try:
            with open(self.input_json_file, 'r') as file:
                self.data = json.load(file)
            self.logger.info(f"Loaded data from {self.input_json_file}")

        # Raise exception if json not found
        except FileNotFoundError:
            self.logger.error(f"File not found: {self.input_json_file}")
            raise

        # Raise exception if something is wrong with the json file
        except json.JSONDecodeError:
            self.logger.error(f"JSON decoding error in {self.input_json_file}")
            raise

    def analyze_data(self):
        if self.data is None:
            self.logger.error("No data loaded.")
            return

        # Convert data to a DataFrame using pandas
        df_car_data = pd.DataFrame(self.data)

        # Format the "Year" column to display only the year part
        df_car_data['Year'] = pd.to_datetime(df_car_data['Year']).dt.year

        unique_cars = df_car_data['Name'].nunique()
        average_hp = df_car_data['Horsepower'].mean()

        # Extract the top 5 heaviest cars with only "Name" and "Weight_in_lbs" columns
        heaviest_cars = df_car_data.nlargest(5, 'Weight_in_lbs')[['Weight_in_lbs', 'Name']]
        cars_by_manufacturer = df_car_data['Origin'].value_counts()

        # Count the number of cars by year and sort in reversed order
        cars_by_year = df_car_data['Year'].value_counts().sort_index(ascending=True)

        # Print results
        print('----------------------------------------------')
        print(f"Number of Unique Cars: {unique_cars}")
        print(f"Average Horsepower of All Cars: {average_hp:.2f}")
        print('----------------------------------------------')
        print("Top 5 Heaviest Cars (Name and Weight):\n")
        print(heaviest_cars.to_string(index=False))
        print('----------------------------------------------')
        print("Number of Cars by Manufacturer:\n")
        print(cars_by_manufacturer.to_string())
        print('----------------------------------------------')
        print("Number of Cars by Year:\n")
        print(cars_by_year.to_string())

        # Save data frame to csv file
        df_car_data.to_csv(self.output_file, index=False)
        self.logger.info(f"Saved data to {self.output_file}")
