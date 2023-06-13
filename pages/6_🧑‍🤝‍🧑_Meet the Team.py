import streamlit as st
from PIL import Image



#image = Image.open("resources/1.png")
#st.image(image, width=300)


st.subheader("Meet Our Wonderful Team of Talented Individuals")



col1, col2, col3, col4, col5,col6 = st.columns(6,gap="large")

with col1:
    image = Image.open("resources/imgs/tereen.jpg")
    st.image(image,  caption='Tereen Reddy', width=120)
    st.markdown('<font size="1.7"><div style="text-align:right;">Project Lead</div></font>', unsafe_allow_html=True)




with col2:

    image = Image.open("resources/imgs/emmanuel.jpg") 
    st.image(image,caption='Emmanuel Momoh', width=110)
    st.markdown('<font size="1.7"><div style="text-align:right;">Software Eng.</div></font>', unsafe_allow_html=True)



with col3:
   image = Image.open("resources/imgs/khamilla.jpg")
   st.image(image,caption='Khamilla Ebrahim',width=120)
   st.markdown('<font size="1.7"><div style="text-align: right;"> Data Scientist</div></font>', unsafe_allow_html=True)

with col4:
   image = Image.open("resources/imgs/tebogo.jpg")
   st.image(image,caption='Tebogo Mngoma', width=106)
   st.markdown('<font size="1.7"><div style="text-align: right;"> Data Eng.</div></font>', unsafe_allow_html=True)

with col5:
   image = Image.open("resources/imgs/tobias.jpg")
   st.image(image,caption='Tochukwu Tobias', width=120)
   st.markdown('<font size="1.7"><div style="text-align:right;">Data Scientist</div></font>', unsafe_allow_html=True)
   



with col6:
   image = Image.open("resources/imgs/aisha.jpg")
   st.image(image,caption='Aisha Yahaya', width=85)
   st.markdown('<font size="1.7"><div style="text-align:right;">Data Scientist</div></font>', unsafe_allow_html=True)










