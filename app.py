import requests
import streamlit as st
import pickle
import pandas as pd
import numpy as np
st.title('Movie Recommendation System')

movies_dict = pickle.load(open('movies_data.pkl', 'rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl', 'rb'))




def recommend(movie):

    index=movies[movies['Title']==movie].index[0]
    distances=similarity[index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])
    recommended_movie_names = []


    for i in movie_list[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].Title)
    return recommended_movie_names



movie_list = movies['Title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names= recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])

    with col2:
        st.text(recommended_movie_names[1])


    with col3:
        st.text(recommended_movie_names[2])

    with col4:
        st.text(recommended_movie_names[3])

    with col5:
        st.text(recommended_movie_names[4])

