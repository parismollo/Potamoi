import streamlit as st
from data_cleaning.cleaner import Cleaner

# @st.cache
def pipeline(dataframe, n_rows, n_cols, required_cols, timestamp_cols):
    c = Cleaner(dataframe)
    #   Run cleaning techniques
    c.check_shape(expected_shape=(n_rows, n_cols))
    st.success("Test 1️⃣ successeful: Shape Check 💖")
    c.check_required_cols(required_cols)
    st.success("Test 2️⃣ successeful: Required Columns 💜")
    c.check_col_types()
    st.success("Test 3️⃣ successeful: Column types 💛")
    c.set_timestamp_index(timestamp_cols)
    st.success("Test 4️⃣ successeful: Timestamp index 💚")
    c.drop_duplicates()
    st.success("Test 5️⃣ successeful: Drop duplicates 💙")
    c.restore_missing_values()
    st.success("Test 6️⃣ successeful: Restore missing values 💟")
    c.replace_outliers()
    st.success("Test 7️⃣ successeful: Replace outliers 💘")
#   Print statistical report
#   Plot dataframe

    return c.df
