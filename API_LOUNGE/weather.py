import random
import json
import json
import spacy
from spacy.matcher import phrasematcher
import requests

nlp = spacy.load("en_core_web_md")

with open("./JSON_LOUNGE/intent.JSON", "r", encoding="utf-8") as f:
    intentions = json.load(f)["intents"]

with open("./JSON_LOUNGE/intent_response.json", "r", encoding = "utf-8") as f:
    response = json.load(f)["responses"]


def get_weather(city = "Mathura"):
    url = "http://api.weatherapi.com/v1/current.json?key=5c283d5bedba44bf93f170535252207&q=Mathura&aqi=no"
    try:
        response = requests.get(url)
        data = response.json()
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        feels_like = data["current"]["feelslike_c"]
        humidity = data["current"]["humidity"]
        return f"It's currently {temp_c}°C in {city} with {condition}. Feels like {feels_like}°C and humidity is {humidity}%."
    except Exception as e:
        return "Hmm... I couldn't fetch the weather right now. Maybe the skies are shy? 🌧️"
    

def get_response(intent_tag):
    if intent_tag == "weather":
        return get_weather() 
    else:
        for item in response:
            if item["tag"] == intent_tag:
                return random.choice(item["responses"])
    return "I'm not sure how to respond to that just yet~"


