char = input("Entrez votre mot > ")
char1 = char.replace(" ", "")
char1 = char1.lower()
reverse = char1[::-1]

if char1 == reverse:
    print(char+" est un palindrome.")
else:
    print(char+" n'est pas un palindrome.")

