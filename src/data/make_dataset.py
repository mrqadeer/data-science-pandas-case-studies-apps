# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import pandas as pd
import pathlib,yaml,sys
curr_dir = pathlib.Path(__file__)
home_dir = curr_dir.parent.parent.parent
params_file = home_dir.as_posix() + '/config.yaml'
paths = yaml.safe_load(open(params_file))
class IndianFundingDataAnalysis:

    def read_csv(self,path):
        df=pd.read_csv(path)
        return df
    
    
    def clean_data(self,df):
        return df.head()
    
    
    def run(self):
        raw_data=paths['paths']['raw_data']
        df=self.read_csv(raw_data)
        return df

if __name__=="__main__":
    c=IndianFundingDataAnalysis()
    df=c.run()
    print(df.head())
