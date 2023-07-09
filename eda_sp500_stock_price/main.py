import yfinance as yf
import pandas as pd
import streamlit as st
import base64
import matplotlib as plt
import seaborn as sns
import numpy as np

st.title('S&P 500 App')

st.markdown("""
This app retrives the list of the **S&P 500** (from wikipedia)
* **Python libraries:** base64, pandas, streamlit, numpy, matplotlib*
* **Data source:** [wikipedia](https://en.wikipedia.org/).
""")

st.sidebar.header('User input Features')

# Web scraping of S&P 500 data
#
@st.cache
def load_data() :
    url = 'https://en.wikipedia.org/wiki/list_of_S%26P_500_companies'
    html = pd.read_html(url, header = 0)
    df = html[0]
    return df