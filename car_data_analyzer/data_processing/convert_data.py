# data_processing/convert_data.py
import pandas as pd


def convert_data(df_car_data: pd.DataFrame) -> None:
    """Convert columns to appropriate formats and units."""

    df_car_data['Year'] = pd.to_datetime(df_car_data['Year'], errors='coerce').dt.year

    # Convert Weight_in_lbs to kg
    if 'Weight_in_lbs' in df_car_data.columns:
        df_car_data['Weight_in_kg'] = df_car_data['Weight_in_lbs'] * 0.45359237

    # Convert Miles_per_Gallon to Liters per 100 km
    if 'Miles_per_Gallon' in df_car_data.columns:
        df_car_data['Liters_per_100km'] = 235.214583 / df_car_data['Miles_per_Gallon']

    # Convert Miles to Kilometers
    if 'Miles_per_Gallon' in df_car_data.columns:
        df_car_data['Kilometers'] = df_car_data['Miles_per_Gallon'] * 1.60934
