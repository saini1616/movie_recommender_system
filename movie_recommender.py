import streamlit as st
import pickle
import pandas as pd

# Load the necessary data (make sure these files exist in the specified paths)
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Set up the page title and description
st.title('Movie Recommendation System')
st.write('Get recommendations for movies based on your favorite movie.')

# Movie selection dropdown
selected_movie = st.selectbox('Choose a movie', movies['title'].values)


# Define a function to recommend movies without fetching posters
def recommend_movies_only(movie):
    # Find the index of the selected movie
    movie_index = movies[movies['title'] == movie].index[0]

    # Get similarity scores for the selected movie
    distances = similarity[movie_index]

    # Get a list of movie indices sorted by similarity score (most similar first)
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie_names = []

    # Loop through the most similar movies and append their names
    for i in movie_list:
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names


# Create a button to get recommendations
if st.button('Recommend'):
    # Call the recommendation function
    recommended_movie_names = recommend_movies_only(selected_movie)

    # Display the recommended movies
    st.write('Here are the top 5 recommended movies:')
    for movie_name in recommended_movie_names:
        st.write(movie_name)
