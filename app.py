import pickle
import streamlit as st
import requests
import zipfile
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters

# Adjust the size of the first header using CSS styling
header1_style = "<style>h1.header1{font-size: 32px;}</style>"
st.markdown(header1_style, unsafe_allow_html=True)

# Display the first header with the adjusted size
st.markdown("<h1 class='header1'>Movie Recommender System</h1>", unsafe_allow_html=True)



#st.header('Movie Recommender System')

import webbrowser

def open_github_repo():
    url = 'https://github.com/sontush123/content_based_movie_recommender_system.git'
    webbrowser.open_new_tab(url)


col1, col2 = st.columns([3, 1])  # Adjust the column widths as needed
# Adjust the size of the second header using CSS styling
header2_style = "<style>h1.header2{font-size: 24px;}</style>"
st.markdown(header2_style, unsafe_allow_html=True)

# Display the second header with the adjusted size
#st.markdown("<h1 class='header2'>Header 2</h1>", unsafe_allow_html=True)
# Add the header to the first column
#col1.header('Welcome to My App')
col1.markdown("<h1 class='header2'>Welcome to My App</h1>", unsafe_allow_html=True)
# Add the button to the second column
if col2.button('CODE OF THIS PROJECT'):
    #open_github_repo()
    st.markdown('<a href="https://github.com/sontush123/content_based_movie_recommender_system.git" target="_blank">Click here to visit code reposistory Website</a>', unsafe_allow_html=True)



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


movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])





