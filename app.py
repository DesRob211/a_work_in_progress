import streamlit as st
import pandas as pd
import plotly.express as px

st.header('New and Used Vehicles')
st.write(""" #### Comparing New and Used cars.In the data below to compare based on different factors.""")
st.checkbox('Include new cars')

data = pd.read_csv('vehicles_us.csv')

data

car_condition = data['type'].unique()

data_type = st.selectbox('Pick your vehicle type', car_condition)
min_year, max_year = int(data['model_year'].min()), int(data['model_year'].max())


years_invovled = st.slider('Which years did you need?', value=(min_year, max_year), min_value=min_year, max_value=max_year)
years_invovled[0]
years_invovled[1]

real_range = list(range(years_invovled[0], years_invovled[1]+1))

df_select = data[(data['type'] == data_type) & (data['model_year'].isin(list(real_range)))]

df_select



