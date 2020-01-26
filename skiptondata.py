import pandas as pd
from importmerge import get_school_data

def get_skipsch_data(year : int) -> pd.DataFrame:
    school_data = get_school_data(year)
    skipsch = merge.loc[school_data['URN'].isin(["136664","141179","121716","121690"])] # SAM - can use ".isin()" method to replace all those OR statements you had before

    return skipsch