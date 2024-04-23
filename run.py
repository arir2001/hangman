# Your code goes here.
import time

#to slow print text
def machineprint(text, delay = 0.01):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(delay)
    print()

#the instructions to the game
instruct = " these are the instructions"
x = 0

#welcoming the game 
def welcome_message():
    machineprint("""
        Hello there! 
        Welcome to this little game of Hangman! 
            +---+
            |   |
            O   |
           /|\  |
           / \  |
                |
        =========

        Do you wish to see the instructions?
        Please answer 'Y' for yes or 'N' for no.""")

    #to see instructions
    while x != 1:
        INSTRUCTIONS = input('View instructions?:')
        if INSTRUCTIONS == 'Y': 
            print(instruct)
            x == 1
            return
        elif INSTRUCTIONS == 'N':
            x == 1
            return
        else: 
            machineprint("That is an invalid input. Please try again.")


def name():
    machineprint("What is your name?")
    NAME = input('Your name: ')

    while x != 1:
        CORRECT = input("Is this correct? Enter 'Y' or 'N':" )
        if CORRECT == 'Y': 
            print("Yay! Time to play," , NAME, "!")
            x == 1
            return
        elif CORRECT == 'N':
            name()
            x==1
            return
        else: 
            machineprint("That is an invalid input. Please try again.")


def playgame():
    pass



welcome_message()   
name()
playgame()