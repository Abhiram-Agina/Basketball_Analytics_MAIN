import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns

import streamlit as st #Create Apps of Python Programs + Hosting

st.markdown("[Return to HomePage](https://share.streamlit.io/abhiram-agina/basketball_analytics_main/main/Basketball_Analytics_MAIN.py)")
st.title("NBA Statistics")

data = pd.read_csv("DATA/RegularSeasonDetailedResults_2018_11_10records.csv",sep=",")

if st.checkbox("Show Table"):
    st.table(data)
    
s2018_teams_df = data

def compute_efg(df, winner=True):
  # Effective Field Goals = (Field Goals Made + (3-Pointer Field Goals Made * 0.5)) / Field Goal Attempts
  df['WEFG'] = (df['WFGM'] + 0.5 * df['WFGM3']) / df['WFGA']
  df['LEFG'] = (df['LFGM'] + 0.5 * df['LFGM3']) / df['LFGA']
  return df
  
def compute_tpp(df, winner=True):
    # Turnover Rate = Turnovers / (Field Goal Attempts + 0.44*Free Throw Attempts + Turnovers)
    df['WTPP'] = df['WTO'] / (df['WFGA'] + 0.44 * df['WFTA'] + df['WTO'])
    df['LTPP'] = df['LTO'] / (df['LFGA'] + 0.44 * df['LFTA'] + df['LTO'])
    return df

def compute_orp(df, winner=True):
    # ORP = WOR / (WOR + LDR)
    df['ORP'] = df['WOR'] / (df['WOR'] + df['LDR'])
    df['DRP'] = df['WDR'] / (df['WDR'] + df['LOR'])
    return df

def compute_ftr(df, winner=True):
    df['WFTR'] = df['WFTM'] / df['WFGA']
    return df

st.header("Team Analysis: 4-Factors")

Wteams_efg = compute_efg(s2018_teams_df, winner=True)
Wteams_tpp = compute_tpp(Wteams_efg, winner=True)
Wteams_orp = compute_orp(Wteams_tpp, winner=True)
Wteams_ftr = compute_ftr(Wteams_orp, winner=True)
Wteams_ftr

# DATA IMPORT
label_attr_dict_teams = {"WFGM":"WFGM","WFGA":"WFGA"}

st.sidebar.markdown("**Select the season you want to analyze:** 👇")
seasons = [2011, 2012, 2013, 2014, 2015, 2016, 2017,2018]
start_season, end_season = st.sidebar.select_slider("Select the Season range", options=seasons, value=(2011, 2015))

st.subheader("Compare Teams using Four-Factor Analysis")

attrib = st.selectbox("Which attribute do you want to analyze?", list(label_attr_dict_teams.keys()), key = 'attribute_team')
st.write(attrib)

def barPlot():
    fig = plt.figure(figsize=(10, 4))
    sns.barplot(x = "WTeamID", y = attrib, data=data)
    st.pyplot(fig)
    
barPlot()
