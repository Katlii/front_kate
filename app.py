import requests
import streamlit as st
import pandas as pd
import boto3
import csv
from io import StringIO

st.set_page_config(page_title='Book Recommender')
st.sidebar.title('Book Recommender')

book_title = st.sidebar.text_input('Enter a book title')
s3 = boto3.client('s3', aws_access_key_id='AKIA2DEBGAQE53LTO5HS', aws_secret_access_key='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')
responseBook = s3.get_object(Bucket='bookrecommender', Key='BX-Books.csv')
responseRatings = s3.get_object(Bucket='ratingsofbooks', Key='BX-Book-Ratings.csv')

csv_data1 = responseBook['Body'].read().decode('cp1251')
csv_data2 = responseRatings['Body'].read().decode('cp1251')
book_title = request.json['book_title']
data1 = StringIO(csv_data1)
data2 = StringIO(csv_data2)

ratings = pd.read_csv(data2, delimiter=';', error_bad_lines=False)
books = pd.read_csv(data1, delimiter=';', error_bad_lines=False)

ratings = ratings.rename(columns={'User-ID':'user_id', 'Book-Rating': 'ratings'})
books = books.rename(columns={'Book-Title':'title', 'Book-Author': 'author', 'Year-Of-Publication': 'year', 'Publisher':'publisher'})

isbnForUser = ratings.groupby('user_id').ISBN.nunique()
average = sum(isbnForUser.to_dict().values())/len(isbnForUser)
x = isbnForUser > int(average)
x = x[x].index.tolist()
ratings = ratings[ratings['user_id'].isin(x)]

dataset = pd.merge(ratings, books, on=['ISBN'])
dataset_lowercase = dataset.apply(lambda x: x.str.lower() if (x.dtype == 'object') else x)
dataset_lowercase = dataset_lowercase.drop_duplicates(['user_id', 'title'])
dataset_lowercase = dataset_lowercase.drop(['Image-URL-S', 'Image-URL-M', 'Image-URL-L'], axis=1)
    
if st.sidebar.button('Get Recommendations'):
    
    response = requests.post('https://book-recommender-kate.herokuapp.com/', json={'book_title': book_title}, allow_redirects =True)
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
    



