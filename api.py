from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

@app.route('/')
def home():
    return "Sentiment Analysis API"

@app.route('/analyze', methods=["POST"])
def analyze():
    data = request.json
    text = data.get('text')
    result = sentiment_pipeline(text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)