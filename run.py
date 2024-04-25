# Your code goes here.
import time
import random
import os 
import sys

#hangmen pic aart
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
    /|\\ |
        |
        |
    =========''', '''
    +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========''', '''
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========''']

#celebration message
CELEBRATE = """
    ＼(＾O＾)／

    (,,>ヮ<,,)!             (づ๑•ᴗ•๑)づ♡
    
    ദ്ദി ˉ͈̀꒳ˉ͈́ )✧         ᵔ ᵕ ᵔ 

                        ( • ̀ω•́ )✧
    (,,>﹏<,,)                           °❀⋆.ೃ࿔*:･


    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡈⠛⢉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⢿⣿⣿⣿⣿⣿⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣿⡏⠀⢸⣿⣿⣿⣿⡇⢸⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⣿⠁⠀⢸⣿⣿⣿⣿⠁⠀⠙⠻⢿⣿⣶⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠛⠋⠀⠀⠸⣿⣿⣿⡏⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⠙⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣦⠈⢿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡟⠀⠀⠻⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⠟⠁⠀⠀⠀⠘⢿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢾⣿⠟⠁⠀⠀⠀⠀⠀⠀⠈⢻⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀

    you are a free man......
                for now......
                            play again?
    """

#loser message
LOSER = """

    $$______ ____$$$___ ___$$$$$__ __$$$$$$$_ __$$$$$$__ ____$$_
    $$______ ___$$_$$__ __$$___$$_ __$$______ __$$___$$_ ____$$_
    $$______ __$$___$$_ ___$$$____ __$$$$$___ __$$___$$_ ____$$_
    $$______ __$$___$$_ _____$$$__ __$$______ __$$$$$$__ ____$$_
    $$____$_ ___$$_$$__ __$$___$$_ __$$______ __$$___$$_ _______
    $$$$$$$_ ____$$$___ ___$$$$$__ __$$$$$$$_ __$$___$$_ ____$$_



    ▄︻デⱠØ₴ɆⱤ══━一


    """


#to slow print text
def machineprint(text, delay = 0.015):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(delay)
    print()

#the instructions to the game
instruct = """Instructions:
    A Hangman pic art will appear. 

    He has 7 parts, including his head and rope, that gives you 7 chances 
    to guess the word given. You will be told the number of letters in 
    the word, the letters you have guessed, and the chances you have left. 

    You will be asked if you want to guess the word or the letter. At 
    any point in the game you can change your mind and input "word" to 
    swap to inputting words, and "letter" to swap to inputting letters.

    If you guess either of them wrong, a part of the hangman will be taken
    away and you will loose a chance. 
    
    If you guess a letter twice, you will be told and no chances will be 
    lost. There are no repeating letters in the words of this game.

    If you guess a word that has one of the corrrect letters in it, you 
    will not be told what letters are correct and will still lose a life.
    
    You must guess lettters individually for them to be revealed.

    """
x = 0

#welcoming the game 
def welcome_message():
    machineprint("""

    ██╗░░██╗░█████╗░███╗░░██╗░██████╗░  ███╗░░░███╗░█████╗░███╗░░██╗
    ██║░░██║██╔══██╗████╗░██║██╔════╝░  ████╗░████║██╔══██╗████╗░██║
    ███████║███████║██╔██╗██║██║░░██╗░  ██╔████╔██║███████║██╔██╗██║
    ██╔══██║██╔══██║██║╚████║██║░░╚██╗  ██║╚██╔╝██║██╔══██║██║╚████║
    ██║░░██║██║░░██║██║░╚███║╚██████╔╝  ██║░╚═╝░██║██║░░██║██║░╚███║
    ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝

        Hello there! 
        Welcome to this little game of Hangman! 
            +---+
            |   |
            O   |
           /|\\  |
           / \\  |
                |
        =========

        Do you wish to see the instructions?
        Please answer 'Y' for yes or 'N' for no.""")

    #to see instructions
    while x != 1:
        INSTRUCTIONS = input('View instructions?: \n')
        INSTRUCTIONS = INSTRUCTIONS.lower()
        if INSTRUCTIONS == 'y': 
            print(instruct)
            x == 1
            return
        #no i don't want to see instructions: 
        elif INSTRUCTIONS == 'n':
            x == 1
            return
        #invalid respoonse: 
        else: 
            machineprint("That is an invalid input. Please try again. \n")

#getting name 
def name():
    machineprint("What is your name?")
    NAME = input('Your name: \n')

    while x != 1:
        CORRECT = input("Is this correct? Enter 'Y' or 'N': \n" )
        CORRECT = CORRECT.lower()
        if CORRECT == 'y': 
            print("Yay! Time to play," , NAME, "!")
            x == 1
            return
        elif CORRECT == 'n':
            name()
            x == 1
            return
        else: 
            machineprint("That is an invalid input. Please try again.\n")


def randomWord():
    #Open text file and get random word.
    file = open('words.txt', 'r', encoding='utf-8')
    line = file.read().splitlines()
    rando_word = random.choice(line)
    return rando_word.lower()



class GamePlay:
    """game play class"""

    def __init__(self, random_word):
        """instance attribute:
        This assigns a random word, provides empty lists for letters found and guessed.
        Correct_letters is a list of the characters for when we must check the letter.
        'n' is a variable that stores the number of letters in the word.
        'lis' holds the _ _ _ . It is updated to found the letters found in the right index 
        later on in 'checker'.

        Then user is asked if they want to use word or letter which is entered to 'func' 
        
        display function called. 
        """
        self.word = random_word
        self.letters_found = []     #the correct letters entered.
        self.letters_guessed= []      #all the letters attempted
        #print(self.word)   #for testing
        
        self.correct_letters = [x for x in self.word] # getting the individual letters

        self.n = len(self.word)                       #number of letters in word

        self.lis_ = [' _ ']*self.n        #list of _ _ _ *n
        self.chances = len(HANGMEN)                      #number of chances

        print('\n')
        machineprint("If you would prefer to guess a word, type 'word' into the terminal.")
        print('\n')
        machineprint("If you would prefer to guess a letter, type 'letter' into the terminal.")
        print('\n')
        machineprint("You can change this at any time by simply typing 'word' or 'letter' into the input.")

        self.func= input("Word or Letter?" )

        self.display()


    def WL(self, func):
        """WL staands for Word Letter. 
        the func string 'word' or 'letter' is entered, which then directs the user to 
        the word-entering function or the letter-entering funcction."""
        func = func.lower()
        if func == 'word':
            self.display_input_word()
            return
            
        elif func == 'letter': 
            self.display_input_letter()
            return

        
    
    def winner(self):
        """If useer is a winner, this function plays winner message and then 
        asks if user wants to play again. if so, the system cclears and the play() method
        is started again. If not, the goodbye message is entered. 
        """

        machineprint("You win!")

        machineprint(CELEBRATE)
        print('\n')
        playagain = input("Please enter y or n: \n" )

        if playagain.isupper():
            playagain = playagain.lower()

        if playagain == 'y': 
            os.system('clear')
            play()

        if playagain == 'n':
            machineprint("Goodbye, winner winner, chicken dinner.")
            sys.exit(1)



    def loser(self):
        """ Loser message announced. Word revealed. Playagain question asked, and if so
        system cleaars and Play() started again. If not, goodbye message printed. """
        print('\n')
        machineprint("You LOSE!")
        print('\n')
        machineprint("The word was: ")
        print(self.word)

        machineprint(LOSER)

        playagain = input("Try again? Please enter y or n: \n" )

        if playagain.isupper():
            playagain = playagain.lower()

        if playagain == 'y': 
            os.system('clear')
            play()

        if playagain == 'n':
            machineprint("Goodbye, sucker.")
            sys.exit(1)


    def display(self ):
        """This is the main function that displays the hangman as it loses limbs, 
        the cchances left, the letters found, the _ _ _, number of letters in the word.
        If chances left = 0, loser function is triggered. 
        The function is then directed to WL function, which, depending on the self.func
        variable, directs the user to the word function or letter function inputs.  """

        print('\n')
        self.chances_left = self.chances -  len(self.letters_guessed)   #the chances left
        print("Chances left:", self.chances_left, '\n')   

        if self.chances_left == 0:
            self.loser()
            return
        
        string_ = ' '.join([str(i) for i in self.lis_])  #adding the _ together in one string
        # creating hangman
        machineprint(HANGMEN[self.chances_left-1])    #-1 due to indexing in python     

        print('\n')
        machineprint(string_)                  #the _ _ _ _ 
        print('\n')
        print("This is a ", self.n , "letter word")
        print('\n') #number of chances left

        print("Incorrect letters used:",'\n' , self.letters_guessed)      #letters guessed
        print('\n' , "Letters found:",'\n' , self.letters_found)       #correct letterrs found

        self.WL(self.func)

        
    def display_input_word(self):
        """This function checks thee word entered. 
        If the function is entered using upper case, we correct it to lower case
        so we can match it up. If the user inputs 'letter;, we then redirect the user 
        to the letter input function. 
        
        If the word is not the same length as the word in queestion, a messaage prompts
        the user to enter the right number of letters, and is redirected to the top of the 
        function. 
        
        The final 'else' then assigns the  guess to self.guess, and inputs it into the 
        checker function. """

        GUESS = input("Your word guess: \n" )
        if GUESS.isupper():
            GUESS = GUESS.lower()

        if GUESS =='letter':
            self.func = 'letter'
            return

        elif len(GUESS) != self.n:
            print("Please enter a word with", self.n ,"letters. ")
            self.display_input_word()
            return

        else: 
            self.guess = GUESS
            self.checker(self.guess)
            return


    def display_input_letter(self):
        """This function checks the letter entered. 
        If the function is entered using upper case, we correct it to lower case
        so we can match it up. If the user inputs 'word;, we then redirect the user 
        to the word input function. 
        
       The letter is checked in the 'for loop' against each character in letters_guessed.
       If the guess equals a letter previously aanswers, the use is alerted and prompted 
       to try again. 

       If the guess doesn't equal one letter, the user is prompted to only guess one letter
       at a time. 
        
        The final 'else' then assigns the  guess to self.guess, and inputs it into the 
        checker function. """


        GUESS = input(" \n Your letter guess:" )

        if GUESS.isupper():
            GUESS = GUESS.lower()
        
        if not GUESS.isalpha():
            print("Invalid input. Try again.")

        if GUESS =='word':
            print("reachning func 349")
            self.func = 'word'
            self.WL(self.func)
            return

        for letter in self.letters_guessed: 
            if GUESS == letter:
                print("This letter was already attempted. Try again.")
                self.display_input_letter()
                return

        if len(GUESS) != 1:
            machineprint("Please only guess one letter at a time. ")
            self.display_input_letter()
            return
            

        else: 
            print('reaching else 365')
            self.guess = GUESS
            self.checker(self.guess)
            return

            
        
    
    def checker(self, GUESS):
        """checking if the letter guessed is in the word. 
        if it is, the index of the letter from the word is noted, and the list containg the ___ 
        is updated so the letter now stands where a _ was. 
        """
        if len(GUESS) == 1:
            for index, letter in enumerate(self.correct_letters):

                index = index
                if GUESS in self.letters_guessed:
                    print("You've already guessed this letter.")
                    
                if GUESS in self.word:
                    if letter == GUESS:
                        self.letters_found.append(GUESS)
                        self.lis_[index]=letter
                        #self.correct_letters.remove(letter)
                        machineprint('Correct guess!!!!! ')

                        if set(self.letters_found) == set(self.correct_letters):
                             self.winner()
            
                        self.start()

                else:
                     self.chances_left -= 1
                     self.letters_guessed.append(GUESS)
                     machineprint('Incorrrect guess!!!!! ')
                     self.start()
        

        if len(GUESS) == self.n:
            if GUESS == self.word:
                self.winner()
            
            else:
                 self.chances_left -= 1
                 machineprint('Incorrrect guess!!!!! ')
                 self.display()
            
            
    def start(self):
        self.display()
        
            
            

def play():
    random_word = randomWord()
    play = GamePlay(random_word)
    play.start()




welcome_message()   
name()
play()

