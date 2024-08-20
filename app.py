import streamlit as st
import plotly_express as px
import pandas as pd
df = pd.read_csv("vehicles_us (2).csv")

st.dataframe(df)
st.header('Number of Cars Made per Year by Manufacturer')
st.write(px.histogram(df, x='model_year', color='manufacturer'))
st.header('Histogram of `model_year` by `manufacturer`')
