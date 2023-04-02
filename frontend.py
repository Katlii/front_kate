# frontend code (Streamlit example)
import streamlit as st
import requests

st.header("Books rec")

selected_books = st.text_input('book')

if st.button('show rec'):
    # request recommendations from API
    response = requests.get('https://book-recommender-kate.herokuapp.com/', params={'book': selected_books})
    data = response.json()
    
    # display recommendations
    recommendations = data['recommendations']
    st.write(recommendations)

