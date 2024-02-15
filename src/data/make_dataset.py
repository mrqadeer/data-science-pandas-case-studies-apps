# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import pandas as pd
import pathlib, yaml, sys

curr_dir = pathlib.Path(__file__)
home_dir = curr_dir.parent.parent.parent
params_file = home_dir.as_posix() + '/config.yaml'
paths = yaml.safe_load(open(params_file))


class IndianFundingDataAnalysis:

    def read_csv(self, path):
        df = pd.read_csv(path)
        return df

    def clean_data(self, df):
        df.set_index("Sr No", inplace=True)
        df.drop('Remarks', axis=1, inplace=True)
        df.rename(columns={"Date dd/mm/yyyy": "Date", "City  Location": "City", "Startup Name": "Startup",
                           'Industry Vertical': "Vertical", 'InvestmentnType': "Round", "Investors Name": "Investors",
                           'Amount in USD': "Amount"}, inplace=True)
        df['Amount'] = df['Amount'].fillna("0")
        df['Amount'] = df["Amount"].str.replace("undisclosed", "0")
        df['Amount'] = df["Amount"].str.replace("unknown", "0")
        df['Amount'] = df["Amount"].str.replace("Undisclosed", "0")
        df['Amount'] = df['Amount'].str.replace(",", '')
        df = df[df['Amount'].str.isdigit()]
        df['Amount']=df['Amount'].astype('float')
        df['Amount'] = df['Amount'].apply(lambda dollar: (dollar * 82.5) / 10000000)
        df["Date"] = df["Date"].str.replace("05/072018", "05/07/2018")
        df["Date"] = pd.to_datetime(df["Date"], errors='coerce',format="%d/%m/%Y")
        df.dropna(subset=['Date', 'Startup', 'Vertical', 'City', 'Investors',
                          'Round', 'Amount'], inplace=True)
        return df
    def run(self):
        
        raw_data = paths['paths']['raw_data']
        df = self.read_csv(raw_data)
        cleaned_df=self.clean_data(df)
        cleaned_df.to_csv(r"data\processed\processed_data.csv",index=False)
        return cleaned_df


if __name__ == "__main__":
    c = IndianFundingDataAnalysis()
    df = c.run()
    print(df.head())
