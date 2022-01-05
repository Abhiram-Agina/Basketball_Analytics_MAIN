# Team Analytics

import streamlit as st
import pandas as pd

st.title("Basketball Analytics")

#make an index of services offered
#list metrics, along with importance & limitations
#predict/analyze game outcome per Team metrics


nav = st.sidebar.radio("Navigation",["Summary","Team Analysis","Player Analysis","Marketing Analysis", "Miscellaneous"])

if nav == "Summary":
    st.header("Table of Contents")

    st.markdown(
    '''
    **Team Analysis:**
    \n
    * [Four-Factor Analysis: EFFG, TPP, OReb%, FTR: Offensive & Defensive](https://share.streamlit.io/abhiram-agina/basketball_analytics_main/main/Four_Factor_Analysis.py)
    * Turnovers
    * Fouls
    * Attempts in the Paint
    * [Predicting Wins -- Simulation](https://share.streamlit.io/abhiram-agina/basketball_analytics_main/main/NBA_Game_Simulation.py)
    * [Injury Report](https://share.streamlit.io/abhiram-agina/basketball_analytics_main/main/NBA_Injuries.py)
    '''
    )
    
    #POST-GAME for Rating & Salary
    #use Excel Formulas in Mathletics
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
    
    #NOTE: Each Team plays 300-600 different lineups during the course of a season.\n
    #GOAL: Play good lineups more and bad lineups less.\n
    #www.lineupsuperiority.xls
    #DATA: https://www.basketball-reference.com/playoffs/2006-nba-western-conference-semifinals-mavericks-vs-spurs.html


    st.markdown(
    '''
    \n
    **Marketing & Sales Analysis:**
    \n
    * Player Salary Analysis
    * Ticketing Optimization
    '''
    )
    
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
