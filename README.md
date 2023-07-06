# NLPFakeNews
The Fake News Classification Application is a project that aims to identify fake news using natural language processing techniques. The application achieves an impressive accuracy level of 96.4%. To train the model, I utilized a dataset consisting of both fake and real news articles. 

To preprocess the text data, I employed stemming techniques provided by the NLTK library. Stemming helps to reduce words to their root form, which can improve the accuracy of the classification model. 

Next, I converted the preprocessed text data into a numerical representation using the TfidfVectorizer library from sklearn. This process is known as vectorization and it assigns numerical values to words based on their frequency and importance in the dataset.

Once the training and vectorization steps were complete, I incorporated TensorFlow and Keras into the Fake News Classification Application to build and train a deep learning model. I then used a python front-end framework called Streamlit to create the UI for the application. Streamlit allows users to interact with the model, input news articles, and receive predictions on whether the articles are real or fake.

By following these steps, I successfully developed a Fake News Classification Application that leverages natural language processing, stemming, vectorization, and a user interface to accurately detect fake news articles.

