from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

result = sentiment_pipeline("I am not sure wheter I love AI projects or not!")

print(result)