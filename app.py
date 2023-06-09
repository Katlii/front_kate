import requests
import streamlit as st

st.set_page_config(page_title='Book Recommender')
st.sidebar.title('Book Recommender')

book_title = st.sidebar.text_input('Enter a book title')    
if st.sidebar.button('Get Recommendations'):
    
    response = requests.post('https://book-recommender-kate.herokuapp.com/', json={'book_title': book_title}, allow_redirects =True)
    recommendations = response.json()
    
    st.title(f'Best 10 Recommendations for {book_title}:')

    if not recommendations['top_10']:
        st.write('No recommendations found.')
    else:
        df_top_10 = pd.DataFrame(recommendations['top_10'])
        st.write(df_top_10)

    st.title(f'Worst 10 Recommendations for {book_title}:')
    if not recommendations['bottom_10']:
        st.write('No recommendations found.')
    else:
        df_bottom_10 = pd.DataFrame(recommendations['bottom_10'])
        st.write(df_bottom_10)
    



