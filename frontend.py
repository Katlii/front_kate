import requests
import streamlit as st
import pandas as pd

st.title('Book Recommendation App')

# Ask user for book title
book_title = st.text_input('Enter book title:', '1984')

if st.button('Get Recommendations'):

    # Send a request to the Flask backend
    res = requests.post('https://book-recommender-kate.herokuapp.com/', json={'title': book_title})

    # Check if the request was successful
    if res.status_code == 200:
        # Convert the JSON response to a Pandas DataFrame
        df_result = pd.DataFrame.from_records(res.json()['top_10'])
        df_worst = pd.DataFrame.from_records(res.json()['bottom_10'])

        # Display the top 10 and bottom 10 results
        st.subheader(f'Top 10 recommendations for "{book_title}"')
        st.write(df_result)

        st.subheader(f'Bottom 10 recommendations for "{book_title}"')
        st.write(df_worst)

    else:
        st.error('Failed to get recommendations')

