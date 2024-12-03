import pandas as pd
import numpy as np
df = pd.read_csv('AQI_Data.csv')

# --------------------first 5 rows of dataset-------------------
first_part = df.head(5)
print( "First 5 rows of dataset df are:\n",first_part)

# ----------------last 6 rows of dataset---------------------------
second_part=df.tail(6)
print("Last 6 rows of dataset df are:\n",second_part)

# -------------statistical(numerical) information of all cities----------- 
third_part=df.describe()
print("numerical information of all cities:\n",third_part)

# ----------------mean of AQI  , PM2.5 , PM10------------------------
fourth_part = df.groupby('City').agg(
    AQI_mean=('AQI', lambda bc: np.mean(bc)),
    PM25_mean=('PM2.5', lambda bc: np.mean(bc)),
    PM10_mean=('PM10', lambda bc: np.mean(bc))
).reset_index()
print("mean of the given parameters of all the cities\n",fourth_part)

