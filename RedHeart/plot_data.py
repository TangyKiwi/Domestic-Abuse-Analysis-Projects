import streamlit as st
import plotly.express as px
import pandas as pd

st.write("""
# Red Heart Campaign Data Visualization
""")

df = pd.read_csv("redheart_data.csv")
st.dataframe(df)

###########################
#           Age           #
###########################
age = df.get("age")
# remove non-numeric values for now, later set under 1 year to 0, remove Unknown
age = [a for a in age if a.isnumeric()]
# convert everything to int
age = list(map(int, age))

s = pd.DataFrame({"Age":age})["Age"].value_counts()
df_age = pd.DataFrame({"Age":s.index, "Count":s.values})
fig = px.bar(df_age, x="Age", y="Count")
st.plotly_chart(fig)

###############################
#           Context           #
###############################
s = df["context"].value_counts()
df_context = pd.DataFrame({"Context":s.index, "Count":s.values})
fig = px.bar(df_context, x="Context", y="Count")
st.plotly_chart(fig)

############################
#           Year           #
############################
year = df.get("year")
year = list(map(int, year))
s = pd.DataFrame({"Year":year})["Year"].value_counts()
df_year = pd.DataFrame({"Year":s.index, "Count":s.values})
fig = px.bar(df_year, x="Year", y="Count")
st.plotly_chart(fig)
