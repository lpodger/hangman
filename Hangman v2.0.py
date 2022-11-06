#########################################################################
#
#  Python Project - Hangman Original
#
#  File:       Python Hangman Game/Project/Hangman.py
#  Project:    Programming Project
#  Author:     Lachlan Podger
#  Copyright:  © Copyright 2022, Lachlan Podger
#
#########################################################################
#
# importing modules
# import system, name and path from os
from os import system, name
# import time to show output for some time period
import time
#
import os.path
#
import random
#########################################################################
# CONSTANTS
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# No longer a constant as of v1.2
#MAX_LIVES = 10

SCORE_AMOUNT = 10

##########################################################################
# INPUT FUNCTIONS

def askUserForSingleCharacter(options=[], prompt="Enter a character"):
    choice = ""
    if len(options) == 0:
        options = ALPHABET
    optionsList = ",".join(options)
    while options.count(choice) <= 0:
        print("Options are: " + optionsList)
        choice = input(prompt + ": ")
        if options.count(choice) <= 0:
            print("OOPS! You made an error...")
        #end if
    #end while
    return choice

# function included as part of Enhancement 1
def getPlayerName():
    # Display game Title
    print("="*40)
    print("Simple Games Collective presents...")
    print("Hangman")
    print("="*40)
    # get player name
    playerName=input("Enter player name: ")
    # if player name is blank, display error message and reprompt
    while playerName=="":
        print("Player name cannot be blank.")
        playerName=input("Please enter player name: ")
    # end while
    # welcome player and explain rules
    print("")
    print("Hello", playerName+".")
    time.sleep(2)
    print("We're going to play a little game...")
    print("")
    time.sleep(3)
    print("I have randomly selected a word for you to guess.")
    time.sleep(3)
    print("The amount of chances you have to guess this word will depend on the difficulty you select.")
    time.sleep(4)
    print("If you fail to guess the word with the allotted chances given...")
    time.sleep(3)
    print("The floor beneath you will collapse...")
    time.sleep(3)
    print("You will be asphyxiated by a combination of gravity and the weight of your sins.")
    time.sleep(3.5)
    print("However, if you correctly guess the word, your life will be spared.")
    time.sleep(3.5)
    print("You've been playing guessing games with investor's funds...")
    time.sleep(3)
    print("Now you will guess for your life.")
    time.sleep(2.5)
    print("Live or die...")
    time.sleep(2)
    print("It's your choice.")
    time.sleep(2)

    # return player name
    return playerName
# end def 

# function included as part of Enhancement 3
def askUserForChoice(validChoices):
    choice = ""
    # while choice not in valid chars:
    while choice not in validChoices:
        choice = input("Select your difficulty: ")
        if choice in validChoices:
            break
        else:
            print("That is not an option, try again...")
        # end if
    #end while
    return choice
# end askUserForChoice

# function included as part of Enhancement 2
def fileExists():
    global fileName 
    global filePath
    while os.path.exists(filePath) != True:
        print("File not found.")
        fileName = input("Enter name of file: ")
        filePath = os.path.normcase("./word-lists/{0}".format(fileName))
    if os.path.exists(filePath) == True:
            print("File Found")
#end fileExists

# function included as part of Enhancement 2
def readFile():
    global fileName 
    global filePath
    file = open(filePath, "r")
    ListofWords = file.read().split()

    while bool(ListofWords) != True:
        print("Error, list is empty.")
        fileName = input("Enter name of file: ")
        filePath = os.path.normcase("./word-lists/{0}".format(fileName))
        file = open(filePath, "r")
        ListofWords = file.read().split()
    file.close()
            
        #print(ListofWords) edit in for testing
#end readFile


##########################################################################
# UTILITY FUNCTIONS
#
# define the clear screen function
def clearScreen():
    # for Windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux (here os.name is 'posix')
    else:
        _ = system('clear')
