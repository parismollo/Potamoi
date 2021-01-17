import streamlit as st
import base64
from data_cleaning.pipeline import pipeline
from io import BytesIO
import pandas as pd
from PIL import Image
import requests

def data_quality_control():
    st.title("Data Quality Control")
    text ='''
    This is Potamoi's **Data Quality Control** API, here you will be able to clean and prepare your data for a multiple number of
    purposes, such as **model training, exploratory analysis and data collection**.
    '''
    st.info(text)
    st.header("How it works")
    text_2 = '''
    Potamoi provides **3 levels of data quality control**.
    The more cleaning levels you want to apply to your data, **more complex and more input we need from the user.**\n
    * Upload your csv file
    * Select the cleaning level
    * Input the preprocessing parameters
    * Download the data ready for use!
    '''
    st.success(text_2)
    st.sidebar.selectbox("Cleaning Level", ("Level 1", "Level 2", "Level 3"))
    image = Image.open('static/potamoi_diagram.png')
    st.image(image)

    st.subheader("Start Here")
    uploaded_file = get_file()

    with st.spinner("Loading data..."):
        st.write(uploaded_file)
    table_name = st.text_input("Dataset Name")

    if not table_name:
        st.warning('Please input a name for this dataset.')
        st.stop()
        # stock_in_database(uploaded_file,table_name)
    # st.info('Thank you for inputting a table name. Data is being uploaded to the cloud')
    # if st.checkbox("Iniate Data Cleaning module"):
    st.sidebar.subheader("Set your parameters")
    sidebar_params(uploaded_file)


def get_file():
    uploaded_file = st.file_uploader("Choose a file", type=[".csv"])
    if uploaded_file is None:
        st.stop()
    return pd.read_csv(uploaded_file)


def sidebar_params(df):
    # check shape params (shape): tuple

    n_rows = st.sidebar.number_input("N° of rows?")
    n_cols = st.sidebar.number_input("N° of cols?")
    # check required cols (cols): list
    required_col = st.sidebar.radio("Minimum Col check: ", ("Summary", "Datetime", "Measurement"))
    req_cols = [required_col]
    # timestamp index (cols) : list
    timestamp_cols = st.sidebar.multiselect("Data Time cols?", df.columns)

    if st.button("Start Cleaning"):
        text = '''
        Running cleaning techniques...\n
        * Data shape
        * Data columns
        * Timestamp
        * Duplicates
        * Missing Values
        * Outliers
        '''
        with st.spinner(text):
            df = pipeline(df, n_rows, n_cols, req_cols, timestamp_cols)
        # stock_in_database(df,table_name)
        tmp_download_link = download_link(df, 'YOUR_DF.csv', 'Click here to download your data!')
        st.markdown(tmp_download_link, unsafe_allow_html=True)
    else:
        st.error("Set your parameters **before** starting the cleaning process")
        st.stop()

# def to_excel(df):
#     output = BytesIO()
#     writer = pd.ExcelWriter(output, engine='xlsxwriter')
#     df.to_excel(writer, sheet_name='Sheet1')
#     writer.save()
#     processed_data = output.getvalue()
#     return processed_data


def download_link(object_to_download, download_filename, download_link_text):
    """
    Generates a link to download the given object_to_download.

    object_to_download (str, pd.DataFrame):  The object to be downloaded.
    download_filename (str): filename and extension of file. e.g. mydata.csv, some_txt_output.txt
    download_link_text (str): Text to display for download link.

    Examples:
    download_link(YOUR_DF, 'YOUR_DF.csv', 'Click here to download data!')
    download_link(YOUR_STRING, 'YOUR_STRING.txt', 'Click here to download your text!')

    """
    if isinstance(object_to_download,pd.DataFrame):
        object_to_download = object_to_download.to_csv(index=True)

    # some strings <-> bytes conversions necessary here
    b64 = base64.b64encode(object_to_download.encode()).decode()

    return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'
