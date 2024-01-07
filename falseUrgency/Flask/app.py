from flask import Flask, request, render_template
import pickle
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import numpy as np
from nltk.stem import PorterStemmer, WordNetLemmatizer
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

app = Flask(__name__)
model = pickle.load(open('../Models/model.pkl', 'rb'))
vectorizer = pickle.load(open('../Models/vectorizer.pkl', 'rb'))
# Load the vectorizer used during training
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()


def preprocess_text(text):
    words = nltk.word_tokenize(text)
    words = [word.lower() for word in words if word.isalpha()
             ]  # Remove non-alphabetic characters
    # Remove stopwords
    words = [word for word in words if word not in stop_words]
    words = [stemmer.stem(word) for word in words]  # Stemming
    words = [lemmatizer.lemmatize(word) for word in words]  # Lemmatization
    return ' '.join(words)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    if request.method == 'POST':
        input_string = request.form['input_string']
        message = input_string

        processed_message = preprocess_text(message)
        # Vectorize the processed message using the pre-trained vectorizer
        vectorized_message = vectorizer.transform([processed_message])
        # Make predictions using the pre-trained model
        prediction = model.predict(vectorized_message)
        if prediction[0] >= 0.5:
            return render_template('result.html', prediction="Dark Pattern")
        else:
            return render_template('result.html', prediction="normal text")


if __name__ == '__main__':
    app.run(debug=True)
