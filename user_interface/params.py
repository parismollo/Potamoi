import streamlit as st
from data_cleaning.run_cleaner import pipeline

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
        st.write(pipeline(df, n_rows, n_cols, req_cols, timestamp_cols))
    else:
        st.stop()

# @st.cache(suppress_st_warning=True)
def get_shape_params():
    pass



# @st.cache(suppress_st_warning=True)
def get_required_cols_params():
    pass


# @st.cache(suppress_st_warning=True)
def get_timestamp_cols_params(df):
    pass
