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

class GamePlay:
    
    word = randomWord()
    
    correct_letters = [x for x in word] # getting the individual letters

    n = len(word)                       #number of letters in word
    
    print("This is a ", n , "letter word")
    
    lis_ = [' _ ']*n        #list of _ _ _ *n
    
    chances = len(HANGMEN)                      #number of chances
    
    guess = ''

    def __init__(self, random_word):
        # instance attribute
        self.letters_found = []     #the correct letters entered.
        self.letters_guessed= []      #all the letters attempted
        self.chances_left = self.chances -  len(self.letters_guessed)
        #the chances left
        
    def winner():
        print("You win!")
        return

    #prints the _ _ _ and the hangman. 
    def display(self ):
        #creating the input lines 
        string_ = ' '.join([str(i) for i in self.lis_])  #adding the _ together in one string

        # creating hangman
        print(HANGMEN[self.chances_left-1])    #-1 due to indexing in python                   
       
        print('\n', string_, '\n')                  #the _ _ _ _ 
       
        print("Chances left:", self.chances_left, '\n')             #number of chances left
        print("Letters used:",'\n' , self.letters_guessed)      #letters guessed
        print("Letters found:",'\n' , self.letters_found)       #correct letterrs found
        
        
    #guessing a word func
    def display_input_word(self):
        GUESS = input("Your guess: " )
        if len(GUESS) != self.n:
                print("Please enter a word with", self.n ,"letters. ")
                self.display_input_word()
        else: 
                print("Your word guess is ", GUESS)
                self.guess = GUESS
                print('guess strring', self.guess)

    