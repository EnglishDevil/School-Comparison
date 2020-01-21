import pandas as pd

def clean_urn(urn_series):

    urn_series = urn_series.astype(str)
    #strip the unwanted junk characters in the URN column
    urn_series = urn_series.map(lambda x: x.lstrip('b'').rstrip('''))
    urn_series = urn_series.str.replace("'", "")

    return urn_series