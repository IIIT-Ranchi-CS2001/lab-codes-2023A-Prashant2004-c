import pandas as pd
import numpy as np
df = pd.read_csv('AQI_Data.csv')

# grouping the data by city and calculating the avg AQI and max PM10 level
grouped_data = df.groupby('City').agg(
    # --------------a = avg AQI value for each city-----------------
    avg_AQI=('AQI', 'mean'),
    # --------------a = max pm10 value of each city----------------
    max_PM10=('PM10', 'max')
).reset_index()

# --------------- uploading the data to the csv file---------------
grouped_data.to_csv('Citywise_AQI.csv', index=False)

# --------------- displaying the data -----------------------------
print(grouped_data)