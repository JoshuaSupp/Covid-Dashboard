
from requests.api import get
from libraries import *
import streamlit as st
import pandas as pd


countries = ['China', 'India', 'Sri Lanka','United States']
data_types = ['cases', 'deaths', 'recoveries']
country = st.sidebar.selectbox('What is your country',countries)
days = st.sidebar.slider('days',min_value=1,max_value=90,step=1)
data_type = st.sidebar.multiselect('Pick data types',data_types)
country_code = {'Sri Lanka': 'lk', 'United States': 'us',
                'China': 'cn', 'India': 'in', 'Italy': 'it'}


#Total_cases

total_cases = get_historic_cases(country,str(days))
total_deaths = get_historic_deaths(country,str(days))
total_recoveries = get_historic_recoveries(country,str(days))


total_df = pd.concat([total_cases,total_deaths,total_recoveries],axis=1).astype(int)




#Daily_cases

daily_cases = get_daily_cases(country,str(days))
daily_deaths = get_daily_deaths(country,str(days))
daily_recoveries = get_daily_recoveries(country,str(days))


daily_df = pd.concat([daily_cases,daily_deaths,daily_recoveries],axis=1).astype(int)





#Yesterday_Cases

yesterday_cases = get_yesterday_cases(country,)
yesterday_deaths = get_yesterday_deaths(country,)
yesterday_recoveries = get_yesterday_recoveries(country,)



st.title('Covid-19 Visualization Dashboard')


st.image(f"https://flagcdn.com/80x60/{country_code[country]}.png")

st.metric('Selected Country', country)
col1,col2,col3 = st.columns(3)
col1.metric('Yesterday Cases',yesterday_cases)
col2.metric('Yesterday Deaths',yesterday_deaths)
col3.metric('Yesterday Recoveries ', yesterday_recoveries)


st.line_chart(daily_df)        #line chart for daily cases
  #line chart for total cases



 

st.video('https://www.youtube.com/watch?v=d7riL6IXi5o')


text_contents = '''Hi Everyone'''
st.download_button('Click Button To Download Text', str(text_contents))


st.image('https://cdn.the-scientist.com/assets/articleNo/69402/aImg/44174/coronavirus-article-s.jpg')
  





