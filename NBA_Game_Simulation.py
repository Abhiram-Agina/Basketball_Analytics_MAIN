import pandas as pd
import random as rnd
import matplotlib.pyplot as plt
import streamlit as st

st.title("Predicting Game Results")
st.title("*Warriors vs. Rockets*")

gamesDF = pd.read_csv('C:\\Users\\Robo1753\\Desktop\\Streamlit_Programs\\SPORTS ANALYTICS\\DATA\\nba.games.stats.csv')
st.dataframe(gamesDF) #We want Team, Date, TeamsPoints, OpponentPoints

#Create 2 DataFrames
gswDF = gamesDF[gamesDF.Team == 'GSW']
houDF = gamesDF[gamesDF.Team == 'HOU']

#Isolating 2017-2018 NBA Regular Season
gswDF.Date = gswDF.Date.apply(lambda x: pd.to_datetime(x, format = '%Y-%m-%d', errors = 'ignore'))
gswDF = gswDF[gswDF['Date'] > pd.to_datetime('20171001', format = '%Y%m%d', errors = 'ignore')]

houDF.Date = houDF.Date.apply(lambda x: pd.to_datetime(x, format = '%Y-%m-%d', errors = 'ignore'))
houDF = houDF[houDF['Date'] > pd.to_datetime('20171001', format = '%Y%m%d', errors = 'ignore')]

fig1, ax1 = plt.subplots()
#gswDF.TeamPoints.hist(color = 'gold')
#houDF.TeamPoints.hist(color = 'maroon')
ax1.hist(gswDF.TeamPoints, bins = 20, color = 'gold', label = "GSW" )
ax1.hist(houDF.TeamPoints, bins = 20, color = 'maroon', label = "HOU")
ax1.set_xlabel("Points Scored")
ax1.set_ylabel("Frequency")
ax1.set_title("Breakdown of Team Scores")
ax1.legend()
st.pyplot(fig1)


fig2, ax2 = plt.subplots()
#gswDF.OpponentPoints.hist(color = 'gold')
#houDF.OpponentPoints.hist(color = 'maroon')
ax2.hist(gswDF.OpponentPoints, bins = 20, color = 'gold', label = "GSW" )
ax2.hist(houDF.OpponentPoints, bins = 20, color = 'maroon', label = "HOU")
ax2.set_xlabel("Points Scored")
ax2.set_ylabel("Frequency")
ax2.set_title("Breakdown of Opponent Scores")
ax2.legend()
st.pyplot(fig2)

# """2 Metric Predictions - MEAN & STANDARD DEVIATION"""

gswMeanPts = gswDF.TeamPoints.mean()
houMeanPts = houDF.TeamPoints.mean()
gswSDPts = gswDF.TeamPoints.std()
houSDPts = houDF.TeamPoints.std()

gswMeanOpp = gswDF.OpponentPoints.mean()
houMeanOpp = houDF.OpponentPoints.mean()
gswSDOpp = gswDF.OpponentPoints.std()
houSDOpp = houDF.OpponentPoints.std()

st.header("Exploratory Analytics of Both Teams")
st.write('GSW TeamPoints Mean:', gswMeanPts)
st.write('GSW TeamPoints SD:', gswSDPts)
st.write('HOU TeamPoints Mean:', houMeanPts)
st.write('HOU TeamPoints SD:', houSDPts)

st.write('GSW OpponentPoints Mean:', gswMeanOpp)
st.write('GSW OpponentPoints SD:', gswSDOpp)
st.write('HOU OpponentPoints Mean:', houMeanOpp)
st.write('HOU OpponentPoints SD:', houSDOpp)


st.header("Predicting Games Scores & Results")
st.write("I utilize a normal/gaussian distribution in order to gauge a likely scoring outcome for each team.\n")
rnd.gauss(gswMeanPts, gswSDPts)


st.write("**Breakdown of Game Results per 10000 Simulated Games**")
def gameSim():
  GSWScore = (rnd.gauss(gswMeanPts, gswSDPts) + rnd.gauss(gswMeanOpp, gswSDOpp))/2
  HOUScore = (rnd.gauss(houMeanPts, houSDPts) + rnd.gauss(houMeanOpp, houSDOpp))/2

  if int(round(GSWScore)) > int(round(HOUScore)):
    return 1
  elif int(round(GSWScore)) < int(round(HOUScore)):
    return -1
  else:
    return 0

def gamesSim(ns):
  
  gamesout = []
  team1win = 0
  team2win = 0
  tie = 0

  for i in range(ns):
    gm = gameSim()
    gamesout.append(gm)
    if gm == 1:
      team1win += 1
    elif gm == -1:
      team2win += 1
    else:
      tie += 1

  st.write('* GSW Win:', round((team1win / (team1win + team2win + tie) * 100), 2), '%')
  st.write('* HOU Win:', round((team2win / (team1win + team2win + tie) * 100), 2), '%')
  st.write('* TIE:', round((tie / (team1win + team2win + tie) * 100), 2), '%')
  return 0 #gamesout

gamesSim(10000)