import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
port_stem = PorterStemmer()
vectorization = TfidfVectorizer()

vector_form = pickle.load(open('vector.pkl', 'rb'))
load_model = pickle.load(open('model.pkl', 'rb'))

def stemming(content):
    con=re.sub('[^a-zA-Z]', ' ', content)
    con=con.lower()
    con=con.split()
    con=[port_stem.stem(word) for word in con if not word in stopwords.words('english')]
    con=' '.join(con)
    return con

def fake_news(news):
    news=stemming(news)
    input_data=[news]
    vector_form1=vector_form.transform(input_data)
    prediction = load_model.predict(vector_form1)
    return prediction




if __name__ == '__main__':
    
    st.markdown("""
        ### Welcome to the Fake News Classification App!
        
        This application uses natural language processing techniques to classify news articles as reliable or unreliable. 
        Simply enter the news content in the text area below and click the **Predict** button to get the classification result.
    """)
    
    sentence = st.text_area("Enter your news content here!", "", height=200)
    predict_btt = st.button("Predict")
    
    if predict_btt:
        prediction_class = fake_news(sentence)
        
        if prediction_class == [0]:
            st.success('The news is classified as reliable.')
        elif prediction_class == [1]:
            st.warning('The news is classified as unreliable.')