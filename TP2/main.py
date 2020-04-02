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
        # print(type(content[1]))
        for i in range(0, int(content[0][0])):
            graph.addNoeud(Noeud(list()))

        for i in range(1, len(content)):
            # on va chercher a recuperer les valeurs dans le csv
            j = 0
            val1 = ""
            val2 = ""
            distance = ""
            while content[i][0][j].isdigit():
                val1 = val1+str(content[i][0][j])
                j += 1
            j += 1
            while content[i][0][j].isdigit():
                val2 = val2+str(content[i][0][j])
                j += 1
            j += 1
            while content[i][0][j].isdigit() or content[i][0][j] == '.' or content[i][0][j] == ',':
                distance = distance + str(content[i][0][j])
                if j+1 < len(content[i][0]):
                    j += 1
                else:
                    break
            # val1 = int(content[i][0][0])
            # val2 = int(content[i][0][2])
            # distance = float(content[i][0][4:])
            # print(int(val1), int(val2), float(distance))
            graph.addLink(Lien(graph.dictNode[int(val1)], graph.dictNode[int(val2)], float(distance)))
        # on fait le lien entre les liens et la liste des noeuds
        for i in range(1, len(content)):
            link = graph.dictLink[i]
            nod1 = link.getNoeud1()
            nod2 = link.getNoeud2()

            nod1.ajoutIdentifiantLien(link)
            nod2.ajoutIdentifiantLien(link)

        return graph


Graph1 = creationGraphe(1, 'fileGraph1.csv')
# Graph2 = creationGraphe(1, 'fileGraph2.csv')
# Graph1.printGraph()
distance = Graph1.dijkstra(Graph1.dictNode[1], Graph1.dictNode[2])
print(distance)
