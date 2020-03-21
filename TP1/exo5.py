s1 = input("Entrez le premier mot >")
s2 = input("Entrez le deuxieme mot >")
s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()

if sorted(s1) == sorted(s2):
    print("The strings are anagrams.")
else:
    print("The strings aren't anagrams.")
