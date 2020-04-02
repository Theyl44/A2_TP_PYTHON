import sys
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

    def getDictNode(self):
        return self.dictNode

    def getDictLink(self):
        return self.dictLink

    def addLink(self, Lien):
        self.dictLink[Lien.getId()] = Lien

    def obtenirProchainsNoeuds(self, id):
        lien = self.dictNode[int(id)].__l1
        newdict = {}
        for i in range(0, len(lien)):
            if lien[i].getNoeud1 == id:
                newdict[lien[i].getNoeud2] = lien[i].getDistance
            else:
                newdict[lien[i].getNoeud1] = lien[i].getDistance
        return newdict


    def printGraph(self):
        print("Graph[" + str(self.id) + "]")
        print("Id des noeuds du graphe => l'id des liens")
        for elem1 in self.dictNode:
            self.dictNode[elem1].printNoeud()

        print("Id des liens du graphe = noeud1 -> noeud2 = distance ")
        for elem2 in self.dictLink:
            self.dictLink[elem2].printLien()

    def dijkstra(self, f, t):
        nodeId = f.getId()
        dist = [None] * len(self.getDictNode())
        for i in range(len(dist)):
            dist[i] = sys.maxsize
            dist[i].append([self.getDictNode()[nodeId]])
        dist[nodeId][0] = 0
        nodeQueue = [i for i in range(len(self.getDictNode()))]
        nodesSeen = set()
        while len(nodeQueue):
            dist_min = sys.maxsize
            node_min = None
            for n in nodeQueue:
                if dist[n][0] < dist_min and n not in nodesSeen:
                    dist_min = dist[n][0]
                    node_min = n
            nodeQueue.remove(node_min)
            nodesSeen.add(nodesSeen)
            neighbours = self.obtenirProchainsNoeuds(node_min.getId())
            for(node, edge) in neighbours:
                dist_tot = edge.getl1() + dist_min
                if dist_tot < dist[node.getId()][0]:
                    dist[node.getId()][0] = dist_tot
                    dist[node.getId()][1] = list(dist[node_min][1])
                    dist[node.getId()][1].append(node)
            return dist

