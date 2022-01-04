import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title("NBA Player Stats Explorer")
st.markdown(
"""
This app performs basic webscraping of B-Ball Player Stats!
* **Python Libraries:** base64, pandas, streamlit
* **Data Source:** [Basketball-reference.com](https: https://www.basketball-reference.com)
"""
)

st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950, 2022))))

def load_data(year):
    url = 'https://www.basketball-reference.com/leagues/NBA_' + str(year) + '_per_game.html'
    st.write(url)
    html = pd.read_html(url, header = 0)
    df = html[0]
    raw = df.drop(df[df.Age == 'Age'].index)
    raw = raw.fillna(0)
    playerstats = raw.drop(['Rk'], axis = 1)
    return playerstats
    
playerstats = load_data(selected_year)


sorted_unique_team = sorted(playerstats.Tm.unique())
selected_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)

unique_pos = ['C', 'PF', 'SF', 'SG', 'PG']
selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos)


df_selected_team = playerstats[(playerstats.Tm.isin(selected_team)) & (playerstats.Pos.isin(selected_pos))]

st.header('Display Player Stats of Selected Team(s)')
st.write('Data Dimension: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' columns')
st.dataframe(df_selected_team)


st.header('Exploratory Data Analysis - Visualized')
st.write("We can now express the B-Ball Data Scraped Online as Colorful/Interactive Graphs!")

unique_attributes = ['PTS', 'AST', 'TRB', 'BLK', 'TOV', 'PF', 'STL']
selected_attribute = st.sidebar.selectbox('Position', list(unique_attributes))

st.set_option('deprecation.showPyplotGlobalUse', False)
sns.distplot(df_selected_team[selected_attribute])
st.pyplot()