
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn import metrics
from joblib import dump

# Output classification column
output_classification = "Pattern Category"

# Load dataset
df = pd.read_csv('train_classifier\dark_patterns.csv')

# Remove rows with missing values in the "Pattern String" column
df = df.dropna(subset=["Pattern String"])

# Select relevant columns
df = df[[output_classification, "Pattern String"]]

# Create category ID based on the output classification
df["category_id"] = df[output_classification].factorize()[0]

# Create a mapping between category and its ID
category_id_df = df[[output_classification, 'category_id']].drop_duplicates().sort_values('category_id')
category_to_id = dict(category_id_df.values)
id_to_category = dict(category_id_df[['category_id', output_classification]].values)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['Pattern String'], df[output_classification], train_size=.3)

# Define a pipeline for text classification
text_clf = Pipeline([
    ('vect', CountVectorizer()),  # Convert text to a matrix of token counts
    ('tfidf', TfidfTransformer()),  # Transform a count matrix to a normalized tf-idf representation
    ('clf', RandomForestClassifier()),  # Random Forest classifier
])

# Train the model
text_clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = text_clf.predict(X_test)

# Evaluate the accuracy of the model
accuracy = metrics.accuracy_score(y_pred, y_test)
print("Accuracy:", accuracy)

# Save the classifier and vectorizer separately
dump(text_clf.named_steps['clf'], 'category_classifier_bn.joblib')
dump(text_clf.named_steps['vect'], 'category_vectorizer_bn.joblib')
