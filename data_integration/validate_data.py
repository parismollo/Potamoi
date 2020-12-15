import os
from os import listdir
from os.path import join
import pandas as pd
import streamlit as st

# TODO: filter data we want

# def filter(dataframe):
#     return dataframe.iloc[["id", "value"]]

@st.cache
def check_target_cols(target, df):
    '''
    Check if all minimal target columns are in the dataframe.
    '''
    is_valid = True
    for col in target:
        is_valid = is_valid and (col in df.columns)
    return is_valid
    
@st.cache
def validate_data(df, target=["value", "id"]):
    if check_target_cols(target, df):
        print(f"File has been validated.")
        return True
    else:
        return False




# def validate_data(max_size=10000, data_dir="data/", accepted_file_formats = (".json", ".csv"), target=["value", "id"]):
#     valid_files = []
#     try:
#         directory_path = os.listdir(data_dir)
#         for filename in directory_path:
#             path = os.path.join(data_dir, filename)
#             if filename.endswith(accepted_file_formats) and os.path.getsize(path) <= max_size:
#                 if check_target_cols(target, path):
#                     valid_files.append(path)
#                     print(f"File {path} has been validated.")
#                 else:
#                     print(f"File {path} not valid (check file columns)")
#             else:
#                 print(f"File {path} not valid (check format or size)")
#     except Exception as e:
#         print(e)
#
#     return valid_files
