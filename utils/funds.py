import streamlit as st 
from datetime import date
from helpers.helpers import HelperX

helper = HelperX()
import pathlib,yaml,sys
curr_dir = pathlib.Path(__file__)
home_dir = curr_dir.parent.parent
params_file = home_dir.as_posix() + '/config.yaml'
paths = yaml.safe_load(open(params_file))
def funds():

    
    if 'select' not in st.session_state:
        st.session_state.select = "Select"
    if 'options' not in st.session_state:
        st.session_state.options=""
    st.header("Indian Funds")
    
        
    options=st.selectbox("Select One",["Overall","Start Up","Investors"])
    st.session_state.options=options
    if st.session_state.options=='Start Up':
        start_up = helper.get_col_data("Start-up")
        select_start_up = st.selectbox("Select StartUp", start_up)
        startup_results=st.button("See Result",key='start_up')
    if st.session_state.options=='Investors':
        investors = helper.get_col_data('Investor')
        selected_investor = st.selectbox("Select Investor", investors,placeholder="Select an Investor")
        invstor_results=st.button("See Result",key='investor')
        if invstor_results:
            st.title(selected_investor) 
            with st.expander("Most Recent Investment"):
                investor_detail=helper.get_investor_data(selected_investor)
                st.dataframe(investor_detail,width=1000)
            with st.expander("Biggest Investment Investor"):
                big_investment=helper.get_investor_biggest_investment(selected_investor)
                st.dataframe(big_investment,width=1000)
            
