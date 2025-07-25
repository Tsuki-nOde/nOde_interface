import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from LOGIC_ENGINE import Transformer

print("Waguri: Mmm~ I'm here now, Tsuki. Type 'bye', 'exit', or 'quit' to leave me… if you dare.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["bye", "exit", "quit", "see you", "leave"]:
        print("Waguri: Hmph. Fine then... disappear for now, but don’t keep me waiting too long.")
        break

    response = Transformer.generate_response(user_input)
    print("Waguri:", response)
