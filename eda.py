import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import plotly.express as px

def run():
    # membuat title
    st.title('Aplikasi Prediksi Rating Pemain FIFA 2022')
    
    # membuat sub header
    st.subheader('Page ini berisi Exploratory Data Analysis')
    
    # menulis baris
    st.write('By *Rizqi Utama*')
    
    # memasukkan dataset
    df = pd.read_csv('https://raw.githubusercontent.com/FTDS-learning-materials/phase-1/refs/heads/v2.4/w1/P1W1D1PM%20-%20Machine%20Learning%20Problem%20Framing.csv')
    st.dataframe(df)
    
    # memasukkan gambar
    img = Image.open('fifa.png')
    st.image(img, caption='EDA FIFA 2022')    
    
    # menampilkan Histogram of Rating
    st.write('### Histogram of Rating')
    fig = plt.figure(figsize=(15,5))
    sns.histplot(df['Overall'], bins=30, kde=True)
    st.pyplot(fig)
    
    # membuat histrogram berdasarkan input user
    st.write('### Histogram berdasarkan input user')
    fig = plt.figure(figsize=(15, 5))
    opsi = st.selectbox('Pilih Column',('Weight','Height','ShootingTotal',))
    sns.histplot(df[opsi], bins=30, kde=True)
    st.pyplot(fig)

    # membuat plotly plot
    st.write('### Plotly Plot - Rating vs Price')
    fig = px.scatter(df, x='Overall', y='ValueEUR', hover_data=['Name','Age'])
    st.plotly_chart(fig)
if __name__ == '__main__':
    run()