from numpy.lib.nanfunctions import _nansum_dispatcher
import streamlit as st
import numpy as np
import pandas as pd
from pandas_datareader import data as pdr

st.title("Playing with Streamlit")
st.subheader("Welcome to my site")


img = st.sidebar.image('minions.jpeg')
start_date = st.sidebar.date_input('Select Start Date')
tickers = st.sidebar.text_input('Enter tickers')

imgfile = st.sidebar.file_uploader('upload an image')

tickers = tickers.split()
if imgfile:
    img.image(imgfile)

# file = st.file_uploader('select a file')

end_date = '2021-06-04'

@st.cache(suppress_st_warning=True)
def get_data():
    stock_data = pdr.get_data_yahoo(
        tickers,
        start_date,
        end_date
    )['Adj Close']
    st.write(stock_data)
    return stock_data

stock_data = get_data()
st.write(stock_data)

cols = stock_data.columns.tolist()



checked = st.checkbox('Display Chart')
if checked:
    show_tickers = st.selectbox('Select Stock', cols)
    st.line_chart(stock_data[show_tickers])
    st.line_chart(stock_data[show_tickers].pct_change())

col1, col2, col3 = st.beta_columns(3)
with col1:
    st.line_chart(stock_data[show_tickers])
with col2:
    st.line_chart(stock_data[show_tickers].pct_change())
with col3:
    st.image(imgfile)