import streamlit as st
import pandas as pd

# CSV file read
df = pd.read_csv("crypto_prices.csv")

st.title("🚀 Cryptocurrency Price Tracker")

st.write("Live Cryptocurrency Data")

st.dataframe(df)

st.success("Data Loaded Successfully!")