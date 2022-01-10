# Team Analytics

import streamlit as st
import pandas as pd
from PIL import Image

st.title("Homepage: **Basketball Analytics**")

#make an index of services offered
#list metrics, along with importance & limitations
#predict/analyze game outcome per Team metrics

secondSpectrumPic = Image.open("PICS/SportsAnalytics.jpg")
nbaLogoPic = Image.open("PICS/NBALogo.png")
aauLogoPic = Image.open("PICS/AAU.png")
ncaaLogoPic = Image.open("PICS/NCAA.png")
ophsAthleticsPic = Image.open("PICS/OPHSAthletics.png")
abhiramPic = Image.open("PICS/AbhiramAgina.png")

st.sidebar.image(abhiramPic, width = 150)
st.sidebar.markdown(
"""
About Me:
* I am a Junior at Oak Park High School in Oak Park, CA. I absolutely love Basketball & the NBA. I developed this app as a tool and portfolio of my early work in Basketball Analytics.
* [**My Github**](https://github.com/Abhiram-Agina)
* [**My LinkedIn**](https://www.linkedin.com/in/abhiram-agina/)
"""
)

nav = st.sidebar.radio("Navigation",["Summary", "Team Analysis", "Player Analysis", "Marketing/Sales Analysis", "Custom/Web Analysis"])


if nav == "Summary":
    st.image(secondSpectrumPic, caption = "Second Spectrum Analysis on 2014 NBA Finals", width = 700)
    st.markdown(
    """
    ***Data Science + Sports? ***
    * **Our world is changing, and sports are no exception.** 
    * Data Science and Analytics can now be implemented into every facet of a game from **Team** and **Player** Analysis all the way to aspects such as **Ticketing** and **Marketing**.
    * More Info: [How Data Analysis In Sports Is Changing The Game](https://www.forbes.com/sites/forbestechcouncil/2019/01/31/how-data-analysis-in-sports-is-changing-the-game/?sh=3c2f0b883f7b)\n
    
    ***My Goal***
    * This website aims to chart and display my growth into the World of Data Analytics. I begin with my favorite sport, a game I continue to love playing, watching, and learning about. 
    * ***Please Explore and Enjoy :)***\n
    """
    )
    col1, col2, col3, col4 = st.columns(4)
    col1.image(aauLogoPic)
    col2.image(nbaLogoPic)
    col3.image(ncaaLogoPic)
    col4.image(ophsAthleticsPic)
    
    st.markdown(
    """
    ***Inspiration: Ken Jee, Data Professor, Mathletics, MIT ADSP***
    """
    )
    
    
if nav == "Team Analysis":
    st.header("*Team Analysis*")
    st.markdown(
    '''
    * [Four-Factor Analysis: EFFG, TPP, OReb%, FTR: Offensive & Defensive](https://share.streamlit.io/abhiram-agina/basketball_analytics_main/main/Four_Factor_Analysis.py)
    * Turnovers
    * Fouls
    * Attempts in the Paint
    * [Predicting Wins -- Simulation](https://share.streamlit.io/abhiram-agina/basketball_analytics_main/main/NBA_Game_Simulation.py)
    * [Injury Report](https://share.streamlit.io/abhiram-agina/basketball_analytics_main/main/NBA_Injuries.py)
    '''
    )
    
if nav == "Player Analysis":
    st.header("*Player Analysis*")
    st.markdown(
    '''
    \n
    **Player Analysis:**
    \n
    * [NBA Efficiency Rating](https://share.streamlit.io/abhiram-agina/basketball_analytics_main/main/NBA_EfficiencyRating.py)
    * John Hollineger's PER
    * [BSB Win Scores](https://share.streamlit.io/abhiram-agina/basketball_analytics_main/main/BSB_WinScores.py)
    * Adjusted NBA +/- Player Rating 
    * Player Impact Ratings
    * Roland Ratings from 82games.com
    * Standard Deviation of a Lineup
    * Standard Deviation of difference of 2 Lineups
    * Lineup Chemistry
    * [Player Shot Analysis](https://share.streamlit.io/abhiram-agina/basketball_analytics_main/main/Shot_Analysis_KobeBryant.py)
    * [Best vs. Worst Defenders](https://share.streamlit.io/abhiram-agina/basketball_analytics_main/main/Best_Worst_Defenders.py)
    '''
    )
    
if nav == "Marketing/Sales Analysis":
    st.header("*Marketing/Sales Analysis*")
    st.markdown(
    '''
    \n
    **Marketing & Sales Analysis:**
    \n
    * Player Salary Analysis
    * [Ticketing Optimization](https://share.streamlit.io/abhiram-agina/basketball_analytics_main/main/Cinema_Ticketing.py)
    * ***MORE COMING SOON!***
    '''
    )
    
if nav == "Custom/Web Analysis":
    st.header("*Custom/Web Analysis*")
    st.markdown(
    '''
    \n
    **Custom Analysis:**
    \n
    * [Analyzing of Web Scraped Data](https://share.streamlit.io/abhiram-agina/basketball_analytics_main/main/Basketball_Explorer.py)
    * Custom Data Analysis
    * AAU Basketball Stats
    * CYBA/AYBA Basketball Stats 
    '''
    )
