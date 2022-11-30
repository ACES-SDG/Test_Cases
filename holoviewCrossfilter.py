import pandas as pd
import altair as alt
churn = pd.read_excel("C:/Users/Mazhar/OneDrive/Desktop/LIve_Working/Ocean Pro V_3.0.0/Excel_files/sales.xlsx")

features = ['Row ID', 'Order ID', 'Order Date', 'Ship Date', 'Ship Mode',
       'Customer ID', 'Customer Name', 'Segment', 'Country/Region', 'City',
       'State', 'Postal Code', 'Region', 'Product ID', 'Category',
       'Sub-Category', 'Product Name', 'Sales', 'Quantity', 'Discount',
       'Profit']
churn = churn[features].sample(n=100, ignore_index=True)
# print(churn.head())

# print(churn.columns)


alt.Chart(churn).mark_bar().encode(x='Ship Date', y='Sales').properties(height=300, width=400)