import streamlit as st 
import pandas as pd
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot

import streamlit as st

st.write('# Bike Sharing Dataset')

st.markdown('''
Bike sharing systems are new generation of traditional bike rentals where whole process fro
back has become automatic. Through these systems, user is able to easily rent a bike from a
back at another position. Currently, there are about over 500 bike-sharing programs around 
over 500 thousands bicycles. Today, there exists great interest in these systems due to the
environmental and health issues.
''')

df_hours = pd.read_csv('Dashboard/hour.csv')

df_hours['dteday'] = pd.to_datetime(df_hours['dteday'])
df_hours = df_hours.rename(columns={'weathersit':'weather',
                       'yr':'year',
                       'mnth':'month',
                       'hr':'hour',
                       'hum':'humidity',
                       'cnt':'count'})

cols = ['season' , 'month' , 'hour' , 'holiday' , 'weekday' , 'workingday' , 'weather']
for col in cols:
    df_hours[col] = df_hours[col].astype('category')

df_hours_status_month=df_hours.groupby('month')['count'].mean()
df_hours_status_workingday=df_hours.groupby('workingday')['count'].mean()
df_hours_status_weekday=df_hours.groupby('weekday')['count'].mean()
with st.container():
    with st.container():
        col1, col2, col3 = st.columns(3)
        st.header('Bike Sharing Summary')
        with col1:
            st.header('Bike Sharing Summary Monthly')
            st.dataframe(df_hours_status_month)
        with col2:
            st.header('Bike Sharing Summary workingday')
            st.dataframe(df_hours_status_workingday)
        with col3:
            st.header('Bike Sharing Summary')
            st.dataframe(df_hours_status_weekday)
    with st.container():
        st.header('Bike Sharing Visualisation')
        option = st.selectbox(
            'Choose Graphics Summary BAR CHART?',
            ('Monthly','Weekday','Workingday')
          )

        if option == 'Monthly':
          st.bar_chart(
            df_hours,
            x = 'month',
            y = 'count',
            color = 'month'
          )
        if option == 'Weekday':
          st.bar_chart(
            df_hours,
            x = 'weekday',
            y = 'count',
            color = 'weekday'
          )
        if option == 'Workingday':
          st.bar_chart(
            df_hours,
            x = 'workingday',
            y = 'count',
            color = 'workingday'
          )
    with st.container():
        option = st.selectbox(
            'Choose Graphics Summary Line Chart',
            ('Monthly','Weekday','Workingday','Hour')
          )
        if option == 'Monthly':
          fig, ax = plt.subplots(figsize=(20,5))
          sns.pointplot(data=df_hours, x='month', y='count', hue='weekday', ax=ax)
          st.pyplot(fig)
        if option == 'Weekday':
          fig, ax = plt.subplots(figsize=(20,5))
          sns.pointplot(data=df_hours, x='weekday', y='count', hue='weekday', ax=ax)
          st.pyplot(fig)
        if option == 'Workingday':
          fig, ax = plt.subplots(figsize=(20,5))
          sns.pointplot(data=df_hours, x='workingday', y='count', hue='weekday', ax=ax)
          st.pyplot(fig)
        if option == 'Hour':
          fig, ax = plt.subplots(figsize=(20,5))
          sns.pointplot(data=df_hours, x='hour', y='count', hue='weekday', ax=ax)
          st.pyplot(fig)

    with st.container():
        st.header('Distribusi Data')
        fig, (ax1,ax2) = plt.subplots(ncols=2, figsize=(20,5))
        sns.distplot(df_hours['count'], ax=ax1 , color ='red')
        ax1.set(title='distribusi pengguna')
        qqplot(df_hours['count'], ax=ax2, line='s')
        ax2.set(title='Teori quantiles')
        st.pyplot(fig)

    with st.container():
      st.header('Pengaruh Cuaca Terhadap Sewa')
      fig, (ax1,ax2) = plt.subplots(ncols=2, figsize=(20,5))
      sns.regplot(x=df_hours['temp'], y=df_hours['count'], ax=ax1 ,color='red')
      ax1.set(title="hubungan antara suhu dan pengguna")
      sns.regplot(x=df_hours['humidity'], y=df_hours['count'], ax=ax2)
      ax2.set(title="hubungan antara kembebapan dengan pengguna")
      st.pyplot(fig)


with st.sidebar:
    st.subheader('About')
    st.markdown('This dashboard is made by Just into Data, using **Streamlit**')

st.sidebar.image('https://streamlit.io/images/brand/streamlit-mark-color.png', width=50)