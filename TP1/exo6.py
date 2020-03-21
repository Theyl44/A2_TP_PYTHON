import random


def write(mot):
    for j in range(len(mot)):
        if not mot[j].isalpha():
            mot = mot.replace(mot[j], "-")
    print("your word is : " + mot)


def check(mot, c, sol):
    if c in sol:
        for index in range(len(sol)):
            if sol[index] == c and mot[index] == "-":
                mot = mot[:index] + c + mot[index + 1:]
    return mot


fileRead = open('dictionnary.txt', 'r')
lines = fileRead.readlines()
i = int(random.randint(1, len(lines)))
sol = lines[i - 1]
print("triche : ", end="")
print(sol, end="")
print(len(sol) - 1)
word = ""
for j in range(len(sol) - 1):
    word = word+"-"

player_name = str(input("Entrez votre nom >"))
for index in range(0, len(player_name) + 1):
    if sol == word:
        print("felicitation")
        break
    else:
        print("Erreur " + str(index) + "/" + str(len(player_name)))
        write(word)
        char = str(input("Entrez une lettre >"))
        word = check(word, char, sol)

