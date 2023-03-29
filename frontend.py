import streamlit as st
import requests
import pandas as pd

# Set up the Streamlit app
st.set_page_config(page_title='Book Recommender')

# Define the API endpoint
url = 'https://heroku-book-recommender.herokuapp.com/recommendation'

# Define the function to make the API request and get the recommendations
def get_recommendations(book_title):
    # Set up the request parameters
    params = {'title': book_title}

    # Send the GET request to the API endpoint
    r = requests.get(url, params=params)
    st.write(r)

    # Parse the JSON response and return the results
    if r.status_code == 200:
        results = r.json()
        return results['top_10'], results['bottom_10']
    else:
        st.error('Error getting recommendations from the API.')

# Define the Streamlit app
def app():
    # Set up the app sidebar
    st.sidebar.title('Book Recommender')
    book_title = st.sidebar.text_input('Enter a book title', value='1984')

    # Get the book recommendations from the backend API
    top_10, bottom_10 = [], []
    if st.sidebar.button('Get Recommendations'):
        top_10, bottom_10 = get_recommendations(book_title)
    else:
        top_10, bottom_10 = [], []

    # Display the book recommendations in the app
    st.title(f'Top 10 Recommendations for {book_title}:')
    if top_10:
        df_top_10 = pd.DataFrame(top_10)
        st.write(df_top_10)
    else:
        st.write('No recommendations found.')

    st.title(f'Bottom 10 Recommendations for {book_title}:')
    if bottom_10:
        df_bottom_10 = pd.DataFrame(bottom_10)
        st.write(df_bottom_10)
    else:
        st.write('No recommendations found.')

# Run the Streamlit app
if __name__ == '__main__':
    app()



