import spacy
import json
import random
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_md")

with open("./JSON_LOUNGE/DATA.JSON" , "r") as f:
    intentions = json.load(f)["intents"]

with open("./JSON_LOUNGE/dataresponse.json", "r") as f:
    response = json.load(f)["responses"]





matcher = PhraseMatcher(nlp.vocab, attr = "lower")

intent_map = {}

for intent in intentions:
    tag = intent["tag"]
    patterns = [nlp.make_doc(p) for p  in intent["patterns"]]
    matcher.add(tag, patterns)
    for phrase in intent["patterns"]:
        intent_map[phrase.lower()] = tag


def detect_intent(user_input):
    doc = nlp(user_input)
    matches = matcher(doc)

    matched_span = ""
    match_id = None

    if matches:
        match_id,start,end = matches[0]
        matched_span = doc[start:end].text.lower()


        for phrase, tag in intent_map.items():
            if phrase in matched_span:
                return tag
        
        return nlp.vocab.strings[match_id]
    else:
        return "unknown"

def get_response(tag):
    if tag in response:
        return random.choice(response[tag])
        

