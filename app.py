import streamlit as st
import pandas as pd
import plotly.express as px

st.header('New and Used Vehicles')
st.write(""" #### Comparing New and Used cars. Use the data below to compare vehicles based on different factors.""")
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


st.header("How does it Compare?")
st.write(""" 
#### Let's see how different factors effect the amount of days posted
""")

first_hist = ['condition', 'transmission','cylinders', 'paint_color','type']

lets_try = st.selectbox('Categories', first_hist)

hist1 = px.histogram( data, x='days_listed', color=lets_try)
hist1.update_layout(title= "<b> Days posted effected by {}</b>".format(lets_try) )



st.plotly_chart(hist1)



def car_age(x):
    if x<4: return '<4'
    elif x>=4 and x<8: return '4-7'
    elif x>=7 and x<11: return '7-11'
    elif x>=11 and x<15: return '11-15'
    elif x>=15 and x<21: return '15-21'
    else: return '>21'

st.write("""
#### Let's use odometer, price, type and condition.
""")

data['years'] = 2020 - data['model_year']

data['car_years'] = data['years'].apply(car_age)

scat_cat = ['odometer', 'type', 'condition', 'price']

scat_cat_list = st.selectbox('On the Market Variables', scat_cat)

scat1 = px.scatter(data, x='days_listed', y=scat_cat_list, color= 'car_years', hover_data=['model_year'])

st.plotly_chart(scat1)

