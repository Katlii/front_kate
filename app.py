import requests
import streamlit as st
import pandas as pd

st.set_page_config(page_title='Book Recommender')
st.sidebar.title('Book Recommender')
data = pd.read_csv('https://github.com/Katlii/heroku-book_recommendation/blob/master/BX-Books.csv')
# Create a selection option from the column 'column_name'
selection = st.sidebar.selectbox('Select an option', data['Book-Title'])

# Display the selected option
st.write('You selected:', selection)
#book_title = st.sidebar.text_input('Enter a book title')

if st.sidebar.button('Get Recommendations'):
    response = requests.post('https://book-recommender-kate.herokuapp.com/', json={'book_title': book_title}, allow_redirects =True)
    st.write(response)
    recommendations = response.json()
    
    st.title(f'Top 10 Recommendations for {book_title}:')

    if not recommendations['top_10']:
        st.write('No recommendations found.')
    else:
        df_top_10 = pd.DataFrame(recommendations['top_10'])
        st.write(df_top_10)

    st.title(f'Bottom 10 Recommendations for {book_title}:')
    if not recommendations['bottom_10']:
        st.write('No recommendations found.')
    else:
        df_bottom_10 = pd.DataFrame(recommendations['bottom_10'])
        st.write(df_bottom_10)
    



