import pandas as pd
import preprocess as pp

# the year for the data
year = 2018

# import the three sets of data
ks4 = pd.read_csv(f'data/815_{year}_ks4.csv',
                         usecols=("URN","SCHNAME","PTEBACC_95","P8_BANDING","ATT8SCR"),dtype={'URN': 'S75'})
ks4['URN'] = pp.clean_urn(ks4['URN'])  # clean away all the bullshit in the URN column
census = pd.read_csv(f'data/815_{year}_census.csv', usecols=("URN", "PNUMEAL"))
cfr = pd.read_csv(f'data/815_{year}_cfr.csv', usecols=('URN', 'TOTALINCOME'))

# merge tables
merge = pd.merge(left=ks4,right=census, how='left', left_on='URN', right_on='URN')
merge = pd.merge(left=merge,right=cfr, how='left', left_on='URN', right_on='URN')

# populate the year column
merge['YEAR'] = str(year)

# locate the right schools.
skipsch = merge.loc[(merge['URN'] == "136664") | (merge['URN'] == "141179") | (merge['URN'] == "121716") | (merge['URN'] == "121690")]

