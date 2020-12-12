from postgres.data_gen import start_data_gen
from postgres.fetch_sample import get_sample
from postgres.delete_data import reset_all_tables, delete_all_csv
from postgres.download_data import download_all_tables
from typing import List

def validate_csv() -> bool:
    return True

def main():
    tables: List[str] = ["rainfall", "soil_moisture", "river_stage"]
    paths:  List[str] = ["data/results_rainfall.csv", "data/results_river_stage.csv", "data/results_soil_moisture.csv"]
    target = int(input("For How long you'd like to generate data? (in seconds): "))
    start_data_gen(target)
    download_all_tables(tables)
    reset_all_tables(tables)
    # if validate_csv():
    #     # send_data()
    #     delete_all_csv(paths)

if __name__ == '__main__':
    main()
