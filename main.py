from data_fetching.data_gen import generate_data_files
from data_fetching.delete_data_files import delete_all_csv
from typing import List
from data_fetching.validate_data import validate_data

def main():
    sensors: List[str] = ["rainfall", "soil_moisture", "river_stage"]
    print("\n----------------Data Generation----------------")
    n_rows = int(input("\nInput the number of rows you'd like to generate: "))
    generate_data_files(sensors, n_rows)
    print("\n----------------Validating files----------------")
    valid_files = validate_data()
    if len(valid_files) != 0:
        # send_data(valid_files)
        print("\n----------------Resetting data folder----------------")
        resp = input("Delete csv files [y/n]: ")
        if resp =="y" or resp == "Y":
            delete_all_csv()
        else:
            print("CSV files available at data/")

if __name__ == '__main__':
    main()
