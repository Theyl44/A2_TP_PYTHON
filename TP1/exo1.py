import random

nom = input("Entrez votre Nom : ")
sol = int(random.randint(0, len(nom)))

for index in range(1, len(nom)+1):
    print("Essai {0}/{1}".format(index,len(nom)))
    val = input("Entrez un nombre entre 0 et 20 >")
    while not val.isdigit():
        print("Essai {0}/{1}".format(index,len(nom)))
        val = input("Entrez un nombre entre 0 et 20 >")
    val =int(val)
    if val < sol:
        print("Le nombre est plus grand")
    else:
        if val == sol:
            print("Bravo vous avez gagné")
            break
        else:
            print("Le nombre est plus petit")

print("vous avez perdu ")


