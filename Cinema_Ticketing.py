#!pip install fbprophet #NOTE: fbprophet is compatible with Python 3.8 and below
# installing fbprophet https://anaconda.org/conda-forge/fbprophet

# manage virtual environment in Anaconda https://www.geeksforgeeks.org/set-up-virtual-environment-for-python-using-anaconda/

import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
import streamlit as st

from fbprophet import Prophet
from fbprophet.plot import add_changepoints_to_plot

st.title("Analyzing Ticketing Trends")

ticket = pd.read_csv('C:\\Users\\tulasi.agina\\PYTHON_Programs\\DATA\\CinemaTicketing.csv', usecols = ['total_sales', 'date'])
ticket['date'] = pd.to_datetime(ticket['date'], errors = 'coerce')

#ticket.info() #use the code snippet from NBA Injury Analysis to display .info() output to screen

ticket.describe(include = 'all')

total_sales = ticket.copy()
total_sales.columns = ['y', 'ds']
st.write("**Rows:** ", total_sales.shape[0], "**Columns:** ", total_sales.shape[1])
st.dataframe(total_sales)
#st.write(total_sales)

fig1, ax1 = plt.subplots()
ax1 = sns.lineplot(data = total_sales, x = 'ds', y = 'y')
ax1.set_title('Total Sales over Time')
st.pyplot(fig1)

"""**Analysis:**
- This graph displaying movie sales over time displays a massive spike in April of 2018. This is likely due to the coinciding release of ***Avengers: Infinity War*** which took the world by storm.
"""

#Fitting Data to Model
m1 = Prophet()
m1.fit(total_sales)

future1 = m1.make_future_dataframe(periods=150,freq='D')
forecast1 = m1.predict(future1)
dfm1 = forecast1[['ds', 'yhat_lower', 'yhat_upper', 'yhat']]
#dfm1

fig_fcast1 = m1.plot(forecast1)
st.pyplot(fig_fcast1)

m2 = Prophet(seasonality_mode = 'multiplicative')
m2.fit(total_sales)

future2 = m2.make_future_dataframe(periods = 150, freq = 'D')
forecast2 = m2.predict(future2)
forecast2[['ds', 'yhat_lower', 'yhat_upper', 'yhat']]

fig_fcast2 = m2.plot(forecast2)
st.pyplot(fig_fcast2)

"""Trend Change Points"""

fig_trend1 = m1.plot(forecast1)
a = add_changepoints_to_plot(fig_trend1.gca(), m1, forecast1)
st.pyplot(fig_trend1)

fig_trend2 = m2.plot(forecast2)
a = add_changepoints_to_plot(fig_trend2.gca(), m2, forecast2)
st.pyplot(fig_trend2)

"""Plot Model Components"""

forecast1 = m1.predict(future1)
fig_model1 = m1.plot_components(forecast1)
st.pyplot(fig_model1)
