import json
from termcolor import colored
import random 
def hangmen():
    data = json.load(open("words_list.json"))
    word = random.choice(data)
    validletters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''

    while len(word)>0:
        main = ""
            
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + ""
        if main == word:
            print(colored(main,'green'))
            print(colored("Congrats, You Win!",'green'))
            break
        
        print(colored(("Guess the word:",main),'yellow'))
        guess = input()
        guess = guess.lower()

        if guess in validletters:
            guessmade = guessmade + guess
        else:
            print(colored("Enter the valid character from a to z",'red'))
            guess = input()
            guess = guess.lower()
        
        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print(colored("9 turns left",'yellow'))
                print("  --------  ")
            if turns == 8:
                print(colored("8 turns left",'yellow'))
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print(colored("7 turns left",'yellow'))
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print(colored("6 turns left",'yellow'))
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print(colored("5 turns left",'yellow'))
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print(colored("4 turns left",'yellow'))
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print(colored("3 turns left",'yellow'))
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print(colored("2 turns left",'yellow'))
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print(colored("1 turns left",'yellow'))
                print(colored("Last breaths counting, Take care!",'yellow'))
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print(colored("You loose",'red'))
                print(colored("You let a kind man die",'red'))
                print(colored("Right answer is : "+word,'green'))
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break


name = input(colored("Enter your name : ",'green'))
print(colored("Welcome to Hangman 2020 " + name.upper(),'blue'))
print(colored("*************************",'blue'))
print(colored("Try to guess the word in less than 10 attempts",'green'))
hangmen()
print()



