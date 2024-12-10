import streamlit as st
import pandas as pd

st.header('New and Used Vehicles')
st.write(""" #### Manipulate the data below to compare different filters.""")
the_new = st.checkbox('Include new cars')