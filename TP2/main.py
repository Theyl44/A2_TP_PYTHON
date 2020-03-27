import csv
from graphe import Graph
from lien import Lien
from noeud import Noeud


def creationGraphe(id , path):
    graph = Graph(id)
    with open(path, newline="") as file:
        fileRead = csv.reader(file)
        content = list()
        for row in fileRead:
            row[0] = row[0].replace('\t', " ")
            content.append(row)
        # print(content[1][0][2])
        for i in range(0, int(content[0][0])):
            graph.addNoeud(Noeud(list()))
        for i in range(1, len(content)):
            graph.addLink(Lien(graph.dictNode[int(content[i][0][0])], graph.dictNode[int(content[i][0][2])], float(content[i][0][4:])))
        for i in range(1, len(content)):
            link = graph.dictLink[i]
            nod1 = link.getNoeud1()
            nod2 = link.getNoeud2()

            nod1.ajoutIdentifiantLien(link)
            nod2.ajoutIdentifiantLien(link)

        return graph


Graph1 = creationGraphe(1, 'fileGraph1.csv')
Graph1.printGraph()

