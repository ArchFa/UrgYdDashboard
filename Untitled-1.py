# %%
# импорт библиотек

import pandas as pd
import streamlit as st
import plotly.graph_objects as go

# %%
st.title("Отчет UrgY")

# %%
countries=['India', 'Australia',
           'Japan', 'America',
           'Russia']
 
values = [4500, 2500, 1053, 500,
          3200]

# %%
fig = go.Figure(
    go.Pie(
    labels = countries,
    values = values,
    hoverinfo = "label+percent",
    textinfo = "value"
))

# %%
st.header("Pie chart")
st.plotly_chart(fig)

# %%



