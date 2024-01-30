# Importing necessary modules
from flask import Flask, jsonify, request
from flask_cors import CORS
from joblib import load
import matplotlib.pyplot as plt

# Loading trained models
presence_classifier = load('category_classifier_bn.joblib')
presence_vect = load('category_vectorizer_bn.joblib')
category_classifier = load('presence_classifier_bn.joblib')
category_vect = load('presence_vectorizer_bn.joblib')

# Initializing Flask app
app = Flask(__name__)
CORS(app)  # Enabling CORS for cross-origin requests

# Define the main route for POST requests
@app.route('/', methods=['POST'])
def main():
    if request.method == 'POST':
        output = []  # List to store the predicted categories
        data = request.get_json().get('tokens')  # Extracting tokens from JSON data

        # Iterating over each token to predict its category
        for token in data:
            result = presence_classifier.predict(presence_vect.transform([token]))
            if result == 'Dark':
                cat = category_classifier.predict(category_vect.transform([token]))
                output.append(cat[0])
            else:
                output.append(result[0])
        
        # Counting the occurrences of each category
        category_count = {}
        for category in output:
            if category in category_count:
                category_count[category] += 1
            else:
                category_count[category] = 1

        # Plotting the pie chart for token distribution
        labels = category_count.keys()
        sizes = category_count.values()
        plt.figure(figsize=(8, 8))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.title('Token Distribution')
        plt.show()

        # Printing and counting tokens classified as 'Dark'
        dark = [data[i] for i in range(len(output)) if output[i] == 'Dark']
        for d in dark:
            print(d)
        print()
        print(len(dark))

        # Creating JSON response
        message = '{ \'result\': ' + str(output) + ' }'
        print(message)

        json = jsonify(message)

        return json

if __name__ == '__main__':
    app.run(threaded=True, debug=True)  # Running the Flask app
