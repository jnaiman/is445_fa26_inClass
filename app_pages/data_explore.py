import streamlit as st

st.set_page_config(page_title="Data", page_icon=":material/table_chart:")
st.sidebar.header("Data")


st.header("Tables about our Data")

import pandas as pd
mobility_url ='https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/mobility.csv'

df = pd.read_csv(mobility_url)

st.text('Showing the dataframe:')
df