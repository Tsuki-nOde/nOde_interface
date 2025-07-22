import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from API_LOUNGE import weather
from LOGIC_ENGINE import nlp


def chat():
    print("あの月さん!! ....... I am online!!!!")

    while True:
        user_input = input("You : ")
    
        if user_input.lower() in ["later", "bye"]:
            print("Waguri : Leaving already  ?? また後で!!")    
            break


        tag = nlp.detect_intent(user_input)

        if tag == "weather":
            base_response = nlp.get_response(tag)
            weather_report = weather.get_weather()
            response = f"{base_response} {weather_report}"

        else:
            response = nlp.get_response(tag)

        print(f"Waguri : {response}")


if __name__ =="__main__":
    chat()