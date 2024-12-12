import streamlit as st
import pandas as pd
import plotly.express as px

st.header('New and Used Vehicles')
st.write(""" #### Comparing New and Used cars.In the data below to compare based on different factors.""")
st.checkbox('Include new cars')

data = pd.read_csv('vehicles_us.csv')
cars = data[data['type'].isin(['sedan', 'coupe','convertible', 'hatchback'])]
family = data[data['type'].isin(['SUV', 'wagon', 'van', 'mini-van'])]
trucks = data[data['type'].isin(['pickup', 'truck', 'offroad'])]
party = data[data['type'].isin(['other','bus'])]

fig = px.histogram(data,
                   x='condition',
                   y='model_year',
                   histfunc='count',
                   title='Car Condition vs. Model Year')

event = st.plotly_chart(fig)

