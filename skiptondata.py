import pandas as pd
import importmerge as im

def get_skipsch_data(year : int) -> pd.DataFrame:  #this means that the year must be an int and the output will be a dataframe
    school_data = im.get_school_data(year)
    skipsch = school_data.loc[school_data['URN'].isin(["136664","141179","121716","121690"])] # SAM - can use ".isin()" method to replace all those OR statements you had before

    return skipsch