from noeud import Noeud
from collections import defaultdict
from heapq import *

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
        lien = self.dictNode[id].__l1
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

        g = defaultdict(list)
        for l, r, c in self.dictLink:
            g[l].append((c, r))

        q, seen, mins = [(0, f, ())], set(), {f: 0}
        while q:
            (cost, v1, path) = heappop(q)
            if v1 not in seen:
                seen.add(v1)
                path = (v1, path)
                if v1 == t:
                    return cost, path

                for c, v2 in g.get(v1, ()):
                    if v2 in seen: continue
                    prev = mins.get(v2, None)
                    next = cost + c
                    if prev is None or next < prev:
                        mins[v2] = next
                        heappush(q, (next, v2, path))

        return float("inf")

