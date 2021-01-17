import streamlit as st
from data_cleaning.cleaner import Cleaner
import time

def pipeline(dataframe, n_rows, n_cols, required_cols, timestamp_cols, dataset_profile):
    placeholder = st.empty()
    c = Cleaner(dataframe, dataset_profile)

    placeholder.text("0: Checking data shape...")
    c.check_shape(expected_shape=(n_rows, n_cols))

    placeholder.text("1: Checking data columns...")
    c.check_required_cols(required_cols)

    placeholder.text("2: Checking column types...")
    c.check_col_types()

    placeholder.text("3: Indexing timestamp...")
    c.set_timestamp_index(timestamp_cols)
    time.sleep(1)

    placeholder.text("4: Dropping duplicates...")
    c.drop_duplicates()
    time.sleep(1)

    placeholder.text("5: Restoring missing values...")
    c.restore_missing_values()
    time.sleep(1)

    placeholder.text("6: Replacing outliers...")
    c.replace_outliers()
    time.sleep(1)
    placeholder.text("Cleaning process completed")

    return c.df
