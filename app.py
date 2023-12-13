# Import necessary libraries
import streamlit as st
import pickle
import pandas as pd
import requests

def get_poster(movie_title, api_key="d7fb5deb7bf602d49ae830246dd05f56"):
    base_url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": api_key,
        "query": movie_title,
        "language": "en-US",
        "include_adult": "false"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        if data["total_results"] > 0:
            poster_path = data["results"][0]["poster_path"]
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
            return full_path
        else:
            # Return a default image URL or a placeholder image
            return "https://example.com/default_poster_image.jpg"
    except requests.RequestException as e:
        # Return a default image URL or a placeholder image
        return "https://example.com/default_poster_image.jpg"

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


movie_dict = pd.read_pickle('movies_list.pkl')
movie = pd.DataFrame(movie_dict)

similarity = pd.read_pickle('similarity.pkl')

st.title('Movie Recommendation System')

selected_movie_name = st.selectbox('Choose a movie:', movie['title'].values)

if st.button('Recommend'):
    names, posters = recommender(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns([0.2, 0.2, 0.2, 0.2, 0.2])
    with col1:
        st.text(names[0])
        st.image(posters[0])
        st.text(names[5])
        st.image(posters[5])
    with col2:
        st.text(names[1])
        st.image(posters[1])
        st.text(names[6])
        st.image(posters[6])
    with col3:
        st.text(names[2])
        st.image(posters[2])
        st.text(names[7])
        st.image(posters[7])
    with col4:
        st.text(names[3])
        st.image(posters[3])
        st.text(names[8])
        st.image(posters[8])
    with col5:
        st.text(names[4])
        st.image(posters[4])
        st.text(names[9])
        st.image(posters[9])
