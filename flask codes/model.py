import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
import pickle
import nltk
import numpy as np
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
data = pd.read_csv("dataset1.csv")
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
def preprocess_text(text):
    words = nltk.word_tokenize(text)
    words = [word.lower() for word in words if word.isalpha()]  # Remove non-alphabetic characters
    words = [word for word in words if word not in stop_words]  # Remove stopwords
    words = [stemmer.stem(word) for word in words]  # Stemming
    words = [lemmatizer.lemmatize(word) for word in words]  # Lemmatization
    return ' '.join(words)
data['processed_text'] = data['text'].apply(preprocess_text)

# Separate features (text) and labels (pattern category)
X = data['processed_text']
y = data['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
vectorizer = CountVectorizer()
X_train_bow = vectorizer.fit_transform(X_train)
X_test_bow = vectorizer.transform(X_test)
classifier = MultinomialNB()
classifier.fit(X_train_bow, y_train)
y_pred = classifier.predict(X_train_bow)
print(type(y_pred))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
vectorizer=pickle.load(open('vectorizer.pkl',"rb"))
pickle.dump(classifier,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))




    