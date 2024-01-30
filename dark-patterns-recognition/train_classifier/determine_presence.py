import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import BernoulliNB
from sklearn.pipeline import Pipeline
from sklearn import metrics
import joblib
from joblib import dump

df1 = pd.read_csv('train_classifier\ormie.csv')
df2 = pd.read_csv('train_classifier\dark_patterns.csv')

df1 = df1[pd.notnull(df1["Pattern String"])]
df1 = df1[df1["classification"] == 0]
df1["classification"] = "Not Dark"
df1.drop_duplicates(subset="Pattern String")

df2 = df2[pd.notnull(df2["Pattern String"])]
df2["classification"] = "Dark"
col = ["Pattern String", "classification"]
df2 = df2[col]

df = pd.concat([df1, df2])
X_train, X_test, y_train, y_test = train_test_split(df['Pattern String'], df["classification"], train_size=0.25)

# Define a pipeline for text classification
text_clf = Pipeline([
    ('vect', CountVectorizer()),  # Convert text to a matrix of token counts
    ('tfidf', TfidfTransformer()),  # Transform a count matrix to a normalized tf-idf representation
    ('clf', BernoulliNB()),  # Bernoulli Naive Bayes classifier
])

# Train the model
text_clf.fit(X_train, y_train)

y_pred = text_clf.predict(X_test)

# Evaluate the accuracy of the model
accuracy = metrics.accuracy_score(y_pred, y_test)
print("Accuracy:", accuracy)

# Save the classifier and vectorizer separately
dump(text_clf.named_steps['clf'], 'presence_classifier_bn.joblib')
dump(text_clf.named_steps['vect'], 'presence_vectorizer_bn.joblib')