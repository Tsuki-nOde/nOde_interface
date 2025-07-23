import json
import random
import requests
from difflib import SequenceMatcher


with open("./JSON_LOUNGE/intent.JSON", "r", encoding="utf-8") as f:
    intentions = json.load(f)["intents"]

with open("./JSON_LOUNGE/intent_response.json", "r", encoding = "utf-8") as f:
    response_data = json.load(f)["responses"]


def similar(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def detect_intent(user_input):
    best_score = 0
    best_intent = None
    for item in intentions:
        for patterns in item["patterns"]:
            score = similar(user_input, patterns)
            if score > best_score:
                best_score = score
                best_intent = item["tag"]
    return best_intent if best_score > 0.6 else None

def get_joke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/jokes/random")
        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']} ... {joke_data['punchline']}"
        else:
            return "I tried to find a joke but the universe isn’t laughing right now."
    except Exception as e:
        return f"Error while fetching joke: {e}"

def generate_response(user_input):
    intent = detect_intent(user_input)
    if intent == "joke":
        prefix = random.choice(response_data[intent])
        joke = get_joke()
        return f"{prefix}\n{joke}"
    else:
        return "Hmm, I didn’t quite get that... try again?"

# Sample test
user_input = input("You: ")
print("Waguri:", generate_response(user_input))
