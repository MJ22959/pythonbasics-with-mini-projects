import json
import sys
from termcolor import colored
from difflib import get_close_matches

data = json.load(open("data.json"))
print(colored("///////////////////////////////////////",'blue'))
print(colored("Welcome to the English Dictionary 2020",'blue'))
print(colored("///////////////////////////////////////",'blue'))



def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        print(colored("Does your word mean %s instead" %get_close_matches(word, data.keys())[0],'green'))
        decision = input(colored("Enter 'y' for yes or 'n' for no \n",'green'))
        decision = decision.lower()
        if decision == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decision == "n":
            print(colored("your word doesn't exists in dictionary dataset",'green'))
        else:
            print(colored("Please enter the correct decision 'y' or 'n'",'green'))
    else:
        print(colored("your word doesn't exists in dictionary dataset",'green'))

word = input(colored("Enter the word to search in the dictionary \n",'yellow'))
output = translate(word)
if type(output) == list:
    for item in output:
        print(colored(item, 'red'))
else:
    print(colored(output,'red'))

