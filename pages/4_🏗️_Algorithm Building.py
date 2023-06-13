import streamlit as st
from PIL import Image

st.title("Algorithm Building")


st.markdown("""In building our recommendation system, we applied 2 algorithim, these are:

- **Content_Based Filtering**
- **Collaborative  Filtering**



After Exploratory Data Analysis and Feature engineering.
Our text data was converted into some numeric format which the machine learning models can understand. We achieved this by using **TFIDF( Term Frequency–Inverse Document Frequency)**

### Procedure for Content-Based Algorithim Building

In building our content-based algorithm, we took the following steps

1. Gathered the various properties of our items so that we can convert them into meaningful features (In our case we used _plot keywords_)
2. We additionally create two pandas series objects to help us translate between movie titles and indexes of our dataframe.
3. Converted our textual features into a format which enables us to compute their relative similarities to one another.
   This will allow us to translate our string of _plot keywords_ into numerical vectors(in our case we used TFIDF vectorizer)
4. We computed the similarity between each vector within our matrix. This is done by making use of the `cosine_similarity` function provided to us by `sklearn`

With our content similarity matrix computed, we're now ready to make some recommendations!. To do this we wrote a function that does the following:

- Select an initial movie to generate recommendations from.
- Extract all the similarity values between the initial item and each other item in the similarity matrix.
- Sort the resulting values in descending order.
- Select the top 10 similarity values, and return the corresponding item details to the user. This is now our simple top-N list.
see function implemenatation below """
)


st.code("""
def recommend_movies(title):
    # Find the index of the movie that matches the title
    indx = df_merge[df_merge['title'] == title].index[0]

    # Get the pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[indx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    return df_merge['title'].iloc[movie_indices]
""", language='python')


st.markdown("""### Procedure for Collaborative Filtering Algorithim Building



In building our collabortive filtering algorithm, we took the same steps from 1-4 of our content-based algorithm.
For our next steps we did the following

- Use pandas to construct a utility matrix by using the pivot_table function

- With our utility matrix created, we processed our data in preparation for similarity computation. we achieved this by normalising each user's set of ratings,
filling in Nan values with 0, transposing our matrix for easier indexing, dropping users with no ratings, and storing the matrix in a sparse representation to save memory.
- Computed the similarity matrix using the cosine similarity metric.
- Wrote a function to ouput top 10 recommendations

see function implementation below

""")


st.code("""
def collab_recommendations(user, N=10, k=20):
    # Cold-start problem - no ratings given by the reference user. 
    # With no further user data, we solve this by simply recommending
    # the top-N most popular movies in the item catalog. 
    if user not in user_sim_df.columns:
        return df_collab.groupby('title').mean().sort_values(by='rating',
                                        ascending=False).index[:N].to_list()

    # Gather the k users which are most similar to the reference user 
    sim_users = user_sim_df.sort_values(by=user, ascending=False).index[1:k+1]
    favorite_user_items = [] # <-- List of highest rated items gathered from the k users  
    most_common_favorites = {} # <-- Dictionary of highest rated items in common for the k users

    for i in sim_users:
        # Maximum rating given by the current user to an item 
        max_score = util_matrix_norm.loc[:, i].max()
        # Save the names of items maximally rated by the current user   
        favorite_user_items.append(util_matrix_norm[util_matrix_norm.loc[:, i]==max_score].index.tolist())

    # Loop over each user's favorite items and tally which ones are 
    # most popular overall.
    for item_collection in range(len(favorite_user_items)):
        for item in favorite_user_items[item_collection]:
            if item in most_common_favorites:
                most_common_favorites[item] += 1
            else:
                most_common_favorites[item] = 1
    # Sort the overall most popular items and return the top-N instances
    sorted_list = sorted(most_common_favorites.items(), key=operator.itemgetter(1), reverse=True)[:N]
    top_N = [x[0] for x in sorted_list]
    return top_N
""", language='python')









