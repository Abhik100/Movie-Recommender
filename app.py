import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_indx = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_indx]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        movie_id = i[0]
        recommended_movies.append(movies.iloc[movie_id].title)
    return recommended_movies

# Load data
similarity = pickle.load(open('similarity.pkl', 'rb'))
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

# Streamlit app
st.title('Movie Recommender System')

selected_movie = st.selectbox(
    'Select a movie to get recommendations',
    movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    for movie in recommendations:
        st.write(movie)
