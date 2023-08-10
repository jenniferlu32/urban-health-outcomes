import pandas as pd
pd.options.display.max_rows = None
pd.options.display.max_columns = None
import numpy as np

#import urbanization + public health data
wh = pd.read_csv(r'../interim/health_outcome.csv', low_memory=False)
urb = pd.read_csv(r'../interim/urb_data.csv', low_memory=False)

len(wh)
len(urb)

#remove data from 2020 onwards
wh = wh[wh['year']<2020]

urb.head()
wh.head()

urb.country.nunique()
wh.country.nunique()

#correct naming differences
country_mapping = {
    'Congo, Rep.':'Congo (Brazzaville)',
    'Congo, Dem. Rep.':'Congo (Kinshasa)',
    'Egypt, Arab Rep.': 'Egypt',
    'Hong Kong SAR, China': 'Hong Kong S.A.R. of China',
    'Iran, Islamic Rep.': 'Iran',
    'Kyrgyz Republic': 'Kyrgyzstan',
    'Lao PDR': 'Laos',
    'Russian Federation': 'Russia',
    'Slovak Republic': 'Slovakia',
    'Venezuela, RB': 'Venezuela',
    'Yemen, Rep.': 'Yemen',
    'Korea, Rep.':'South Korea'
    }

urb['country'].replace(country_mapping, inplace=True)

urb[urb['country']=='Egypt']

#join urban data to wh
df = pd.merge(wh, urb, on=['country', 'year'], how='left')

df.count()

df.income_group.unique()

#fill missing values

df.count()