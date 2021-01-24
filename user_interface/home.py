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
    st.subheader('The Idea :bulb:')
    st.write("fbjezkbkfezkfzekze")
    col1, col2, col3 = st.beta_columns(3)
    
    display_df(df,"DF1",col1)
    display_df(df,"DF2",col2)
    display_df(df,"DF3",col3)
    # faire la page comme dans le dessin
    # query datasets
    # pour chaque dataset:
        # afficher nom
        # transformer dataframe
        # disponibilize lien pour telechager
