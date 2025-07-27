import json
import random
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

# === Load model ===
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# === Load intents & responses ===
with open("./JSON_LOUNGE/intent.JSON", "r", encoding="utf-8") as f:
    intents = json.load(f)["intents"]

with open("./JSON_LOUNGE/intent_response.json", "r", encoding="utf-8") as f:
    response_data = json.load(f)["responses"]

# === Prepare patterns ===
intent_patterns = []
intent_tags = []

for intent in intents:
    for pattern in intent["patterns"]:
        intent_patterns.append(pattern)
        intent_tags.append(intent["tag"])

pattern_embeddings = model.encode(intent_patterns)

def get_best_intent(user_input):
    input_embedding = model.encode([user_input])[0]
    similarities = cosine_similarity([input_embedding], pattern_embeddings)[0]
    best_match_index = np.argmax(similarities)
    best_tag = intent_tags[best_match_index]
    best_score = similarities[best_match_index]
    return best_tag, best_score

def get_response_from_tag(tag):
    if tag in response_data:
        return random.choice(response_data[tag])
    return "Hmm... I don't have an answer for that yet, Tsuki~"
\
def generate_response(user_input, threshold=0.55):
    tag, score = get_best_intent(user_input)
    
    if score < threshold:

        fallback_responses = [
            "Hmm... that one's tricky. Can you say it another way, Tsuki?",
            "I didn’t quite catch that~ want to try again?",
            "My circuits are spinning, but I’m not sure what you mean yet~"
        ]
        return random.choice(fallback_responses)

    return get_response_from_tag(tag)




