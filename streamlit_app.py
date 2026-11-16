import streamlit as st
import eda
import prediction

st.set_page_config(
    layout='wide',
    initial_sidebar_state='expanded',
    page_title='FIFA 2022 Player Rating Prediction'
)

page = st.sidebar.selectbox('Pilih Halaman', ('EDA','Prediction'))
if page == 'EDA':
    eda.run()
else:
    prediction.run()