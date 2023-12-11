import random, sys

garbage_chars = '~!@#$%^&*()_+-={}[]|;:,.<>?/'

with open ('SevenLetterWords.txt') as wordListFile:
    words = wordListFile.readlines()
for i in range (len(words)):
    words[i] = words[i].strip().upper()

def main():
    print("Fallout Style Hacking Simulator. Guess the correct word based on positions of the letters.\n")
    input('Press Enter to begin:')
    
    gameWords=getWords()
    computerMemory = getComputerMemoryString(gameWords)
    secretPassword = random.choice(gameWords)