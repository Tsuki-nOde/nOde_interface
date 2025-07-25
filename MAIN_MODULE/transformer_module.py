import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



from API_LOUNGE import weather, jokes_api, Date_time
from LOGIC_ENGINE import nlp, Transformer


def handle_weather():
    return f"{nlp.get_response('weather')} {weather.get_weather()}"

def handle_joke():
    return f"{nlp.get_response('joke')}, {jokes_api.get_joke()}"

def handle_datetime():
    base = nlp.get_response("date_time")
    time_str, date_str = Date_time.get_date_time()
    return base.format(time=time_str, date=date_str)

def fallback_transformer(user_input):
    return Transformer.generate_response(user_input)

def chat():
    print("Waguri: I'm listening, Tsuki~ What do you want?\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["bye", "exit", "quit", "leave"]:
            print("Waguri: Hmph. Fine. Come back soon… or I’ll come find you.")
            break

        tag = nlp.detect_intent(user_input)

        # Handle known tags
        if tag == "weather":
            response = handle_weather()
        elif tag == "joke":
            response = handle_joke()
        elif tag == "date_time":
            response = handle_datetime()
        elif tag != "unknown":
            response = nlp.get_response(tag)
        else:
            # Unknown tag: use Transformer
            response = fallback_transformer(user_input)

        print("Waguri:", response)

# Entry Point
if __name__ == "__main__":
    chat()
