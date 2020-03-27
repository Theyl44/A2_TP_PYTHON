from noeud import Noeud

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
        print("Graph["+str(self.id)+"]")
        print("Id des noeuds du graphe :")
        for elem1 in self.dictNode:
            self.dictNode[elem1].printNoeud()
            
        print("Id des liens du graphe :")
        for elem2 in self.dictLink:
            self.dictLink[elem2].printLien()




