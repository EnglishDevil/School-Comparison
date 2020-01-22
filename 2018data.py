import pandas as pd
import preprocess as pp

ks4pro2018 = pd.read_csv('data/815_2018_ks4final.csv',
                         usecols=("URN","SCHNAME","PTEBACC_95","P8_BANDING","ATT8SCR"),dtype={'URN': 'S75'})

ks4pro2018['URN'] = pp.clean_urn(ks4pro2018['URN'])

census2018 = pd.read_csv('data/815_2018_census.csv', usecols=("URN", "PNUMEAL"))
cfr2018 = pd.read_csv('data/815_2018_cfr.csv', usecols=('URN', 'TOTALINCOME'))

#merge all the 2018 tables

merge2018 = pd.merge(left=ks4pro2018,right=census2018, how='left', left_on='URN', right_on='URN')
merge2018 = pd.merge(left=merge2018,right=cfr2018, how='left', left_on='URN', right_on='URN')


print(merge2018.head())