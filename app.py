import streamlit as st
import requests
import pandas as pd

# Set up the base URL for the Flask API
BASE_URL = "https://book-recommender-kate.herokuapp.com/"

# Define a function to make the API request and get recommendations
def get_recommendations(book_title):
    # Define the endpoint and the request body
    endpoint = f"{BASE_URL}/recommend_books"
    body = {"book_title": book_title}
    # Make the POST request to the endpoint
    response = requests.post(endpoint, json=body)
    # Check if the request was successful
    if response.status_code == 200:
        # Get the response data as a dictionary
        data = response.json()
        # Convert the dictionary to pandas dataframes
        top_recs = pd.DataFrame.from_dict(data["top_recommendations"])
        worst_recs = pd.DataFrame.from_dict(data["worst_recommendations"])
        # Return the recommendations
        return top_recs, worst_recs
    else:
        # If the request failed, show an error message
        st.error(f"Request failed with status code {response.status_code}")

# Set up the Streamlit app
st.title("Book Recommendations")
book_title = st.text_input("Enter a book title")
if book_title:
    # Get the recommendations for the book title
    top_recs, worst_recs = get_recommendations(book_title)
    # Display the recommendations
    st.subheader("Top Recommendations")
    st.table(top_recs)
    st.subheader("Worst Recommendations")
    st.table(worst_recs)



