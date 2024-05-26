import speech_recognition as sr
import requests
import os

# News API endpoint and API key
NEWS_API_ENDPOINT = "https://newsapi.org/"
API_KEY = "NEWS API KEY"

def get_news(category):
    params = {
        "country": "us",
        "category": category,
        "apiKey": API_KEY
    }
    response = requests.get(NEWS_API_ENDPOINT, params=params)
    news_articles = response.json()["articles"]
    return news_articles