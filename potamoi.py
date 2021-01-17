# from data_fetching.data_gen import generate_data_files
# from data_fetching.delete_data_files import delete_all_csv
# from typing import List
# from data_integration.delete_tables import drop_all_tables

from PIL import Image
from data_integration.validate_data import validate_data
from data_integration.stock_in_db import stock_in_database
import streamlit as st
import pandas as pd
from user_interface.quality_control import sidebar_params, data_quality_control
from user_interface.home import home
# Icons made by <a href="http://www.freepik.com/" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
st.set_page_config(
     page_title="Potamoi",
     page_icon="🌊",
     initial_sidebar_state="expanded"
 )


def main():
    image = Image.open('static/wave.png')
    image.thumbnail((120, 120))
    st.sidebar.image(image)
    st.sidebar.title("Potamoi CS")
    app_mode = st.sidebar.selectbox(
        "App Mode",
        ("Datasets", "Data Quality Control")
    )

    if app_mode == "Datasets":
        home()
    elif app_mode == "Data Quality Control":
        data_quality_control()


if __name__ == '__main__':
    main()
