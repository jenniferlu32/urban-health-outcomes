import pandas as pd
import numpy as np
pd.options.display.max_rows = None
pd.options.display.max_columns = None

#import public health data
pub = pd.read_csv(r'../raw/wellbeing_data/global_burden_of_disease.csv', low_memory=False)
#import world happiness data
wh = pd.read_excel(r'../raw/wellbeing_data/world_happiness_report.xls')

wh.head()

len(wh)

#countries
wh['Country name'].nunique()

wh.count()

#data availability by country and year

data_avail = wh.groupby(['Country name', 'year']).count().reset_index()

#get sum of all values for each row
data_avail['col_sum'] = data_avail.iloc[:,2:].sum(axis=1)

#total values
total_measures = 9
data_avail['complete_perc'] = round((data_avail['col_sum']/total_measures)*100,2)

data_avail.head()

#data available by country
avail_country = data_avail.pivot_table(index='Country name',columns='year', values='complete_perc').fillna(0).reset_index()

avail_country.head()

#average data availability by country
avail_country['avg_data'] = round(avail_country.iloc[:,2:].mean(axis=1),2)

avail_country.head()

#remove 24 countries with < 50% yearly data available

exclude = ['Cuba','Maldives','Oman','Suriname','Guyana','Belize','Somaliland region','Bhutan','Eswatini','Somalia','South Sudan','Qatar','Djibouti','Gambia','Angola','Lesotho','Central African Republic','Trinidad and Tobago','Burundi','Sudan','Libya','Comoros','Syria','Namibia']
wh = wh[~(wh['Country name'].isin(exclude))]

wh.head()

#get only physical + mental health measures
wh = wh[['Country name', 'year', 'Healthy life expectancy at birth', 'Social support', 'Freedom to make life choices', 'Positive affect']]

#rename columns
wh.columns = ['country', 'year', 'life_exp', 'support', 'freedom', 'pos_aff']

#export data
wh.to_csv(r'health_outcome.csv', header=True, index=False, encoding='utf-8')