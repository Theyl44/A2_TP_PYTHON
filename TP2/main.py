import csv

def creationGraphe(id , path):
    with open(path, newline="") as file:
        fileRead = csv.reader(file)
        for row in fileRead:
            print(row)


creationGraphe(1, 'fileGraph1.csv')
