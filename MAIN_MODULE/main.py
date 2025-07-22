import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



from LOGIC_ENGINE import nlp

def chat():
    print("あの月さん!! ....... I am online!!!!")

    while True:
        user_input = input("You : ")
    
    
        if user_input.lower() in ["later", "bye"]:
            print("Waguri : Leaving already  ?? また後で!!")    
            break

        tag = nlp.detect_intent(user_input)
        response = nlp.get_response(tag)
        print(f"Waguri : {response}")

if __name__ =="__main__":
    chat()