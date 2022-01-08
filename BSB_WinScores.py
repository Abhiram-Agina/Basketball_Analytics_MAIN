# -*- coding: utf-8 -*-
"""Mathletics_LinearWeights.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nYftngq8FT7eymTe5NVB2LncpjKy1tkR

NBA Efficiency Rating
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
from PIL import Image

st.markdown("[Return to HomePage](https://share.streamlit.io/abhiram-agina/basketball_analytics_main/main/Basketball_Analytics_MAIN.py)")

image = Image.open('PICS/BSBWinScores.jpg')
st.image(image, caption = "73-9 Warriors")

st.sidebar.header('Select A Season')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950, 2022))))

def load_data(year):
    url = 'https://www.basketball-reference.com/leagues/NBA_' + str(year) + '_per_game.html'
    html = pd.read_html(url, header = 0)
    df = html[0]
    raw = df.drop(df[df.Age == 'Age'].index)
    raw = raw.fillna(0)
    playerstats = raw.drop(['Rk'], axis = 1)
    return playerstats
    
playerstats = load_data(selected_year)
#st.dataframe(playerstats)


#BSB Win Scores = 
playerStatsDF = pd.read_csv('DATA/PlayerStats.csv')
refinedDF = playerStatsDF.drop(columns = ['Birthdate', 'Age', 'Birth_Place', 'Collage', 'Experience', 'Height', 'Pos', 'Weight', 'BMI'])
st.title("Analyzing BSB Win Scores")
#st.write("**NBA Dataset(2014 to 2015) -- Attributes for BSB's Win Scores:**")
#st.dataframe(refinedDF)

#st.write(playerStatsDF['Team'].unique())
teamOptions = refinedDF['Team'].unique()
st.sidebar.header('**Select A Team:**')


st.markdown(
"""
* Berri, Schmidt, and Brook's Win Scores respresent a concise and comprehensive metric for evaluating the base value of a player to their teams success.
* BSB Win Scores uses base offensive and defensive stats calculated across games/seasons
* In this project I aim to analyze and visualize player value within the NBA.
"""
)


st.write("**Selected Team Stats:**")


sorted_unique_team = sorted(playerstats.Tm.unique())
selected_team = st.sidebar.selectbox('Team',sorted_unique_team)

userDF = playerstats[playerstats.Tm == selected_team]
st.dataframe(userDF)

st.markdown(
"""
* This dataset represents the isolated team selected through Year and Team Input
* All Base Metrics are provided, such as PPG, which greatly assist in our Win Score Calculations!
"""
)

userNames = userDF["Player"]
userDF = userDF.drop(columns = ['Player', 'Pos', 'Tm'])

userDF = userDF.astype(float)

st.write("**Calculating Reg-Season Player Win Scores/Shares: **")
userDF["BSB's Win Scores"] = round(userDF['PTS'] + userDF['TRB'] + userDF['STL'] + 0.5 * userDF['AST'] + 0.5 * userDF['BLK'] - userDF['FGA'] - userDF['TOV'] + 
0.5 * (userDF['FTA']) - 0.5 * (userDF['PF']), 2)


col1, col2 = st.columns(2)
fig = plt.subplots()
sns.barplot(x = userNames, y = userDF["BSB's Win Scores"], data = userDF["BSB's Win Scores"])
#st.set_option('deprecation.showPyplotGlobalUse', False)
plt.xticks(rotation = 90)

for index, value in enumerate(userDF["BSB's Win Scores"]):
    plt.text(index - 0.42, value, str(value), fontsize = 'small' ,fontstyle = 'italic', )

st.set_option('deprecation.showPyplotGlobalUse', False)
col1.pyplot()

piePlottedSet = pd.concat([userNames, userDF], axis = 1, join = 'inner')
piePlottedSet = piePlottedSet[piePlottedSet["BSB's Win Scores"] > 0]

color = sns.color_palette('pastel')[0:5]
textprops = {"fontsize": 5}
plt.pie(piePlottedSet["BSB's Win Scores"], labels = piePlottedSet['Player'], colors = color, autopct = '%.000f%%', textprops = textprops)
col2.pyplot()
