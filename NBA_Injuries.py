import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.markdown("[Return to HomePage](https://share.streamlit.io/abhiram-agina/basketball_analytics_main/main/Basketball_Analytics_MAIN.py)")

st.title("Basketball INJURY Analysis")
st.write("IL = Injured List")

df = pd.read_csv("DATA/Injury_Updates.csv")

# st.write(len(df))


st.write("Total Columns: ", df.shape[0], "Total Rows: ", df.shape[1])
data = df
dataInjury = data[data['Acquired'].isnull()] #include only rows where Acquired is null i.e. exclude rows with Players returning from injuries
st.write("Injured Columns: ", dataInjury.shape[0] , "Injured Rows: ", dataInjury.shape[1])

dataInjury

# # https://discuss.streamlit.io/t/direct-the-output-of-df-info-to-web-page/14894
# df.info() #by default, Pandas prints to sys,stdout. To print the data to Streamlit, pupe the data to a buffer, get the buffer content, and display it with st.text
# buffer = io.StringIO()
# df.info(buf=buffer)
# s = buffer.getvalue()
# st.text(s)

# split date into year,month,day
dataInjury['yearInjury'] = pd.DatetimeIndex(dataInjury['Date']).year
dataInjury['monthInjury'] = pd.DatetimeIndex(dataInjury['Date']).month
dataInjury.drop("Date")
#dataInjury['dayInjury'] = pd.DatetimeIndex(dataInjury['Date']).day
# dataInjury

cols = list(dataInjury.columns)
st.sidebar.header('select a column')
col = st.sidebar.selectbox('Column', cols)

st.header("Exploratory Analysis")

def countPlot(): #Show the counts of observations in each categorical bin using bars.
    fig1 = plt.figure(figsize=(10,4))
    sns.countplot(x=dataInjury[col])
    plt.xticks(rotation=90)
    st.pyplot(fig1)
st.subheader("Frequency Disrtibution of Injuries")
countPlot()








