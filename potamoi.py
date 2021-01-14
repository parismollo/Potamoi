# from data_fetching.data_gen import generate_data_files
# from data_fetching.delete_data_files import delete_all_csv
# from typing import List
# from data_integration.delete_tables import drop_all_tables

from PIL import Image
from data_integration.validate_data import validate_data
from data_integration.stock_in_db import stock_in_database
import streamlit as st
import pandas as pd
from user_interface.params import sidebar_params
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
    # valid = validate_data(uploaded_file)
# if valid:
    st.write(uploaded_file)
    table_name = st.text_input("Table Name")
    if not table_name:
        st.warning('Please input a table name.')
        st.stop()
        # stock_in_database(uploaded_file,table_name)
    st.info('Thank you for inputting a table name. Data is being uploaded to the cloud')
    # if st.checkbox("Iniate Data Cleaning module"):
    sidebar_params(uploaded_file)

    # else:
    #     st.stop()

    # else:
    #     st.write("File not valid")
    #     st.stop()
if __name__ == '__main__':
    main()
