import pandas as pd
class HelperX:
    def read_data(self,path):
        self.df= pd.read_csv(path)
        
        return self.df
    def get_col_data(self,df):
        start_up=sorted(df['Startup Name'].unique().tolist())
        return start_up