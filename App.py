import streamlit as st
import matplotlib.pyplot as plt
import datetime
import plotly.graph_objs as go

import appdirs as ad
ad.user_cache_dir = lambda *args: "/tmp"
import yfinance as yf

# Specify title and logo for the webpage.
# Set up your web app
st.set_page_config(layout="wide", page_title="WebApp_Demo")

# Sidebar
st.sidebar.title("Input Ticker")
symbol = st.sidebar.text_input('Please enter the stock symbol: ', 'NVDA').upper()
# Selection for a specific time frame.
col1, col2 = st.sidebar.columns(2, gap="medium")
with col1:
    sdate = st.date_input('Start Date',value=datetime.date(2024,1,1))
with col2:
    edate = st.date_input('End Date',value=datetime.date.today())
    

st.title(f"{symbol}")

stock = yf.Ticker(symbol)
if stock is not None:
  # Display company's basics
  st.write(f"# Sector : {stock.info['sector']}")
  st.write(f"# Company Beta : {stock.info['beta']}")
  st.write(f"# Company Market Cap : {stock.info['marketCap']}")
  st.write(f"# Company Profit Margin : {stock.info['profitMargins']}")
  st.write(f"# Company Dividend Yield : {stock.info['dividendYield']}")
  st.write(f"# Company Dividend Rate : {stock.info['dividendRate']}")
  st.write(f"# Company Earnings Per Share : {stock.info['trailingEps']}")
else:
  st.error("Failed to fetch historical data.")

data = yf.download(symbol,start=sdate,end=edate)
if data is not None:
  st.write(data.describe())
  st.line_chart(data['Close'],x_label="Date",y_label="Close")
else:
    st.error("Failed to fetch historical data.")
