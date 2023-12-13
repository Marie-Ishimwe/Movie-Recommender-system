# Import necessary libraries
import streamlit as st
import pickle
import pandas as pd
import requests

def get_poster(movie_title):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
        movie_title)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommender(movies):
    movies_index = movie[movie['title'] == movies].index[0]
    distances = similarity[movies_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
    recommended_movie = []
    recommended_movie_poster = []

    for item in movie_list:
        movie_title = movie.iloc[item[0]].title
        recommended_movie.append(movie.iloc[item[0]].title)
        recommended_movie_poster.append(get_poster(movie_title))
    return recommended_movie, recommended_movie_poster


movie_dict = pickle.load(open('movies_list.pkl', 'rb'))
movie = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommendation System')

selected_movie_name = st.selectbox('Choose a movie:', movie['title'].values)

if st.button('Recommend'):
    names, posters = recommender(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])