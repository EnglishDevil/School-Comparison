import pandas as pd
import preprocess as pp


def get_school_data(year: int) -> pd.DataFrame:
    """Get the school data for the requested year
    Inputs:
    -------
    year : int
    the year of the data you want

    'Outputs:
    --------
    merge : pd.DataFrame
    A dataframe of the school data for the requested year"""

    # the year for the data

    # import the three sets of data
    ks4 = pd.read_csv(f'data/815_{year}_ks4.csv',
                      usecols=("URN", "SCHNAME", "PTEBACC_95", "ATT8SCR"), dtype={'URN': 'S75'})
    ks4['URN'] = pp.clean_urn(ks4['URN'])  # clean away all the bullshit in the URN column
    census = pd.read_csv(f'data/815_{year}_census.csv', usecols=("URN", "PNUMEAL"))
    cfr = pd.read_csv(f'data/815_{year}_cfr.csv', usecols=('URN', 'TOTALINCOME'))

    # merge tables
    merge = pd.merge(left=ks4, right=census, how='left', left_on='URN', right_on='URN')
    merge = pd.merge(left=merge, right=cfr, how='left', left_on='URN', right_on='URN')

    # populate the year column
    merge['YEAR'] = str(year)

    return merge