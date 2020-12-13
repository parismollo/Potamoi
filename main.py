from postgres.data_gen import start_data_gen
from postgres.fetch_sample import get_sample
from postgres.delete_data import reset_all_tables, delete_all_csv
from postgres.download_data import download_all_tables
from typing import List
from postgres.validate_data import validate_data

def main():
    tables: List[str] = ["rainfall", "soil_moisture", "river_stage"]
    paths:  List[str] = ["data/results_rainfall.csv", "data/results_river_stage.csv", "data/results_soil_moisture.csv"]
    print("\n----------------Data Generation----------------")
    target = int(input("\nFor how long you'd like to generate data? (in seconds): "))
    start_data_gen(target)
    print("\n----------------Downloading data----------------")
    download_all_tables(tables)
    print("\n----------------Reseting database----------------")
    reset_all_tables(tables)
    print("\n----------------Validating files----------------")
    valid_files = validate_data()
    if len(valid_files) != 0:
        # send_data(valid_files)
        print("\n----------------Resetting data folder----------------")
        delete_all_csv(paths)

if __name__ == '__main__':
    main()
