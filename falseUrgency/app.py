from flask import Flask, request, jsonify, render_template
import pickle
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

with open('bertmodel.pkl', 'rb') as f:
    model = pickle.load(f)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form.get('text')
    if text is not None:
        prediction = int(model.predict(text))

        # Determine the message for the popup
        popup_message = "Dark Pattern Detected!" if prediction == 1 else "No Dark Pattern Detected."

        # Render the result template with the prediction and popup message
        return render_template('result.html', prediction=prediction, popup_message=popup_message)
    else:
        return jsonify({'error': 'Input text not provided.'})

if __name__ == '__main__':
    app.run(debug=True)
