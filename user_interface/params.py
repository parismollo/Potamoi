import streamlit as st
import base64
from data_cleaning.run_cleaner import pipeline
from io import BytesIO
import pandas as pd


def sidebar_params(df):
    # check shape params (shape): tuple
    print(df.shape)
    n_rows = st.sidebar.number_input("N° of rows?")
    n_cols = st.sidebar.number_input("N° of cols?")
    # check required cols (cols): list
    required_col = st.sidebar.radio("Minimum Col check: ", ("Summary", "Datetime", "Measurement"))
    req_cols = [required_col]
    # timestamp index (cols) : list
    timestamp_cols = st.sidebar.multiselect("Data Time cols?", df.columns)
    print(timestamp_cols)

    if st.button("Ready?"):
        df = pipeline(df, n_rows, n_cols, req_cols, timestamp_cols)
        # stock_in_database(df,table_name)
        tmp_download_link = download_link(df, 'YOUR_DF.csv', 'Click here to download your data!')
        st.markdown(tmp_download_link, unsafe_allow_html=True)
    else:
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
# @st.cache(suppress_st_warning=True)
def get_shape_params():
    pass



# @st.cache(suppress_st_warning=True)
def get_required_cols_params():
    pass


# @st.cache(suppress_st_warning=True)
def get_timestamp_cols_params(df):
    pass
