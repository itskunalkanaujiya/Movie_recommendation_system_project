import streamlit as st
import pickle
import pandas as pd


import os

# Get the folder where app.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load files using absolute path
with open(os.path.join(BASE_DIR, "similarity.pkl"), "rb") as f:
    similarity = pickle.load(f)

with open(os.path.join(BASE_DIR, "movies_dict.pkl"), "rb") as f:
    movies_dict = pickle.load(f)
movies=pd.DataFrame(movies_dict)
st.title("Movie Recommendation System")

option = st.selectbox(
    "Which movie you want ot watch ? ",
    (movies['title'].values),
)

def recommend(movie):
     l=[]
     index=movies[movies['title']==movie].index[0]
     movies_list=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])[1:6]
     for i in movies_list:
        l.append(movies.iloc[i[0]].title)
     return l


if st.button("Recommend"):
    movies_recommended=recommend(option)
    for i in movies_recommended:
        st.write(i)