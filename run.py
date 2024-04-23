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

    x = 0

    #to see instructions
    while x != 1:
        INSTRUCTIONS = input('View instructions?:')
        if INSTRUCTIONS == 'Y': 
            print(instruct)
            name()
            x == 1
            print(x)
        elif INSTRUCTIONS == 'N':
            name()
            x == 1
            print(x)
        else: 
            machineprint("That is an invalid input. Please try again.")
            print(x)

welcome_message()         

def name():
    machineprint("What is your name?")
    NAME = input('Your name: ')
    CORRECT = input("Is this correct? Enter 'Y' or 'N':" )

    x=0

    while x != 1:
        if CORRECT == 'Y': 
            print("Yay! Time to play," , NAME, "!")
            x == 1
        elif CORRECT == 'N':
            name()
            x==1
        else: 
            machineprint("That is an invalid input. Please try again.")
        


 

     


def playgame():
    print('playing game')



