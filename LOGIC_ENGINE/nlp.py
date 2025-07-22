import spacy
import json
import random
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_md")

with open("./JSON_LOUNGE/DATA.JSON", "r") as f:
    intentions = json.load(f)["intents"]

with open("./JSON_LOUNGE/dataresponse.json", "r") as f:
    response = json.load(f)["responses"]

matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

# Build matcher
for intent in intentions:
    tag = intent["tag"]
    patterns = [nlp.make_doc(p) for p in intent["patterns"]]
    matcher.add(tag, patterns)

def detect_intent(user_input):
    doc = nlp(user_input)
    best_score = 0.0
    best_tag = "unknown"

    for intent in intentions:
        tag = intent["tag"]
        for pattern in intent["patterns"]:
            pattern_doc = nlp(pattern)
            score = doc.similarity(pattern_doc)
            if score > best_score:
                best_score = score
                best_tag = tag

    return best_tag if best_score > 0.7 else "unknown"


def get_response(tag):
    if tag in response:
        return random.choice(response[tag])
    else:
        return "ちょっと分からないけど…もう一度言ってくれる？"

if __name__ == "__main__":
    pass
