# School comparison code

import pandas as pd
import preprocess as pp


ks4pro = pd.read_csv('data/815_2019_ks4provisional.csv', usecols=("URN","SCHNAME","PTEBACC_95","P8_BANDING","ATT8SCR"),dtype={'URN': 'S75'})
ks4pro['URN'] = pp.clean_urn(ks4pro['URN'])


census2019 = pd.read_csv('data/815_2019_census.csv', usecols=("URN", "PNUMEAL"))
cfr2019 = pd.read_csv('data/815_2019_cfr.csv', usecols=('URN', 'TOTALINCOME'))

# merge all the 2019 tables

merge2019 = pd.merge(left=ks4pro,right=census2019, how='left', left_on='URN', right_on='URN')
merge2019 = pd.merge(left=merge2019,right=cfr2019, how='left', left_on='URN', right_on='URN')

#add year to the 2019 table

merge2019['YEAR'] = '2019'

# locate the right schools.
skipsch2019 = merge2019.loc[(merge2019['URN'] == "136664") | (merge2019['URN'] == "141179") | (merge2019['URN'] == "121716") | (merge2019['URN'] == "121690")]


# multi merge all of the tables
# first load all of the tables
from functools import reduce

ks42018 = pd.read_csv('data/815_2018_ks4final.csv', usecols=("URN","SCHNAME","PTEBACC_95","P8_BANDING","ATT8SCR"),dtype={'URN': 'S75'})
ks42018 = pp.clean_urn(ks42018['URN'])
census2018 = pd.read_csv('data/815_2018_census.csv', usecols=("URN", "PNUMEAL"))
cfr2018 = pd.read_csv('data/815_2018_cfr.csv', usecols=('URN', 'TOTALINCOME'))

#2019 = [ks4pro, census2019, cfr2019]
#2018 = [ks42018, census2018, cfr2018]


print(skipsch2019.head())

# Need to restructure like before, getting the final table for 2019 then adding a 2019 year column.
# do not merge the year by year data, we can append it to the dataset.