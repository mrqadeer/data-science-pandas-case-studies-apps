import streamlit as st 

import pandas as pd

def home():
    st.header("Home")
    data=st.file_uploader("Upload file",type=['csv'])
    st.session_state['data']=data
    