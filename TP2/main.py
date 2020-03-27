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
        # print(content[3][0][4:])
        for i in range(0, int(content[0][0])):
            graph.addNoeud(Noeud(list()))
        for i in range(1, len(content)):
            # print(content[i][0][:2])
            # print(content[i][0][4])
            # print(content[i][0][4:])
            # print("---")

            node1 = graph.dictNode[content[i][0][:2]]
            node2 = graph.dictNode[content[i][0][4]]
            distance = float(content[i][0][4:])
            lien = Lien(node1, node2, distance)
            graph.addLink(Lien(node1, node2, distance))

        # TODO faire le lien entre les liens et la liste de chaque noeu
        # TODO finir le tp askip
        # graph.printGraph()
        return graph


Graph1 = creationGraphe(1, 'fileGraph1.csv')
# nod1 = Noeud(list())
# nod2 = Noeud(list())
# lien1 = Lien(nod1, nod2, 2)
# lien2 = Lien(nod2, nod1, 3)
# Graph1 = Graph(1)
# Graph1.addNoeud(nod1)
# Graph1.addNoeud(nod2)
# Graph1.addLink(lien1)
# Graph1.addLink(lien2)
# nod3 = Graph1.dictNode[nod1.getId()]
# if nod1 == nod3:
#     print("true")
# else:
#     print("false")
Graph1.printGraph()

