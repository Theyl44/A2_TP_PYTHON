from noeud import Noeud
from collections import defaultdict
import copy

class Graph:

    def __init__(self, id):
        self.id = id
        self.nbrNodes = 0
        self.dictNode = {}
        self.dictLink = {}

    def getNbrNodes(self):
        return self.nbrNodes

    def addNoeud(self, Noeud):
        self.nbrNodes += 1
        self.dictNode[Noeud.getId()] = Noeud

    def removeNoeud(self, idNoeud):
        self.dictNode.pop(idNoeud)
        return self.dictNode

    def getDictNode(self):
        return self.dictNode

    def getDictLink(self):
        return self.dictLink

    def addLink(self, Lien):
        self.dictLink[Lien.getId()] = Lien

    def printGraph(self):
        print("Graph[" + str(self.id) + "]")
        print("Id des noeuds du graphe => l'id des liens")
        for elem1 in self.dictNode:
            self.dictNode[elem1].printNoeud()

        print("Id des liens du graphe = noeud1 -> noeud2 = distance ")
        for elem2 in self.dictLink:
            self.dictLink[elem2].printLien()


    def obtenirProchainsNoeuds(self, id):
        nextNode = dict()
        lien = self.dictNode[id].getl1()
        for i in range(len(lien)):
            if lien[i].getNoeud1().getId() == id:
                nextNode[lien[i].getNoeud2().getId()] = lien[i].getDistance()
            else:
                nextNode[lien[i].getNoeud1().getId()] = lien[i].getDistance()
        return nextNode

    def dijkstra(self, noeudDep, noeudArr):
        distance = {}      #distance
        Path = {}          #chemin
        NVisit = {}        #les elem qui sont visité id noeud : id si visité 0 sinon

        #init des val des dict
        idNoeudDep = noeudDep
        for i in range(1, self.getNbrNodes() + 1):
            if i == idNoeudDep:
                distance[i] = "0"
                Path[i] = i
                NVisit[i] = 0
            else:
                distance[i] = float('inf')
                NVisit[i] = i
                Path[i] = i

        idCourant = idNoeudDep
        bool = False
        #on arrive dans le srx
        while bool == False:#on verifie un sommet hors de P
            i = 0
            for elem in NVisit:
                if NVisit[elem] == 0:
                    i += 1

            if i == len(NVisit) - 1 :
                bool = True #on aura tout visité
                break

            # print("NC : "+str(idCourant))
            listNoeudproxy = self.obtenirProchainsNoeuds(int(idCourant))
            # print(listNoeudproxy)
            distanceMin = float('inf')

            idmin = 0
            for elem in listNoeudproxy:
                val = listNoeudproxy[elem]
                if val < distanceMin and NVisit[elem] != 0:
                    distanceMin = val
                    idmin = elem

            # print("+ p'tit distance = "+str(distanceMin)+" du noeud "+str(idmin))
            for elem in listNoeudproxy:
                distance[elem] = min(float(distance[elem]), float(distance[idCourant]) + float(listNoeudproxy[elem]))
                if float(distance[elem]) > float(distance[idCourant]) + float(distanceMin):
                    Path[elem] = str(Path[elem])+str(idCourant)

            NVisit[idCourant] = 0
            idCourant = idmin

        return distance[noeudArr]
