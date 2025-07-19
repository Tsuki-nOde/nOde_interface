import json
import random

# TAKING INPUT FOR GREETINGS

with open ("Greetings.json" , "r") as f:
    data = json.load(f)

user_input = input("You : ").lower()

if user_input in data["greetings"]:
    response = random.choice(data["greetings"][user_input])
    print("Waguri:", response)
else:
    print("Waguri: Hmm? I don't have a reply for that yet, Tsuki~")
    
# TAKING INPUT FOR NAME 

with open("name,age.json" ,"r") as file:
    data = json.load(file)


user_name = input("Waguri: And your name is...? Just asking: ")
response = random.choice(data["name_input"])
print("Waguri: ",response,user_name)


#TAKING THE INPUT OF AGE 
try:
    user_age  = int(input("Waguri : Enter your age BOY!! or girl whatever i ain't asking gender rn hehe : "))

    if user_age < 18:
        response = random.choice(data["under_18"])
        print(response)
    else:
        response = random.choice(data["adult_18_plus"])
        print(response)

except ValueError:
        print("Siirrr I dont know that please use number Tsuki, sorry i mean my fucking master is still making me AARIGATO!!")