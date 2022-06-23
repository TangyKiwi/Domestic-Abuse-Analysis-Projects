import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.write("""
# Red Heart Campaign Data Visualization
""")

df = pd.read_csv("https://raw.githubusercontent.com/TangyKiwi/Worldie/master/RedHeart/redheart_data_cleaned.csv")
st.write("Raw Data")
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
age_counts = pd.DataFrame({"Age":s.index, "Count":s.values})
fig = px.bar(age_counts, x="Age", y="Count", title="Age")
st.plotly_chart(fig)
age_groups = pd.cut(age, bins=[-2, -1, 14, 24, 64, 100])
# (-2, -1] (-1, 14] (14, 24] (24, 64] (64, 100]
unique, counts = np.unique(age_groups, return_counts=True)
age_groups = dict(zip(unique, counts))
age_groups = pd.DataFrame({"Age Groups":["Unknown", "Children (0-14)", "Youth (15-24)", "Adults (25-64)", "Seniors (65+)"], "Count":age_groups.values()})
fig = px.bar(age_groups, x="Age Groups", y="Count", title="Age Groups")
st.plotly_chart(fig)
fig = px.pie(age_groups, values="Count", names="Age Groups", title="Age Groups")
st.plotly_chart(fig)

###############################
#           Context           #
###############################
s = df["context"].value_counts()
context_counts = pd.DataFrame({"Context":s.index, "Count":s.values})
fig = px.bar(context_counts, x="Context", y="Count", title="Context")
st.plotly_chart(fig)
fig = px.pie(context_counts, values="Count", names="Context", title="Context")
st.plotly_chart(fig)

#############################
#           Cause           #
#############################
causes = []
for i in range(len(df["cause"])):
    for c in df["cause"][i].split(", "):
        causes.append(c.strip())

s = pd.DataFrame({"Cause":causes})["Cause"].value_counts()
cause_counts = pd.DataFrame({"Cause":s.index, "Count":s.values})
fig = px.bar(cause_counts, x="Cause", y="Count", title="Cause of Death")
st.plotly_chart(fig)

############################
#           Year           #
############################
year = df.get("year")
year = list(map(int, year))
s = pd.DataFrame({"Year":year})["Year"].value_counts()
year_counts = pd.DataFrame({"Year":s.index, "Count":s.values})
fig = px.bar(year_counts, x="Year", y="Count", title="Year")
st.plotly_chart(fig)

######################################
#           Accused Gender           #
######################################
gender = df.get("gender")
s = pd.DataFrame({"Accused Gender":gender})["Accused Gender"].value_counts()
gender_counts = pd.DataFrame({"Accused Gender":s.index, "Count":s.values})
fig = px.bar(gender_counts, x="Accused Gender", y="Count", title="Accused Gender")
st.plotly_chart(fig)
fig = px.pie(gender_counts, values="Count", names="Accused Gender", title="Accused Gender")
st.plotly_chart(fig)

##############################
#           Charge           #
##############################
charge = df.get("charge")
s = pd.DataFrame({"Charge":charge})["Charge"].value_counts()
charge_counts = pd.DataFrame({"Charge":s.index, "Count":s.values})
fig = px.bar(charge_counts, x="Charge", y="Count", title="Charge")
st.plotly_chart(fig)

################################
#           Sentence           #
################################
sentence = df.get("sentence").str.lower()
for i in range(len(sentence)):
    if "sentenced to " in sentence[i]:
        sentence[i] = "sentenced to x years"
    elif "served" in sentence[i]:
        sentence[i] = "served x years"
s = pd.DataFrame({"Sentence":sentence})["Sentence"].value_counts()
sentence_counts = pd.DataFrame({"Sentence":s.index, "Count":s.values})
fig = px.bar(sentence_counts, x="Sentence", y="Count", title="Sentence")
st.plotly_chart(fig)

################################
#           Relation           #
################################
relation = df.get("relation").str.lower()
s = pd.DataFrame({"Relation":relation})["Relation"].value_counts()
relation_counts = pd.DataFrame({"Relation":s.index, "Count":s.values})
fig = px.bar(relation_counts, x="Relation", y="Count", title="Relation")
st.plotly_chart(fig)
