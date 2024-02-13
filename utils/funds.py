import streamlit as st 
from helpers.helpers import HelperX
helper=HelperX()
class IndianFunds:
    def __init__(self) -> None:
        self.df=None
    def funds(self):
        if 'file' not in st.session_state:
            st.session_state.file=""
        
        st.header("Indian Funds")
        with st.expander("Load Data"):
            file=st.file_uploader("Upload CSV file",type='csv')
            load=st.button("Load Data")
            if file is not None and load:
                self.df=helper.read_data(file)
                
                
            
            
                col1,col2=st.columns(2)
                with col1:
                    start_up=helper.get_col_data(self.df)
                    select=st.selectbox("Select StartUp",start_up)
            
    
    
    
    