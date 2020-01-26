# School comparison code

import pandas as pd
import skiptondata as sk

data2018 = sk.get_skipsch_data(2018)
data2019 = sk.get_skipsch_data(2019)
data2017 = sk.get_skipsch_data(2017)

print(data2017, data2018, data2019)