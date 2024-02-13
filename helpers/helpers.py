import pandas as pd
class HelperX:
    def read_data(self,path):
        self.df= pd.read_csv(path)
        self.df['Investors Name']=self.df['Investors Name'].fillna("Undisclosed")
        return self.df
    def get_col_data(self,df,tag):
        if tag=='Start-up':
            start_up=sorted(df['Startup Name'].unique().tolist())
            return start_up
        if tag=='Investor':
            investors=sorted(df['Investors Name'].unique().tolist())
            return investors
            