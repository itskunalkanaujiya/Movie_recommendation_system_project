import streamlit as st
import pickle
import pandas as pd

import gdown
import os

# Check if file already exists
if not os.path.exists("similarity.pkl"):
    url = "https://drive.google.com/file/d/10fy_GDXohKsBK5lvnHrFktWf3CixsR4G/view?usp=drive_link"
    gdown.download(url, "similarity.pkl", quiet=False)



movies_dict=pickle.load(open("movies_dict",'rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
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