import streamlit as st 
from helpers.helpers import HelperX

helper = HelperX()

def funds():
    if 'file' not in st.session_state:
        st.session_state.file = ""
        
    if 'select' not in st.session_state:
        st.session_state.select = "Select"
        
    st.header("Indian Funds")
    with st.expander("Load Data"):
        file = st.file_uploader("Upload CSV file", type='csv')
        st.session_state.file = file
        load = st.button("Load Data")
        if file is not None and load:
            df = helper.read_data(file)
            st.session_state.df = df  # Store the DataFrame in session state
    with st.expander("Analysis"):
        if 'df' in st.session_state:
            options=st.selectbox("Select One",["Overall","Start Up","Investors"])
        
            if options=='Start Up':
                start_up = helper.get_col_data(st.session_state.df,"Start-up")
                select = st.selectbox("Select StartUp", start_up)
                find_start_up=st.button("Find Start Up")
            elif options=='Investors':
                investors = helper.get_col_data(st.session_state.df,'Investor')
                select = st.selectbox("Select StartUp", investors)
                find_investors=st.button("Find Investors")
                    