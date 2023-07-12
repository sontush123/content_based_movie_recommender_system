import pickle
import streamlit as st
import zipfile
st.title("Content based Movie Recommender System")
#st.write('Hello world!')
#movie_dict = pickle.load(open(r"C:\Users\prasant\Desktop\DATASCIENCE\Projects\content_based_movie_recommender_system\movie-recommender-system-tmdb-dataset-main\movie_list.pkl",'rb'))
#similarity_matrix = pickle.load(open(r"C:\Users\prasant\Desktop\DATASCIENCE\Projects\content_based_movie_recommender_system\movie-recommender-system-tmdb-dataset-main\similarity.pkl","rb"))
movies = pickle.load(open("movie_list.pkl",'rb'))
#similarity = pickle.load(open(r"C:\Users\prasant\Desktop\DATASCIENCE\Projects\content_based_movie_recommender_system\similarity.pkl",'rb'))

def load_zipped_pkl(zip_file_path, pkl_file_name):
    with zipfile.ZipFile(zip_file_path, 'r') as zipf:
        with zipf.open(pkl_file_name) as pkl_file:
            data = pickle.load(pkl_file)
    return data

# Provide the file paths
input_zip_file_path = 'similarity_zip.zip'
pkl_file_name = 'data.pkl'

# Load the zipped .pkl file
similarity = load_zipped_pkl(input_zip_file_path, pkl_file_name)




def similarity_fun(movie):
    recommender_movies = []
    movie_index = movies[movies["title"]==movie].index[0]
    distances = sorted(list(enumerate(similarity[movie_index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:6]:
        recommender_movies.append(movies.iloc[i[0]].title)
    return recommender_movies


movie_list = movies['title'].values
selected_movie_name = st.selectbox('How would you like to be contracted ?',movie_list)
if st.button("Click To Get Top 5 Similarity"):
    recomendation = similarity_fun(selected_movie_name)
    for i in recomendation:
        st.write(i)