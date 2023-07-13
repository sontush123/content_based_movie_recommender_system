import pickle
import streamlit as st
import zipfile
#st.title("Content based Movie Recommender System")
#st.write('Hello world!')
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
    open_github_repo()







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
selected_movie_name = st.selectbox('Type or select a movie from the dropdown',movie_list)
if st.button("Click To Get Top 5 Similarity"):
    recomendation = similarity_fun(selected_movie_name)
    for i in recomendation:
        st.write(i)