# from data_fetching.data_gen import generate_data_files
# from data_fetching.delete_data_files import delete_all_csv
# from typing import List
# from data_integration.delete_tables import drop_all_tables

from PIL import Image
from data_integration.validate_data import validate_data
from data_integration.stock_in_db import stock_in_database
import streamlit as st
import pandas as pd


# Icons made by <a href="http://www.freepik.com/" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
st.set_page_config(
     page_title="Potamoi",
     page_icon="🌊",
     initial_sidebar_state="expanded",
 )

def get_file():
    uploaded_file = st.file_uploader("Choose a file", type=[".csv", ".json"])
    if uploaded_file is None:
        st.stop()
    return pd.read_csv(uploaded_file)


def main():
    image = Image.open('static/wave.png')
    image.thumbnail((120, 120))
    st.image(image)
    st.title("Potamoi CS")

    uploaded_file = get_file()
    valid = validate_data(uploaded_file)
    if valid:
        st.write(uploaded_file)
        table_name = st.text_input("Table Name")
        if not table_name:
            st.warning('Please input a table name.')
            st.stop()
        # stock_in_database(uploaded_file,table_name)
        st.success('Thank you for inputting a table name. Data is being uploaded to the cloud')
        st.button("Iniate Data Cleaning module")
    else:
        st.write("File not valid")
        st.stop()



    # upload csv file
    # validate_data
    # store on our database
    # proceed to cleaning
    # return clean data + report


# def run_simulation():
#     sensors: List[str] = ["rainfall", "soil_moisture", "river_stage"]
#     print("\n----------------Data Generation----------------")
#     n_rows = int(input("\nInput the number of rows you'd like to generate: "))
#     generate_data_files(sensors, n_rows)
#     print("\n----------------Validating files----------------")
#     valid_files = validate_data()
#     if len(valid_files) != 0:
#         for i in range(len(valid_files)):
#             table_name = valid_files[i][5:-4]
#             df = pd.read_csv(str(valid_files[i]))
#             stock_in_database(df,table_name)
#
#         # drop_all_tables(valid_files)
#         # final_data = clean_data(valid_files) -> cleaning process
#         # data_report(final_data)
#         resp = input("Delete csv files [y/n]: ")
#         if resp =="y" or resp == "Y":
#             print("\n----------------Resetting data folder----------------")
#             delete_all_csv()
#         else:
#             print("CSV files available at data/")

if __name__ == '__main__':
    main()
