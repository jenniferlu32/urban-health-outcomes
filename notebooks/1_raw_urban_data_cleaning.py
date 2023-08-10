import pandas as pd;
import numpy as np;
pd.options.display.max_rows=None
pd.options.display.max_columns=None
import re
import os
os.getcwd()

#import urban growth %, urban population %, income group
urb_growth = pd.read_csv(r'../raw/urbanization/urbanization_growth.csv',low_memory=False)
urb = pd.read_csv(r'../raw/urbanization/urbanization_perc.csv', low_memory=False)
income = pd.read_csv(r'../raw/urbanization/income_group.csv', low_memory=False)

income.head()

income = income[['Country Code', 'Region', 'IncomeGroup']]
income.columns = ['country_code', 'region', 'income_group']

#remove " [YRXXXX]"" in year columns
def remove_brackets(year):
    #substitue " []" with ""
    return re.sub(r'\s*\[.*?\]', '', year)

def urb_transform(df, value_name):
    #set new year fields to remove [YRXXXX]
    df.columns = [remove_brackets(year) for year in df.columns]
    
    #transform data to show country, country code, and year
    df = df.melt(id_vars=['Country Name', 'Country Code'],
            value_vars=[str(year) for year in range(1998,2022)],
            var_name='year',
            value_name=value_name
            )
    
    df.columns = ['country', 'country_code', 'year', value_name]
    
    return df

#clean urban growth and urban % data
urb_growth = urb_transform(urb_growth, 'urb_growth')
urb = urb_transform(urb, 'urb_rate')

urb_growth.head()
urb.head()

len(urb)
urb.country.nunique()
len(urb_growth)
urb_growth.country.nunique()
income.country_code.nunique()

#join income data with urb rate and urb growth
urb_df = pd.merge(income, urb, on='country_code', how='left')
urb_df = pd.merge(urb_df, urb_growth, on=['country_code', 'country', 'year'], how='left')

len(urb_df)

urb_df.head()

#remove all blank rows
urb_df = urb_df[urb_df['urb_rate'].notna()]

len(urb_df)

urb_df.head()

#export urbanization data
urb_df.to_csv(r'urb_data.csv', header=True, index=False, encoding='utf-8')