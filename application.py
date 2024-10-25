from flask import Flask, request, jsonify
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

application = Flask(__name__)

def load_model():
    # Load the vectorizer
    with open('count_vectorizer.pkl', 'rb') as file:
        vectorizer = pickle.load(file)
    
    # Load the classifier
    with open('basic_classifier.pkl', 'rb') as file:
        classifier = pickle.load(file)
    
    return vectorizer, classifier

vectorizer, classifier = load_model()

@application.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the text from the POST request
        data = request.get_json()
        text = data['text']

        print(text)
        
        # Transform the text using the loaded vectorizer
        text_vectorized = vectorizer.transform([text])
        
        # Make prediction
        prediction = classifier.predict(text_vectorized)

        print(prediction)
        
        return jsonify({
            'text': text,
            'is_fake_news': prediction[0],  # Use the string label directly
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
        }), 400

if __name__ == '__main__':
    application.run(debug=True)