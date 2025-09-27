import pickle
import streamlit as st
import requests
import joblib
from difflib import get_close_matches


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=fea837cdd3aa3248c23f50be10c535d1&language=en-us".format(movie_id)
    data = requests.get(url=url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = 'https://image.tmdb.org/t/p/w185'+poster_path # poster path has /

    return full_path




# Recieves selected movie title, and use 'get_close_matches' to igonre missing latter in the word & match into 
# corrct words using title list, then reccomnd movie list using similarity metrics
def recommender(movie):
    titles = all_movies['title'].tolist()
    matches = get_close_matches(movie, titles, n=1, cutoff=0.6)

    if not matches:
        print(f"No close match found for '{movie}'")
        return

    best_match = matches[0]
    index = all_movies[all_movies['title'] == best_match].index[0]
    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movie_names = []
    recommended_movie_posters= []

    # print(f"\nRecommendations for: {best_match}\n")
    for i in distances[1:6]:
        # print(all_movies.iloc[i[0]].title)
        movie_id = all_movies.iloc[i[0]]['movie_id']
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(all_movies.iloc[i[0]].title)
    return recommended_movie_names, recommended_movie_posters



# Since we use jupytor (base-annaconda) for pkl files creation, we cannot excute it in another env or python/pandas version
# SO use same env

st.header("Movies Recommendation System")

# Using pickle
# movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
# similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

# Using joblib
all_movies = joblib.load('artifacts/movie_list.pkl')
similarity = joblib.load('artifacts/similarity.pkl')

movie_list = all_movies['title'].values

# Let get thre the selected value into variable
selected_movie = st.selectbox(
    'Type or select a movie to get recommendation',
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommender(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[3])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

