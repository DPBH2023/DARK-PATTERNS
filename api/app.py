from flask import Flask, jsonify, request
from flask_cors import CORS
from joblib import load
import matplotlib.pyplot as plt

presence_classifier = load('category_classifier_fr.joblib')
presence_vect = load('category_vectorizer_fr.joblib')
category_classifier = load('presence_classifier_fr.joblib')
category_vect = load('presence_vectorizer_fr.joblib')

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def main():
    if request.method == 'POST':
        output = []
        data = request.get_json().get('tokens')

        for token in data:
            result = presence_classifier.predict(presence_vect.transform([token]))
            if result == 'Dark':
                cat = category_classifier.predict(category_vect.transform([token]))
                output.append(cat[0])
            else:
                output.append(result[0])
        category_count = {}
        for category in output:
            if category in category_count:
                category_count[category] += 1
            else:
                category_count[category] = 1

        # Plotting the pie chart
        labels = category_count.keys()
        sizes = category_count.values()
        plt.figure(figsize=(8, 8))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title('Token Distribution')
        plt.show()

        dark = [data[i] for i in range(len(output)) if output[i] == 'Dark']
        for d in dark:
            print(d)
        print()
        print(len(dark))

        message = '{ \'result\': ' + str(output) + ' }'
        print(message)

        json = jsonify(message)

        return json

if __name__ == '__main__':
    app.run(threaded=True, debug=True)