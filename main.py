from data_fetching.data_gen import generate_data_files
from data_fetching.delete_data_files import delete_all_csv
from typing import List
from data_fetching.validate_data import validate_data
# from data_integration.stock_in_db import stock_in_database
# from data_integration.delete_tables import drop_all_tables
import streamlit as st
import pandas as pd

def run_simulation():
    sensors: List[str] = ["rainfall", "soil_moisture", "river_stage"]
    print("\n----------------Data Generation----------------")
    n_rows = int(input("\nInput the number of rows you'd like to generate: "))
    generate_data_files(sensors, n_rows)
    print("\n----------------Validating files----------------")
    valid_files = validate_data()
    if len(valid_files) != 0:
        for i in range(len(valid_files)):
            table_name = valid_files[i][5:-4]
            df = pd.read_csv(str(valid_files[i]))
            # stock_in_database(df,table_name)

        # drop_all_tables(valid_files)
        # store_data(valid_files) - store data on our database
        # final_data = clean_data(valid_files) - cleaning process
        # send_user_data(user, final_data)
        resp = input("Delete csv files [y/n]: ")
        if resp =="y" or resp == "Y":
            print("\n----------------Resetting data folder----------------")
            # delete_all_csv()
        else:
            print("CSV files available at data/")

def main():
    st.title("Hello!")

if __name__ == '__main__':
    main()
    # app.run()
    # main()
