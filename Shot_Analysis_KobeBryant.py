# -*- coding: utf-8 -*-
"""Shot Selection - Mamba Mentality.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Bh-ylPp4y1_Jn4HHK7D5ewmT2JK4GfQn

Next Steps:
https://www.kaggle.com/drgilermo/irrational-shot-selection/data

Script Analyzing the Shot-Selection of Kobe Bean Bryant

In this project I aim to analyze the "Hot-Hand Effect" in one of the Greatest Ever. 

Info: ["Hot-Hand Effect" - Social Psychology](http://psychology.iresearchnet.com/social-psychology/decision-making/hot-hand-effect/#:~:text=Hot%20Hand%20Effect%20Definition&text=In%20the%20basketball%2Dshooting%20example,shot%20he%20or%20she%20takes.&text=misses%20in%20basketball%20shooting%2C%20or,losses%20in%20roulette%20betting)
"""

#Importing Packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import streamlit as st

#Load Training Data
totalData = pd.read_csv('DATA/Kobe_CareerShots.csv')
#totalData.head()

st.markdown("[Return to HomePage](https://share.streamlit.io/abhiram-agina/basketball_analytics_main/main/Basketball_Analytics_MAIN.py)")
st.title("Shot Analysis")
st.markdown(
"""
Next Steps:
https://www.kaggle.com/drgilermo/irrational-shot-selection/data

Script Analyzing the Shot-Selection of Kobe Bean Bryant

In this project I aim to analyze the "Hot-Hand Effect" in one of the Greatest Ever. 

Info: ["Hot-Hand Effect" - Social Psychology](http://psychology.iresearchnet.com/social-psychology/decision-making/hot-hand-effect/#:~:text=Hot%20Hand%20Effect%20Definition&text=In%20the%20basketball%2Dshooting%20example,shot%20he%20or%20she%20takes.&text=misses%20in%20basketball%20shooting%2C%20or,losses%20in%20roulette%20betting)
"""
)

st.write("\n**Base Dataset of Kobe's Career:**")
KBData = totalData[totalData['shot_made_flag'].notnull()].reset_index()
st.write("Columns: ", KBData.shape[0], "Rows: ", KBData.shape[1])
st.dataframe(KBData.head())

import datetime
#Cleaning & Organizing Date & Time Datapoints
KBData['game_date_DT'] = pd.to_datetime(KBData['game_date'])
KBData['dayOfWeek'] = KBData['game_date_DT'].dt.dayofweek
KBData['dayOfYear'] = KBData['game_date_DT'].dt.dayofyear

KBData['secondsFromPeriodEnd'] = 60*KBData['minutes_remaining'] + KBData['seconds_remaining']
KBData['secondsFromPeriodStart'] = 60*(11 - KBData['minutes_remaining']) + (60 - KBData['seconds_remaining'])
KBData['secondsFromGameStart'] = (KBData['period'] <= 4).astype(int) * (KBData['period'] - 1) * 12 * 60 + (KBData['period'] > 4).astype(int) * ((KBData['period'] - 4) * 5 * 60 + 3 * 12 + 60) + KBData['secondsFromPeriodStart']

st.write("\n**Isolating Time-Centered Attributes:**")
st.dataframe(KBData.loc[:10,['period', 'minutes_remaining', 'seconds_remaining', 'secondsFromGameStart']])

#Plotting Shot Attempts through Time, through several different binning
plt.rcParams['figure.figsize'] = (16, 16)
plt.rcParams['font.size'] = 16

binsSizes = [24,12,6]

fig = plt.subplots()
for k, binSizeInSeconds in enumerate(binsSizes):
    timeBins = np.arange(0,60*(4*12+3*5),binSizeInSeconds)+0.01
    attemptsAsFunctionOfTime, b = np.histogram(KBData['secondsFromGameStart'], bins=timeBins)     
    
    maxHeight = max(attemptsAsFunctionOfTime) + 30
    barWidth = 0.999*(timeBins[1]-timeBins[0])
    plt.subplot(len(binsSizes),1,k+1)
    plt.bar(timeBins[:-1],attemptsAsFunctionOfTime, align='edge', width=barWidth) 
    plt.title(str(binSizeInSeconds) + ' second time bins')
    plt.vlines(x=[0,12*60,2*12*60,3*12*60,4*12*60,4*12*60+5*60,4*12*60+2*5*60,4*12*60+3*5*60], ymin=0,ymax=maxHeight, colors='r')
    plt.xlim((-20,3200))
    plt.ylim((0,maxHeight))
    plt.ylabel('attempts')
plt.xlabel('time [seconds from start of game]')
st.write("**Analysis of the Career Shot Distribution of KB Over A Game:**")
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()
st.markdown(
"""
Analysis:
* Based on our Visual Representation we can see that Kobe is always entrusted to take the last the shots at the end of the Quarter.
* Kobe is also shown having lower shot totals at the start of the 2nd & 4th, this could be because he is usually benched to start these Quarters.
"""
)

#Plotting the Accuracy of Shots throughout the Shot-Clock(Time)
plt.rcParams['figure.figsize'] = (15, 10)
plt.rcParams['font.size'] = 16

binSizeInSeconds = 24
timeBins = np.arange(0,60*(4*12+3*5),binSizeInSeconds)+0.01
attemptsAsFunctionOfTime,     b = np.histogram(KBData['secondsFromGameStart'], bins=timeBins)     
madeAttemptsAsFunctionOfTime, b = np.histogram(KBData.loc[KBData['shot_made_flag']==1,'secondsFromGameStart'], bins=timeBins)     
attemptsAsFunctionOfTime[attemptsAsFunctionOfTime < 1] = 1
accuracyAsFunctionOfTime = madeAttemptsAsFunctionOfTime.astype(float)/attemptsAsFunctionOfTime
accuracyAsFunctionOfTime[attemptsAsFunctionOfTime <= 50] = 0 # zero accuracy in bins that don't have enough samples

maxHeight = max(attemptsAsFunctionOfTime) + 30
barWidth = 0.999*(timeBins[1]-timeBins[0])

fig2 = plt.subplots()
plt.subplot(2,1,1); plt.bar(timeBins[:-1],attemptsAsFunctionOfTime, align='edge', width=barWidth); 
plt.xlim((-20,3200)); plt.ylim((0,maxHeight)); plt.ylabel('attempts'); plt.title(str(binSizeInSeconds) + ' second time bins')
plt.vlines(x=[0,12*60,2*12*60,3*12*60,4*12*60,4*12*60+5*60,4*12*60+2*5*60,4*12*60+3*5*60], ymin=0,ymax=maxHeight, colors='r')
plt.subplot(2,1,2); plt.bar(timeBins[:-1],accuracyAsFunctionOfTime, align='edge', width=barWidth); 
plt.xlim((-20,3200)); plt.ylabel('accuracy'); plt.xlabel('time [seconds from start of game]')
plt.vlines(x=[0,12*60,2*12*60,3*12*60,4*12*60,4*12*60+5*60,4*12*60+2*5*60,4*12*60+3*5*60], ymin=0.0,ymax=0.7, colors='r')
st.write("**Analysis of Shot Percentage Over A Game:**")
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()
st.markdown(
"""
Analysis:
* Despite the large number of shots that Kobe takes at the end of Quarters, he has a Lower Shot Percentage.
"""
)
