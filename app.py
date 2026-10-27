import streamlit as st
import nltk
import sklearn
import pandas as pd
import pickle
import joblib


st.title('Movie Recommendation System')

with open('movie.pickle','rb') as m:
    movies=pickle.load(m)

similarity=joblib.load('similarity.joblib')

movie_name=movies['title'].values

def recommend(name_movie):
    movies_index=movies[movies['title']==name_movie].index[0]
    recommendation=similarity[movies_index]

    movie_list=sorted(enumerate(recommendation)
                      ,reverse=True,key=lambda x:x[1])[1:6]

    recommendation_movie=[]
    
    for i in movie_list:
       recommendation_movie.append(movies.iloc[i[0]].title)
    return recommendation_movie

name_movie=st.selectbox('Enter the Movie Name', movie_name)

if st.button("Recommend"):
   r=recommend(name_movie)
   st.write("The Recommended Movies are:")

   for i in r:
       st.write(i)
     
