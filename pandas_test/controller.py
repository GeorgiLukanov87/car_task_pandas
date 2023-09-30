from main import CarDataAnalyzer

if __name__ == "__main__":
    input_json_file = "cars.json"
    output_result_file = "car_data_result_output.csv"

    analyzer = CarDataAnalyzer(input_json_file, output_result_file)

    try:
        analyzer.load_data()
        analyzer.analyze_data()

    except Exception as err:
        print(f"An error occurred: {str(err)}")
