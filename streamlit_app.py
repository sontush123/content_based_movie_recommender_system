import pickle
import streamlit as st
import pandas as pd
st.title("Content based Movie Recommender System")
#st.write('Hello world!')
movie_dict = pickle.load(open(r"C:\Users\prasant\Desktop\DATASCIENCE\Projects\content_based_movie_recommender_system\movie-recommender-system-tmdb-dataset-main\movie_list.pkl",'rb'))
similarity_matrix = pickle.load(open(r"C:\Users\prasant\Desktop\DATASCIENCE\Projects\content_based_movie_recommender_system\movie-recommender-system-tmdb-dataset-main\similarity.pkl","rb"))
def similarity(movie):
    recommender_movies = []
    movie_index = movie_dict[movie_dict["title"]==movie].index[0]
    distances = sorted(list(enumerate(similarity_matrix[movie_index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:6]:
        recommender_movies.append(movie_dict.iloc[i[0]].title)
    return recommender_movies


movie_list = movie_dict['title'].values
selected_movie_name = st.selectbox('How would you like to be contracted ?',movie_list)
if st.button("Click To Get Top 5 Similarity"):
    recomendation = similarity(selected_movie_name)
    for i in recomendation:
        st.write(i)