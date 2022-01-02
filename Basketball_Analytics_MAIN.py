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
    * Four-Factor Analysis: EFFG, TPP, OReb%, FTR: Offensive & Defensive
    * Turnovers
    * Fouls
    * Attempts in the Paint
    * Predicting Wins -- Simulation 
    * Injury Report
    '''
    )
    
    #POST-GAME for Rating & Salary
    #use Excel Formulas in Mathletics
    st.markdown(
    '''
    \n
    **Player Analysis:**
    \n
    * NBA Efficiency Rating
    * John Hollineger's PER
    * BSB Win Scores
    * Adjusted NBA +/- Player Rating 
    * Player Impact Ratings
    * Roland Ratings from 82games.com
    * Standard Deviation of a Lineup
    * Standard Deviation of difference of 2 Lineups
    * Lineup Chemistry
    * Shot Analysis
    * Best vs. Worst Defenders
    * 
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
    * Analyzing of Web Scraped Data
    * Custom Data Analysis
    * AAU Basketball Stats
    * CYBA/AYBA Basketball Stats
    '''
    )