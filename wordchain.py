# Name:  Jake Colson
# Student Number:  10472749

# This file is provided to you as a starting point for the "wordchain.py" program of Assignment 2
# of CSP1150/CSP5110 in Semester 1, 2018.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.

# Import the necessary modules.
import random
import urllib.request
import json
import string
import operator 

# This function repeatedly prompts for input until the user enters
# something at least one character long and entirely alphabetic.
# See the "The 'inputWord' Function" section of the assignment brief.
def inputWord(promt):
    while True:
        value = input(promt)
        if value.isalpha() == False:
            print("Invalid input, please use alphabetical characters only.")
            continue
        return value.lower()

def inputInt(promt): #stops the user and makes sure a value is an int
    while True:
        value = input(promt)
        try:
            numResponse = int(value) 
        except ValueError:
            print("Invalid input, please enter an integer.")
            continue
        return numResponse
    
def wordTypeGenerator():
    q = random.randint(1,3)
    if q == 1:
        return "noun"
    elif q == 2:
        return "verb"
    elif q == 3:
        return "adjective"

def alphaGenerator():
    return random.choice("abcdefghijklmnopqrstuvwxyz").upper()    
# Initialise variables (Requirement 1).

word = ""
wordType = ""
letter = None
playerNames = []
playerNamesImmutable = []
playerScore = {}
playerLives = {}
playerAnswer = None
playerAnswerList = []
wordCount = 0
gameData = {}
state = True
wordLength = 0
gameDataList = []

# Get player count and names (Requirements 2-3).

print("Welcome to the wordchain game!")
numOfPlayers = inputInt("Number of Players: ")
for i in range(1,numOfPlayers + 1):
    playerNames.append(inputWord("Player " + str(i) + "'s name: ").upper())


playerNamesImmutable = list(playerNames)
print(playerNamesImmutable)

for n in range(0, len(playerNames)):
    playerScore.update({playerNames[n]: 0})
    playerLives.update({playerNames[n]: 3})

# Begin main gameplay loop (Requirement 4).
while state == True:
    for n in range(0, len(playerNames)): #for each player

        #generates first random letter
        if wordCount == 0:
            letter = random.choice(string.ascii_letters)
            letter = letter.upper()
        wordType = wordTypeGenerator()
        print("Lives: "+ str(playerLives) + "\n")
        print("Okay " + playerNames[n] + ", you need to find a " + wordType + " that begins with the letter " + letter)

        playerAnswer = inputWord("Please enter your answer: ")
        playerAnswer = str(playerAnswer)
        word = playerAnswer
        wordLength = len(word)

        if playerAnswer in playerAnswerList:
            print("This word has been used before.")
            playerLives[playerNames[n]] -= 1
            print("\n" + str(playerNames[n] + " is now on " + str(playerLives[playerNames[n]]) + " lives" ))
            if playerLives[playerNames[n]] == 0:
                print("\n" + playerNames[n] + " Has ran out of lives and has been removed from the game.")
                playerNames.remove(playerNames[n])
                break

        elif playerAnswer[0].upper() != letter:
            print("The first letter of " + playerAnswer + " is not " + letter )
            playerLives[playerNames[n]] -= 1
            print("\n" + str(playerNames[n] + " is now on " + str(playerLives[playerNames[n]]) + " lives" ))

            if playerLives[playerNames[n]] == 0:
                print("\n" + playerNames[n] + " Has ran out of lives and has been removed from the game.")
                playerNames.remove(playerNames[n])
                break

        #gets response on wordnik
        if playerAnswer not in playerAnswerList and playerAnswer[0].upper() == letter:
            response = urllib.request.urlopen('http://api.wordnik.com:80/v4/word.json/' + word + '/definitions?limit=5&partOfSpeech=' + wordType + '&api_key=aaaa946871985c2eb2004061aba0695e00190753d6560ebea') #taken from the discussion board
            wordData = json.load(response)
            for i in range(0, len(wordData)):
                firstDef = wordData[i]
                print("\n" + "○ " + firstDef['text'] + "\n")

            #checks if search resault came back blank
            if wordData == []:
                print(word + " is not a " + wordType)
                playerLives[playerNames[n]] -= 1
                print("\n" + str(playerNames[n] + " is now on " + str(playerLives[playerNames[n]]) + " lives" ))
                if playerLives[playerNames[n]] == 0:
                    print("\n" + playerNames[n] + " Has ran out of lives and has been removed from the game.")
                    playerNames.remove(playerNames[n])
                    break
            
            else:

                print("\nWell done " + playerNames[n] + "! " + word + " is " + str(wordLength) + " characters long!\n")
                playerScore[playerNames[n]] += wordLength
                print("Scoreboard: " + str(playerScore) + "\n")
                playerAnswerList.append(playerAnswer)
                letter = alphaGenerator()
                letter = letter.upper()
                wordCount += 1
                print("Chain number: " + str(wordCount) + "\n")
                

                
            
    
    if len(playerNames) == 0 :
        state == False
        break
        
    
# Show final chain length and record a log of the game (Requirement 5).

print("\nThe Game has ended")
print("\nThe words used were: " + str(playerAnswerList))
print("\nNumber of words: " + str(wordCount))


winner = max(playerScore.items(), key=operator.itemgetter(1))
print("\nThe winner is " + str(winner[0]) + " with a score of " + str(winner[1]))

print("\n Scoreboard: \n" + str(playerScore))


gameData = {
    "Players": numOfPlayers,
    "Names": playerNamesImmutable,
    "Winner": winner[0],
    "Scores": playerScore,
    "Chain": wordCount,
    "Words used": playerAnswerList,
}

if wordCount >= 1:     
    try:
        with open("log.txt","r") as logFile:
            gameDataList = json.load(logFile)
            gameDataList.append(gameData)
            logFile.close()
        with open("log.txt","w") as logFile:
            json.dump(gameDataList,logFile,indent=4)
            logFile.close()
    except:
        with open("log.txt","w") as logFile:
            gameDataList = [gameData]
            json.dump(gameDataList,logFile,indent=4)
            logFile.close()
        
