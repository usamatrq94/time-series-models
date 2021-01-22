import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Understanding Shampoo sales using Sunspots and Daily'
' Minimum Temperature Datesets in Melbourne')
st.header('Sunspot Dataset')
st.markdown('Lets start by understanding Sunspots Dataset')

@st.cache(persist=True, allow_output_mutation=True)
def load_data(fname):
    df = pd.read_csv(fname, index_col=0)
    return df

sunspot = load_data('Sunspots.csv')
sunspot.columns = ['Date', 'Mean']
sunspot['Date'] = pd.to_datetime(sunspot['Date'])
fig = px.line(sunspot, x='Date', y="Mean")
st.write(fig)

st.markdown('Its a typical timeseries dataset showing'
' fluctuations that repeats themselves in cycles.'
' Each cycle has seasonal plus residual parts.')

st.header('Shampoo Dateset')
shampoo = load_data('shampoo.csv')
shampoo['Month'] = shampoo.index
shampoo.columns = ['Month', 'Sales']
fig = px.line(shampoo, x='Month', y='Sales')
st.write(fig)
