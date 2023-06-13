import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import pandas as pd



df_merge = pd.read_csv('resources/data/ratings.csv')
df_2 = pd.read_csv('resources/data/df_merge.csv')


st.title('Exploratory Data Analysis')


st.markdown(""" Exploratory Data Analysis is a very important aspect of machine learning. It refers to the critical process of performing initial investigations on data so as to discover patterns,to spot anomalies,to test hypothesis and to check assumptions with the help of summary statistics and graphical representations.


It is a good practice to understand the data first and try to gather as many insights from it. EDA is all about making sense of data in hand,before getting into proper data investigation.""")

st.markdown("### Insights from Exploratory Data Analysis")


data_source = ['Charts', 'WordClouds']

source_selection = st.selectbox('Select a section of EDA', data_source)
if source_selection == 'Charts':
    st.markdown("""
### `Rating Distribution Amongst Users`
""")
    df1 = df_merge['rating'].value_counts()
    st.bar_chart(df1)


    st.markdown("""

### `Year with most number of movies released` """)
    df2 = df_2['year'].value_counts()
    st.bar_chart(df2)
    
    #sns.countplot(x='year', data=df_merge,order=df_merge['year'].value_counts().iloc[:20].index)


    st.markdown(""" ### `Top 20 Movie Genres ` """)
    df3 = df_2['genres'].value_counts()[:20].sort_values()
    st.bar_chart(df3)


if source_selection == 'WordClouds':

    st.markdown(""" Word Cloud of the most common words: A word cloud is a collection, or cluster, of words depicted in different sizes. The bigger and bolder the word appears, the more often it’s mentioned within a given text and the more important it is.""")


    st.markdown(""" ### `WordCloud for title Cast` """)
    image = Image.open('resources/imgs/title_cast wordcloud.png')
    st.image(image, width=700)


    st.markdown(""" ### `WordCloud for Genres` """)
    image = Image.open('resources/imgs/genre_wordcloud.png')
    st.image(image, width=700)

    st.markdown(""" ### `WordCloud for Plot Keywords` """)
    image = Image.open('resources/imgs/plot keyword word cloud.png')
    st.image(image, width=700)

    st.markdown(""" ### `WordCloud for Titles` """)
    image = Image.open('resources/imgs/title_word cloud.png')
    st.image(image, width=700)

    














