import streamlit as st
import json
#from streamlit_lottie import st_lottie
from PIL import Image


st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎥",
)




#image = Image.open('resources/new_sent.png')
#st.image(image, width=600,use_column_width=True)


st.title('Movie Recommender System')


st.markdown("""A movie recommendation system is a fancy way to describe a process that tries to predict your preferred items based on your or people similar to you.
In layman’s terms, we can say that a Recommendation System is a tool designed to predict/filter the items as per the user’s behavior.


""")

st.subheader('Why exactly do we need Recommendation Systems?')

st.markdown("""The primary goal of movie recommendation systems is to filter and predict only those movies that a corresponding user is most likely to want to watch. The ML algorithms for these recommendation systems use the data about this user from the system’s database.
This data is used to predict the future behavior of the user concerned based on the information from the past.


""")

st.subheader('Filtration Strategies for Movie Recommendation Systems')


st.markdown("""Movie recommendation systems use a set of different filtration strategies and algorithms to help users find the most relevant films.
The most popular categories of the ML algorithms used for movie recommendations include **content-based filtering** and **collaborative filtering systems**.


""")

st.markdown(""" ## `Content-based filtering:`

A filtration strategy for movie recommendation systems, which uses the data provided about the items (movies). This data plays a crucial role here and is extracted from only one user. An ML algorithm used for this strategy recommends motion pictures that are similar to the user’s preferences in the past.
Therefore, the similarity in **content-based filtering** is generated by the data about the past film selections and likes by only one user.

How does it work? The recommendation system analyzes the past preferences of the user concerned, and then it uses this information to try to find similar movies.
This information is available in the database (e.g., lead actors, director, genre, etc.). After that, the system provides movie recommendations for the user.
That said, the core element in content-based filtering is only the data of only one user that is used to make predictions.

""")



st.markdown(""" ## `Collaborative filtering:`

As the name suggests, this filtering strategy is based on the combination of the relevant user’s and other users’ behaviors. The system compares and contrasts these behaviors for the most optimal results. It’s a collaboration of the multiple users’ film preferences and behaviors.

What’s the mechanism behind this strategy? The core element in this movie recommendation system and the ML algorithm it’s built on is the history of all users in the database. Basically, collaborative filtering is based on the interaction of all users in the system with the items (movies).
Thus, every user impacts the final outcome of this ML-based recommendation system, while content-based filtering depends strictly on the data from one user for its modeling.

Collaborative filtering algorithms are divided into two categories:

- **User-based collaborative filtering**: The idea is to look for similar patterns in movie preferences in the target user and other users in the database.
- **Item-based collaborative filtering**: The basic concept here is to look for similar items (movies) that target users rate or interact with.
The modern approach to the movie recommendation systems implies a mix of both strategies for the most gradual and explicit results.
""")
image = Image.open('resources/imgs/content-based_vs_collaborative.png')
st.image(image, width=600,use_column_width=True)
