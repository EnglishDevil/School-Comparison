#School comparison code

import pandas as pd
import preprocess as pp



ks4pro = pd.read_csv('data/815_2019_ks4provisional.csv', usecols=("URN","SCHNAME","PTEBACC_95","P8_BANDING","ATT8SCR"),dtype={'URN': 'S75'})
ks4pro_pp = pp.clean_urn(ks4pro['URN'])

ks4pro['URN'] = ks4pro['URN'].astype(str)
#strip the unwanted junk characters in the URN column
ks4pro['URN'] = ks4pro['URN'].map(lambda x: x.lstrip('b'').rstrip('''))
ks4pro['URN'] = ks4pro['URN'].str.replace("'", "")

census2019 = pd.read_csv('data/815_2019_census.csv', usecols=("URN", "PNUMEAL"))
cfr2019 = pd.read_csv('data/815_2019_cfr.csv', usecols=('URN', 'TOTALINCOME'))

#merge all the 2019 tables

merge2019 = pd.merge(left=ks4pro,right=census2019, how='left', left_on='URN', right_on='URN')
merge2019 = pd.merge(left=merge2019,right=cfr2019, how='left', left_on='URN', right_on='URN')

#need to fix it so the URN column doesnt give a decimal place to the data
skipsch2019 = merge2019.loc[(ks4pro['URN'] == "136664") | (merge2019['URN'] == "141179") | (merge2019['URN'] == "121716") | (merge2019['URN'] == "121690")]

#merge2019.loc[(merge2019['SCHNAME'] == "The Skipton Academy")]

skipsch2019.info()