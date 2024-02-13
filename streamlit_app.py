import streamlit as st 
from streamlit_option_menu import option_menu
st.set_page_config(page_title="Data Analysis", page_icon="📅",layout='wide')

from utils.funds import IndianFunds
funds=IndianFunds()
from utils.home import home

class MyApp:
    """
    This class is main class of this application
    """
    # Constructor of class
    def __init__(self):
        # st.title("Data Analysis")
        self.apps = []
        # st.markdown("---")
        
    def add_app(self, title, function):
        self.apps.append({"title": title, "function": function})


    def run(self):
        """
        This method run the streamlit app
        """
        with st.sidebar:
            app = option_menu(
                menu_title='Domain Zone',
                options=['Home', 'Indian Funds'],
                icons=['house-heart', 'data'],
                menu_icon='chat-text-fill',
                default_index=0,

                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "20px"},
                    "nav-link": {"color": "white", "font-size": "20px", 
                                 "text-align": "left", "margin": "0px",
                                 "--hover-color": "magenta"},
                    "nav-link-selected": {"background-color": "#02ab21"}, })
      
        if app=="Home":
            
            home()
        if app=="Indian Funds":
            funds.funds()



if __name__ == "__main__":
    app = MyApp()  # Object of classa
    app.run()
