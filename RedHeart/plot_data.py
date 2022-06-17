import streamlit as st
import plotly.express as px
import pandas as pd

st.write("""
# Red Heart Campaign Data Visualization
""")

df = pd.read_csv("https://raw.githubusercontent.com/TangyKiwi/Worldie/master/RedHeart/redheart_data_cleaned.csv")
st.dataframe(df)

###########################
#           Age           #
###########################
age = df.get("age")

# remove non-numeric values for now, later set under 1 year to 0, set Unknown to -1
# age = [a for a in age if a.isnumeric()]
# handled in clean_data.py now
age = list(map(int, age))

s = pd.DataFrame({"Age":age})["Age"].value_counts()
df_age = pd.DataFrame({"Age":s.index, "Count":s.values})
fig = px.bar(df_age, x="Age", y="Count", title="Age")
st.plotly_chart(fig)

###############################
#           Context           #
###############################
s = df["context"].value_counts()
df_context = pd.DataFrame({"Context":s.index, "Count":s.values})
fig = px.bar(df_context, x="Context", y="Count", title="Context")
st.plotly_chart(fig)

############################
#           Year           #
############################
year = df.get("year")
year = list(map(int, year))
s = pd.DataFrame({"Year":year})["Year"].value_counts()
df_year = pd.DataFrame({"Year":s.index, "Count":s.values})
fig = px.bar(df_year, x="Year", y="Count", title="Year")
st.plotly_chart(fig)

######################################
#           Accused Gender           #
######################################
gender = df.get("gender")
s = pd.DataFrame({"Accused Gender":gender})["Accused Gender"].value_counts()
df_gender = pd.DataFrame({"Accused Gender":s.index, "Count":s.values})
fig = px.bar(df_gender, x="Accused Gender", y="Count", title="Accused Gender")
st.plotly_chart(fig)
