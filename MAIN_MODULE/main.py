import sys
import os



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from API_LOUNGE import weather, jokes_api , Date_time
from LOGIC_ENGINE import nlp



def handle_weather():
    base_response = nlp.get_response("weather")
    weather_report = weather.get_weather()
    return f"{base_response} {weather_report}"

def handle_joke():
    base_response = nlp.get_response("joke")
    joke = jokes_api.get_joke()
    return f"{base_response}, {joke}"
def handle_datetime():
    base_response = nlp.get_response("date_time")
    time_str, date_str = Date_time.get_date_time()
    return base_response.format(time=time_str, date=date_str)

def handle_general(tag):
    return nlp.get_response(tag)


def chat():
    print("あの月さん!! ....... I am online!!!!")

    while True:
        user_input = input("You : ").strip()

        if user_input.lower() in ["later", "bye"]:
            print("Waguri : Leaving already?? また後で!!")    
            break

        tag = nlp.detect_intent(user_input)


        if tag == "weather":
            response = handle_weather()
        elif tag == "joke":
            response = handle_joke()
        elif tag == "date_time":
            response = handle_datetime()
        else:
            response = handle_general(tag)

        print(f"Waguri : {response}")

# Entry Point
if __name__ == "__main__":
    chat()
