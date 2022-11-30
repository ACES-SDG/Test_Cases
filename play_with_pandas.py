import pandas as pd


df =pd.read_csv("D:\Excel_files\Sample - Superstore.csv")
df['Order Date'] = pd.to_datetime( df['Order Date'])
x = df['Order Date'].dt.day_name().unique()
y = tuple(x)
print(type(x),f'\n {x}')
print(type(y),f'\n {y}')
