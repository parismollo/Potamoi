import streamlit as st
import pandas as pd
from user_interface.quality_control import download_link

def display_df(df,header,col):
    col.header(header)
    col.write(df)
    tmp_download_link3 = download_link(df ,'YOUR_df.csv' ,'Download')
    col.markdown(tmp_download_link3, unsafe_allow_html=True)
    

def home():
    df = pd.read_csv('user_interface/submissionRFC_nosplit.csv')
    st.title("How it works ?")
    st.subheader('The Problem :bulb:')
    st.write("In an ideal world, the data collected by meteorological stations, radars, or wireless sensors networks is stored in **databases and processed** by the **hydrological models** that output the flood forecast. **However**, not all countries have a **centralized database** that is continually receiving the most recent data. The data can sometimes be temporarily stored in spreadsheets, a cheaper and less sophisticated way to check the quality of the data before its sent to the central database. However, this can take weeks or even months to preprocess. ")

    
    st.subheader('The Idea :bulb:')
    st.write("**Potamoi** is a service that provides **data quality control** for flood forecast centers,it manages the data flow between data collectors and hydrological models, by performing numerous **data cleaning** and **preprocessing** techniques, such as validity and completeness, statistical quality control and missing values restoration.  ")
     
    col1, col2, col3 = st.beta_columns(3) 
    display_df(df,"DF1",col1)
    display_df(df,"DF2",col2)
    display_df(df,"DF3",col3)
    
    
 
