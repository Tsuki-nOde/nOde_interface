import random
import json
from datetime import datetime

# Load intents and responses
with open("./JSON_LOUNGE/intent.JSON", "r", encoding="utf-8") as f:
    intentions = json.load(f)["intents"]

with open("./JSON_LOUNGE/intent_response.json", "r", encoding="utf-8") as f:
    response = json.load(f)["responses"]

# Function to get current time and date
def get_date_time():
    try:
        now = datetime.now()
        time_str = now.strftime("%I:%M %p")  
        date_str = now.strftime("%d %B %Y") 
        return time_str, date_str
    except Exception as e:
        print("[ERROR] Local time fetch failed:", e)
        return "error time", "error date"

# Function to generate a response based on the intent tag
def get_response(intent_tag):
    if intent_tag == "date_time":
        time_str, date_str = get_date_time()
        template = random.choice(response["date_time"])
        return template.format(time=time_str, date=date_str)
    else:
        for item in response:
            if item["tag"] == intent_tag:
                return random.choice(item["responses"])
    return "I'm not sure how to respond to that just yet~"

# Test the response
if __name__ == "__main__":
    print(get_response("date_time"))


# if __name__ == "__main__":
#     t, d = get_date_time()
#     print(f"[DEBUG] Time: {t}, Date: {d}")
