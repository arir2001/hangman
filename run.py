# Your code goes here.
import time

def machineprint(text, delay = 0.1):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(delay)
    print()

instruct = " these are the instructions"



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

    instructions = input('View instructions?:')

    if instructions == 'Y': 
        print(instruct)
    elif instructions == 'N':
        playgame()
    else: 
        machineprint("That is an invalid input. Please try again.")
        instructions

def playgame():
    print('playing game')



welcome_message()