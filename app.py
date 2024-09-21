import streamlit as st
import plotly_express as px
import pandas as pd
df = pd.read_csv("vehicles_us (2).csv")

df['manufacturer'] = df['model'].apply(lambda x: x.split()[0] if isinstance(x, str) else None)

car_counts_df = df.groupby(['manufacturer', 'model_year']).size().reset_index(name='count')

st.dataframe(df)
st.header('Number of Cars Made per Year by Manufacturer')
his = px.histogram(car_counts_df, x='model_year', color='manufacturer')
st.write(his)

st.header('Histogram of `model_year` by `manufacturer`')
manufacturer_metrics = df.groupby('manufacturer').agg({'days_listed': 'mean', 'price': 'mean'}).reset_index().round(2)
avg_days_listed_mapping = manufacturer_metrics.set_index('manufacturer')['days_listed'].to_dict()
avg_price_mapping = manufacturer_metrics.set_index('manufacturer')['price'].to_dict()
df['avg_days_listed'] = df['manufacturer'].map(avg_days_listed_mapping)
df['mean_price'] = df['manufacturer'].map(avg_price_mapping)

st.dataframe(df)
st.header('Comparison of Average Days Listed and Mean Price by Manufacturer')
scatter = px.scatter(df, x= 'mean_price', y= 'mean_price')
st.write(scatter)

