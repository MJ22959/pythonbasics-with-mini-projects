import json
from difflib import get_close_matches

data = json.load(open("data.json"))
print("///////////////////////////////////////")
print("Welcome to the English Dictionary 2020")
print("///////////////////////////////////////")



def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        print("Does your word mean %s instead" %get_close_matches(word, data.keys())[0])
        decision = input("Enter 'y' for yes or 'n' for no")
        decision = decision.lower()
        if decision == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decision == "n":
            print("your word doesn't exists in dictionary dataset")
        else:
            print("Please enter the correct decision 'y' or 'n'")
    else:
        print("your word doesn't exists in dictionary dataset")

word = input("Enter the word to search in the dictionary")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

