# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 23:18:06 2024

@author: vmbay
"""

#COUNTRY DATA
import pandas
file = pandas.read_csv("country_data.csv")
print(file)
print(file.info())

import pandas as pd
df = pd.DataFrame(file)
print(df.describe())

# DIABETES DATA
import pandas as pd
file = pandas.read_csv("diab_data.csv")
df = pd.DataFrame(file)
print(file)
print(file.info())
print(df.describe())

# HOUSING DATA
import pandas as pd
file = pandas.read_csv("housing_data.csv")
print(file)
print(file.info())
df = pd.DataFrame(file)
print(df.describe())

# INSURANCE DATA
import pandas as pd
file = pandas.read_csv("insurance_data.csv")
print(file)
print(file.info())
df = pd.DataFrame(file)
print(df.describe())

# IRIS DATA
import pandas as pd
file = pandas.read_csv("iris.csv")
print(file)
print(file.info())
df = pd.DataFrame(file)
print(df.describe())

