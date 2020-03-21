l1 = list()
for index in range(5):
    num = input("Entrez un entier >")
    if num.isdigit():
        num = int(num)
        if index == 0:
            min = num
            max = num
        if min > num:
            min = num
        if max < num:
            max = num
        num = int(num)
        l1.append(num)
    else:
        break
print("Le min et le max de "+str(l1)+"sont "+str(min)+" "+str(max))


