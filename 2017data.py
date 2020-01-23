import pandas as pd
import preprocess as pp

ks4pro2017 = pd.read_csv('data/815_2017_ks4final.csv',
                         usecols=("URN","SCHNAME","PTEBACC_95","P8_BANDING","ATT8SCR"),dtype={'URN': 'S75'})

ks4final2017['URN'] = pp.clean_urn(ks4final2017['URN'])

census2017 = pd.read_csv('data/815_2017_census.csv', usecols=("URN", "PNUMEAL"))
cfr2017 = pd.read_csv('data/815_2017_cfr.csv', usecols=('URN', 'TOTALINCOME'))

#merge all the 2017 tables

merge2017 = pd.merge(left=ks4pro2017,right=census2017, how='left', left_on='URN', right_on='URN')
merge2017 = pd.merge(left=merge2017,right=cfr2017, how='left', left_on='URN', right_on='URN')

merge2017['YEAR'] = '2017'

# locate the right schools.
skipsch2017 = merge2017.loc[(merge2017['URN'] == "136664") | (merge2017['URN'] == "141179") | (merge2017['URN'] == "121716") | (merge2017['URN'] == "121690")]



print(skipsch2017.head())