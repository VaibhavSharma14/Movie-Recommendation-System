import streamlit as st
import pickle
import pandas as pd
import requests
def fetch_movie(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=31ba5f6e219a92f6bf995d1ae537da3e'.format(movie_id))
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w185/"+data['poster_path']

similarity = pickle.load(open('similarity.pkl','rb'))
movie_dict = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movie_dict)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0] ## this is used to fetch index of movie
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movie = []
    recommended_movie_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        
        recommended_movie.append(movies.iloc[i[0]].title)
        recommended_movie_poster.append(fetch_movie(movie_id))
    return recommended_movie,recommended_movie_poster
    

st.title("Movie Recommander System")

movie = st.selectbox(
    'How would you like to be contacted?',movies['title'].values)


if st.button('Recommend'):
    recommended_movie,recommended_movie_poster = recommend(movie)
        
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
   st.text(recommended_movie[0])
   st.image(recommended_movie_poster[0])

with col2:
   st.text(recommended_movie[1])
   st.image(recommended_movie_poster[1])

with col3:
   st.text(recommended_movie[2])
   st.image(recommended_movie_poster[2])
   
with col4:
   st.text(recommended_movie[3])
   st.image(recommended_movie_poster[3])
   
with col5:  
   st.text(recommended_movie[4])
   st.image(recommended_movie_poster[4])