
from random import *
import linecache


def replaceWord(word, lettersfound):
    nbLettersWord = len(word)
    for loop in range(nbLettersWord):
        index = lettersfound.find(word[loop])
        if index == -1:
            word = word.replace(word[loop], "-")
    return word


def printWord(word):
    nbLettersWord = len(word)
    for loop in range(nbLettersWord):
        if loop != (nbLettersWord - 1):
            print(word[loop] + " ", end='')
        else:
            print(word[loop])


name = str(input('Entrez votre nom >'))

dead = 1
nbEssai = 7
dictionnary = open('Dictionnary.txt', 'r')
n = 0
for line in dictionnary:
    n += 1
dictionnary.close()
word = linecache.getline('Dictionnary.txt', randint(0, n))
word = word.upper()
word = word.replace('\n', "")

"""print(word) AFFICHER SOLUTION"""

missLetters = ""
lettersfound = ""
while dead <= nbEssai:
    hiddenWord = replaceWord(word, lettersfound)
    print('Mot : ', end='')
    printWord(hiddenWord)
    if missLetters.isalpha():
        if len(missLetters) == 1:
            print('Lettre essayée : ', end='')
        else:
            print('Lettres essayées : ', end='')
        printWord(missLetters)
    print("Essai " + str(dead) + "/" + str(nbEssai))
    letter = str(input('Entrez une lettre :'))
    letter = letter[0: 1]
    letter = letter.upper()
    index = word.find(letter)
    if index == -1:
        if missLetters.find(letter) != -1:
            print('Vous avez déjà rentré cette lettre !')
        else:
            print('La lettre ne se trouve pas dans le mot masqué.')
            missLetters += letter
            dead += 1
    else:
        if lettersfound.find(letter) != -1:
            print('Vous avez déjà rentré cette lettre !')
        else:
            lettersfound += letter
            isWinWord = replaceWord(word, lettersfound)
            isWinIndex = isWinWord.find("-")
            if isWinIndex == -1:
                break
    print()

if dead <= 7:
    print()
    printWord(word)
    print('Bravo ' + name + ' vous avez gagné !')
else:
    print('Perdu ' + name + ' vous êtes mort, le mot était ' + word + '.')

"""Verifier que valeur rentrée != chiffre"""
