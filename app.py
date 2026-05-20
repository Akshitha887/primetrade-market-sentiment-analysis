import streamlit as st
import pandas as pd

# title
st.title("Trader Sentiment Dashboard")

# load datasets
sentiment = pd.read_csv("fear_greed_index.csv")

trades = pd.read_csv("historical_data.csv")

# convert timestamps
trades['Timestamp'] = pd.to_datetime(
    trades['Timestamp'],
    unit='ms'
)

trades['Date'] = trades['Timestamp'].dt.date

# convert sentiment dates
sentiment['date'] = pd.to_datetime(
    sentiment['date']
)

sentiment['Date'] = sentiment['date'].dt.date

# merge datasets
merged = pd.merge(
    trades,
    sentiment,
    on='Date',
    how='inner'
)

# dashboard output
st.subheader("Merged Dataset")
st.write(merged.head())

# sentiment chart
st.subheader("Market Sentiment Distribution")

st.bar_chart(
    merged['classification'].value_counts()
)