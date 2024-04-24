# Your code goes here.
import time
import random

HANGMEN = ['''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
     |  |
     O  |
    /|  |
        |
        |
    =========''', '''
    +---+
     |  |
     O  |
    /|\ |
        |
        |
    =========''', '''
    +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========''', '''
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========''']


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
        #no i don't want to see instructions: 
        elif INSTRUCTIONS == 'N':
            x == 1
            return
        #invalid respoonse: 
        else: 
            machineprint("That is an invalid input. Please try again.")

#getting name 
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


def randomWord():
    #Open text file and get random word.
    file = open('words.txt', 'r', encoding='utf-8')
    line = file.read().splitlines()
    rando_word = random.choice(line)
    return rando_word.lower()


chances_gone = 0
letters_spaces_found  = 0
letters_used  = []

def display(letters_spaces_found, letters_used, chances_gone):
    #creating the input lines 
    n = len(randomWord())                       #number of letters in word
    lis_ = [' _ ']*n                            #_ _ _ *n
    string_ = ' '.join([str(i) for i in lis_])  #adding the _ together in one string

    """if letters_spaces_found != 0:
        string"""

    # creating hangman
    m = len(HANGMEN) - chances_gone             #which hangman to print? 
    print(HANGMEN[m])                       
    print('\n', string_, '\n')                  #the _ _ _ _ 
    print("Chances left:", m, '\n')             #numberr of chances left
    print("Letters used:",'\n' , letters_used)  
    return n

display(0, 0, 3)

def display_input():
    while x != 1:
        GUESS = input("Your guess: " )

        if len(GUESS) != n:
            machineprint("Please enter a word with the correct number of letters. ")
        else: 
            machineprint("Your guess is ", GUESS)
            return






display_input()







    





'''
welcome_message()   
name()
playgame()
'''