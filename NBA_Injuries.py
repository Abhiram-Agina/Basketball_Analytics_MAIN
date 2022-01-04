import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import io

st.title("Basketball INJURY Analysis")
st.write("IL = Injured List")

url = "https://www.prosportstransactions.com/basketball/Search/SearchResults.php?Player=&Team=&BeginDate=&EndDate=&ILChkBx=yes"
df = pd.read_html(url, header=0)
#df[0]

cols = list(df[0].columns)
st.sidebar.header('select a column')
col = st.sidebar.selectbox('Column', cols)

# st.write(len(df))

for i in range(0, 5):
    url_i = "https://www.prosportstransactions.com/basketball/Search/SearchResults.php?Player=&Team=&BeginDate=&EndDate=&ILChkBx=yes&Submit=Search&start={}".format(i*25)
    #st.write(url_i)
    df_i = pd.read_html(url_i, header=0, parse_dates=[0], converters={1:str})
    # #df_i[0]
    #inefficient way to append one DataFrame with contents from another DataFrame
    # df[0] = df[0].append(df_i[0], ignore_index=True)
# df[0]

# a= pd.concat([pd.DataFrame([i], columns=['Date', 'Team', 'Acquired', 'Relinquished', 'Notes']) for i in range(5)], ignore_index=True)
# # pd.concat([pd.DataFrame([i], columns=['A']) for i in range(5)], ignore_index=True)
# a

df[0] = pd.concat([df_i[0] for i in range(1, 1360)], ignore_index=True)
st.write(len(df[0]))
data = df[0]
dataInjury = data[data['Acquired'].isnull()] #include only rows where Acquired is null i.e. exclude rows with Players returning from injuries
st.write(len(dataInjury))
dataInjury

# https://discuss.streamlit.io/t/direct-the-output-of-df-info-to-web-page/14894
df[0].info() #by default, Pandas prints to sys,stdout. To print the data to Streamlit, pupe the data to a buffer, get the buffer content, and display it with st.text
buffer = io.StringIO()
df[0].info(buf=buffer)
s = buffer.getvalue()
st.text(s)

# # split date into year,month,day
# dataInjury['yearInjury'] = pd.DatetimeIndex(dataInjury['Date']).year
# dataInjury['monthInjury'] = pd.DatetimeIndex(dataInjury['Date']).month
# dataInjury['dayInjury'] = pd.DatetimeIndex(dataInjury['Date']).day
# dataInjury

st.header("Exploratory Analysis")

def countPlot(): #Show the counts of observations in each categorical bin using bars.
    fig1 = plt.figure(figsize=(10,4))
    sns.countplot(x=dataInjury[col])
    st.pyplot(fig1)
st.subheader("Frequency Disrtibution of Injuries")
countPlot()








