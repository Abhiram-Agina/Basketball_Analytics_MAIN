# -*- coding: utf-8 -*-
"""Best&Worst_Defenders.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AkJKVjt48s3scQZkfN4kj9265SDOoQo9

***Hypothesis:***

- I believe that the BEST & WORST defenders can be identified by observing each closest defender and isolating the shot/fg percentage against them. 
- In addition, I should evaluate the difficulty and distance of the shots taken as they can gauge whether or not the made shot was a result of brilliant offense or poor defense.
- In order to ensure that this method identifies the strongest defenders it will solely work on players that exceed/have a certain number of shots against them.
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import pylab as P
import streamlit as st
import matplotlib.pyplot as plt
#Allows for the addition of plot within the browser interface
# %matplotlib inline

st.title("*Analyzing Player Defense*")


#Importing Dataset
shot_df = pd.read_csv('DATA/NBAshot_logs.csv')
#st.write(len(shot_df))
st.dataframe(shot_df)
st.write("Columns: ", shot_df.shape[0], " Rows: ", shot_df.shape[1])

#Isolating Defenders
defender_df = pd.concat([shot_df['CLOSEST_DEFENDER_PLAYER_ID'], shot_df['CLOSEST_DEFENDER']], axis = 1, keys = ['PLAYER_ID', 'PLAYER'])
defender_df = defender_df.drop_duplicates()

#Isolating Shooters
shooter_df = pd.concat([shot_df['player_id'], shot_df['player_name']], axis = 1, keys = ['PLAYER_ID', 'PLAYER'])
shooter_df = shooter_df.drop_duplicates()


st.header("Identifying FG% & DFG%")
st.write("**I collect and calculate the shot results of shots taken against defenders. Using this information I can identify whether or not a defender effectively guards.**")
st.write("* Taking the difference between the regular FG% of a player and the FG% against a defender helps us quantify defense!")

#FG%
for index, row in shooter_df.iterrows():
  this_id = row['PLAYER_ID']

  shooter_df.loc[ (shooter_df['PLAYER_ID'] == this_id), 'FGM']\
   = shot_df[ (shot_df['SHOT_RESULT'] == 'made') 
   & (shot_df['player_id'] == this_id)]['player_id'].count()

  shooter_df.loc[ (shooter_df['PLAYER_ID'] == this_id), 'FGA']\
   = shot_df[(shot_df['player_id'] == this_id)]['player_id'].count()

  shooter_df['FG%'] = shooter_df['FGM'] / shooter_df['FGA']

#DFG%
for index, row in defender_df.iterrows():
  this_id = row['PLAYER_ID']

  defender_df.loc[ (defender_df['PLAYER_ID'] == this_id), 'DFGM']\
   = shot_df[ (shot_df['SHOT_RESULT'] == 'made')\
             & (shot_df['CLOSEST_DEFENDER_PLAYER_ID'] == this_id)]['player_id'].count()

  defender_df.loc[ (defender_df['PLAYER_ID'] == this_id), 'DFGA']\
   = shot_df[(shot_df['CLOSEST_DEFENDER_PLAYER_ID'] == this_id)]['player_id'].count()

  defender_df['DFG%'] = defender_df['DFGM'] / defender_df['DFGA']

  #Identifiying Average FG% of offensive players gaurded by this defender
  defender_dict = {}
  for shooter_index, shooter_row in shooter_df.iterrows():
      shooter_id = shooter_row['PLAYER_ID']
      shots_against_player = shot_df[ (shot_df['CLOSEST_DEFENDER_PLAYER_ID'] == this_id)\
                                        & (shot_df['player_id'] == shooter_id)]['player_id'].count()
      if shots_against_player > 0:
          defender_dict[shooter_id] = shots_against_player
    
  ofg = 0.0
  total_shots = defender_df[ (defender_df['PLAYER_ID'] == this_id)]['DFGA']
  for shooter, shots in defender_dict.items():
      ofg += shots/total_shots*shooter_df[ (shooter_df['PLAYER_ID'] == shooter)].iloc[0]['FG%']
    
  defender_df.loc[ (defender_df['PLAYER_ID'] == this_id), 'OFG%'] = ofg


defender_df['diff'] = defender_df['OFG%'] - defender_df['DFG%']
st.dataframe(defender_df)


st.header("Top NBA Defenders per 300 attempts:")
diff_df = defender_df.sort_values(by='diff', axis=0, ascending=False, inplace=False)
st.dataframe(diff_df[ (diff_df['DFGA'] > 300.0)].head(10))

st.header("Worst NBA Defenders per 300 attempts:")
diff_df = defender_df.sort_values(by='diff', axis=0, ascending=True, inplace=False)
st.dataframe(diff_df[ (diff_df['DFGA'] > 100.0)].head(10))

# diff_df[ (diff_df['PLAYER'] == "Leonard, Kawhi")].head(1)