#
# Display a line of characters with end characters different if required
def displayLine(char="=", lineLength=10, endChar="*"):
    print(endChar + char * (lineLength - len(endChar) * 2) + endChar)
#
#
# function included as part of Enhancement 3
# Create menu styling
def showMenu(menuWidth=60, menuLines=[]):
    clearScreen()
    insideWidth = menuWidth - 4
    displayLine("-", menuWidth, "+")
    for aMenuLine in menuLines:
        print("| {1:{0}} |".format(insideWidth, aMenuLine))
    displayLine("-", menuWidth, "+")
# end showMenu

# function included as part of Enhancement 2
def selectWord():
    
    with open(filePath, "r") as file:
        content = file.read()
        global words
        words = list(map(str, content.split()))
        file.close()
         
#end selectWord
 
#########################################################################
# THE MAIN PROGRAM
#########################################################################
clearScreen()
displayLine("-", 80, "-")

# Welcome enhancement included from v1.1 onward

# Welcome the user
playerName = getPlayerName()

# Menu enhancement included from v1.2 onward
 
# set up predetermined list of menu choices
choices = ["0","1","2","3"]
# set menu options
myMenu = [
        "Menu - Enter a number. ",
        " ",
        "1) Easy",
        "2) Normal ",
        "3) Hard ",
        " ",
        "0) Quit"
    ]

# Start up sequence...
clearScreen()
print("Starting up...")
time.sleep(2)

# display the menu and process choice
showMenu(40, myMenu)
menuChoice = askUserForChoice(choices)
print()

if menuChoice == "0":
    dummy = input("Press [ENTER] to exit...")
    quit()
if menuChoice == "1":
    print("A coward always chooses the easy way out.")
    print("You have 15 guesses.")
    lives = 15;
elif menuChoice == "2":
    print("Mediocrity was always your forte...")
    print("You have 10 guesses.")
    lives = 10;
elif menuChoice == "3":
    print("Only those who risk going too far can find out how far one can go.")
    print("You have 5 guesses.")
    lives = 5;
    
dummy = input("Press [ENTER] to continue...")
print()

# add line
displayLine("=", 80, "=")

# set the secret word
# open the default file and extract a list of words, and randomly select
# from that list.
# Secret word enhancment included
fileName = input("Enter name of file: ")
filePath = os.path.normcase("./word-lists/{0}".format(fileName))

# fileExists function
fileExists()

# readFile function
readFile()

# selectWord function
selectWord()

word = random.choice(words)
#print(word) used for testing

# create a guesses variable with an empty value
guesses = ''

# create a variable for the score
score = 0

# Lives now determined as part of Enhancment 3
# determine the number of lives
#lives = MAX_LIVES

# list of letters not used
letters = ALPHABET

# Create a while loop
# check if the lives are more than zero
while lives > 0:
    # make a counter that starts with zero
    failed = 0

    print("\nGuess the word: ", end="")
    # for every character in the secret word
    for char in word:
        # see if the character is in the players guesses
        if char in guesses:
            # print then out the character
            print(char, end="")
        else:
            # if not found, print a dash
            print("-", end="")
            # and increase the failed counter by one
            failed += 1
    #if failed is equal to zero
    # print You Won
    if failed == 0:
        print("\nYou won")
        # exit the script
        break

    print("\n\n")
    # ask the user to guess a character
    guess = askUserForSingleCharacter(letters, "Enter a character")
    # add the guess to the list of characters used so far...
    guesses += guess

    # remove the guess from the list of available letters
    letters.remove(guess)

    # if the guess is not found in the secret word
    if guess not in word:
        # lives counter decreases by 1
        lives -= 1
        # print wrong
        print("Guessed Wrong!\n")
    else:
        # increase the player score
        score = score + SCORE_AMOUNT

    # how many lives are left
    print("You have", + lives, 'more guesses\n')

    # if the lives are equal to zero
    if lives == 0:
        # print "You Lose"
        print("You Lose")
        
# Press enter to quit
finish = input("Press enter to finish. Goodbye " + playerName)
