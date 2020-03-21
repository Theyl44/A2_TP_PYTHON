iban = str("IE29 AIBK 9311 5212 3456 78")
print(iban)
sol = iban[2:4]
numCara = 0
for index in range(len(iban)):
    if iban[index].isalpha():
           numCara += 1


start = iban[0:2]
iban = iban[5:len(iban)]+" "+str(start)+"00"
print(iban)
for index in range(len(iban) + numCara):
    if str.isalpha(iban[index]):
        iban = iban.replace(iban[index], str(int(ord(iban[index])) - 55))
iban = iban.replace(" ", "")
print(iban)
iban = 98 - int(iban) % 97
if iban == sol:
    print("c'est le bon iban")
else:
    print("c'est pas le bon iban")
