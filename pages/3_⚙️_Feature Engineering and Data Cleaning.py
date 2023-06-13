import streamlit as st
from PIL import Image
import pandas as pd

st.title('Feature Engineering And Data Cleaning')

st.subheader("What's Feature Engineering?🤔")

st.markdown("""Feature engineering is the process of selecting, manipulating, and transforming raw data into features that can be used in supervised learning.
Feature Engineering is a very important step in machine learning as it helps to boost model performances with these artificials features created.

When feature engineering activities are done correctly, the resulting dataset is optimal and contains all of the important factors that affect the business problem. As a result of these datasets, the most accurate predictive models and the most useful insights are produced.
### Feature Engineering Techniques Used In Our Model Development

Some feature engineering techniques applied during this project include;""")

st.markdown(""" #### `Creating a dataframe that merges all the features that may be useful`""")

st.markdown("""see implimentation below""")

# Creating a dataframe that merges all the features that may be useful


#df_train = pd.read_csv('resources/data/train.csv')

#df_gscores = pd.read_csv('resources/data/genome_scores.csv')
#df_gtags = pd.read_csv('resources/data/genome_tags.csv')
df_imdb = pd.read_csv('resources/data/imdb_data.csv')
#df_links = pd.read_csv('resources/data/links.csv')
df_movies = pd.read_csv('resources/data/movies_2.csv')
#df_tags = pd.read_csv('resources/data/tags.csv')


## Test data: 
#df_test = pd.read_csv('resources/data/test.csv')

# Create a DataFrame
# Creating a dataframe that merges all the features that may be useful
df_merge = df_imdb[['movieId','title_cast','director', 'plot_keywords']]
df_merge = df_merge.merge(df_movies[['movieId', 'genres', 'title']], on='movieId', how='inner')

#Add colummn for release year
df_merge['year'] = df_merge['title'].str.extract(r"\((\d+)\)", expand=False)

# Display the code block
st.code("""
# Creating a dataframe that merges all the features that may be useful
df_merge = df_imdb[['movieId','title_cast','director', 'plot_keywords']]
df_merge = df_merge.merge(df_movies[['movieId', 'genres', 'title']], on='movieId', how='inner')

#Add colummn for release year
df_merge['year'] = df_merge['title'].str.extract(r"\((\d+)\)", expand=False)
""", language='python')

# Display the DataFrame
st.write(df_merge.head())



st.markdown(""" #### `Convert data types to strings for string handling`""")


df_merge['title_cast'] = df_merge.title_cast.astype(str)
df_merge['plot_keywords'] = df_merge.plot_keywords.astype(str)
df_merge['genres'] = df_merge.genres.astype(str)
df_merge['director'] = df_merge.director.astype(str)


st.code("""
df_merge['title_cast'] = df_merge.title_cast.astype(str)
df_merge['plot_keywords'] = df_merge.plot_keywords.astype(str)
df_merge['genres'] = df_merge.genres.astype(str)
df_merge['director'] = df_merge.director.astype(str)

)
""", language='python')

# Display the DataFrame
st.write(df_merge.head())



st.markdown(""" #### `Removing spaces between director and cast names and convert to lowercase`""")


df_merge['director'] = df_merge['director'].apply(lambda x: "".join(x.lower() for x in x.split()))
df_merge['title_cast'] = df_merge['title_cast'].apply(lambda x: "".join(x.lower() for x in x.split()))


st.code("""
df_merge['director'] = df_merge['director'].apply(lambda x: "".join(x.lower() for x in x.split()))
df_merge['title_cast'] = df_merge['title_cast'].apply(lambda x: "".join(x.lower() for x in x.split()))

)
""", language='python')

# Display the DataFrame
st.write(df_merge.head())




st.markdown(""" #### `Discarding the pipes between the casts full names and extracting only the first three names`""")


df_merge['title_cast'] = df_merge['title_cast'].map(lambda x: x.split('|')[:3])


st.code("""
df_merge['title_cast'] = df_merge['title_cast'].map(lambda x: x.split('|')[:3]))

""", language='python')

# Display the DataFrame
st.write(df_merge.head())




st.markdown(""" #### `Seperating Title Names with comma`""")


df_merge['title_cast'] = [','.join(map(str, l)) for l in df_merge['title_cast']]


st.code("""
df_merge['title_cast'] = [','.join(map(str, l)) for l in df_merge['title_cast']]

""", language='python')

# Display the DataFrame
st.write(df_merge.head())




st.markdown(""" #### `replacing commas with spaces to easily identify casts and plot keywords on wordcloud`""")


df_merge['title_cast'] = df_merge['title_cast'].str.replace(",", " ")


st.code("""
df_merge['title_cast'] = df_merge['title_cast'].str.replace(",", " ")
""", language='python')

# Display the DataFrame
st.write(df_merge.head())



st.markdown(""" #### `Discarding the pipes between the genres and plot_keywords convert to lowercase`""")


df_merge['genres'] = df_merge['genres'].map(lambda x: x.lower().split('|'))
df_merge['genres'] = df_merge['genres'].apply(lambda x: " ".join(x))
df_merge['plot_keywords'] = df_merge['plot_keywords'].map(lambda x: x.lower().split('|'))
df_merge['plot_keywords'] = df_merge['plot_keywords'].apply(lambda x: " ".join(x))


st.code("""
df_merge['title_cast'] = df_merge['title_cast'].str.replace(",", " ")
""", language='python')

# Display the DataFrame
st.write(df_merge.head())


st.markdown(""" #### `Transforming plot Keywords to vectors using TFIDF vectorizer`""")




st.code("""
vect_plot = tfd_vect.fit_transform(df_merge['plot_keywords'])
""", language='python')













