import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', 200)

df_cities = pd.read_csv("./data/city_temps.csv")
df_global = pd.read_csv("./data/global_temps.csv")
df = pd.merge(df_global, df_cities, how = "outer", on =["year"]).sort_values(by=["year"])

df.rename(columns = 
          {'avg_temp_y':'city_temp',
          'avg_temp_x':'global_temp'}, inplace = True)

df['global_10y_MA'] = df['global_temp']  .rolling(10).mean()
df['city_10y_MA'] = df['city_temp']      .rolling(10).mean()

x = df['year']
y_global = df['global_temp']
y_global_max = max(df['global_temp'])
x_global_max = df.loc[df['global_temp'] == y_global_max, 'year'].iloc[0]

