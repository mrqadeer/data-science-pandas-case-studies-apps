import pandas as pd
import streamlit as st
import pathlib,yaml
curr_dir = pathlib.Path(__file__)
home_dir = curr_dir.parent.parent
params_file = home_dir.as_posix() + '/config.yaml'
paths = yaml.safe_load(open(params_file))
class HelperX:
    def __init__(self):
        file = paths['paths']['processed_data']
        self.df= pd.read_csv(file)
        
    def get_col_data(self,tag):
        if tag=='Start-up':
            start_up=sorted(self.df['Startup'].unique().tolist())
            return start_up
        if tag=='Investor':
            investors=sorted(set(self.df["Investors"].str.split(",").sum()))
            return investors
    def min_max_date(self):
        min_date = pd.to_datetime(self.df["Date"]).min()
        max_date = pd.to_datetime(self.df["Date"]).max()
        return min_date,max_date
    
    def get_investor_data(self,investor):
        
        return self.df[self.df["Investors"].str.contains(investor)].head().iloc[:,[0,1,2,4,6,7]]
    def get_investor_biggest_investment(self,investor):
        return self.df[self.df["Investors"].str.contains(investor)].groupby('Startup')['Amount'].sum().sort_values(ascending=False)
        
