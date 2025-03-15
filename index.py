import random
jokes = ["Why don't skeletons fight each other?They don't have the guts!",
         "I told my wife she was drawing her eyebrows too high.She looked surprised.",
         "You're like a cloud, when you disappear, the day gets a whole lot brighter",
         "I told my friend 10 jokes to make him laugh.Sadly, no pun in ten did.",
         "I have a lot of jokes about unemployed people,but none of them work.",
         "I told my wife she should embrace her mistakes.She gave me a hug.",
         "I wasn't originally going to get a brain transplant,but then I changed my mind.",
]

def request():
    while True:
        userInput = input(" Want a joke?(Yes or no): ")
        if userInput == "yes":
            print(random.choice(jokes))
        elif userInput == "no":
            print('Ok, you must be the joke then')
            break
        else:
            print("I don't even know what you’re saying right now.")

request()



