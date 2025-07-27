import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from API_LOUNGE import weather, jokes_api, Date_time
from LOGIC_ENGINE import Transformer


def handle_weather():
    return f"The skies say: {weather.get_weather()}"

def handle_joke():
    return f"Here’s one for you: {jokes_api.get_joke()}"

def handle_datetime():
    time_str, date_str = Date_time.get_date_time()
    return f"It's {time_str} on {date_str}, Tsuki~"

def chat():
    print("Waguri: I’m all ears, Tsuki~ What’s on your mind?\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["bye", "exit", "quit", "leave"]:
            print("Waguri: Hmph. Fine. Come back soon… or I’ll come find you.")
            break

        tag = Transformer.get_best_intent(user_input)[0]


        if tag == "unknown":
            response = Transformer.generate_response(user_input)
        elif tag == "weather":
            response = handle_weather()
        elif tag == "joke":
            response = handle_joke()
        elif tag == "date_time":
            response = handle_datetime()
        else:
            response = Transformer.get_response_from_tag(tag)

        print("Waguri:", response)

# Entry Point
if __name__ == "__main__":
    chat()
