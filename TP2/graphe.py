from noeud import Noeud

class Graph:

    def __init__(self, id):
        self._id = id
        self._nbrNodes = 0
        self._dictNodes = {}
        self._dictLinks = {}

    def getNbrNodes(self):  
        return self._nbrNodes

    def addNoeud(self, Noeud):
        self._nbrNodes += 1
        self._dictNodes[Noeud.getId()] = Noeud

    def addLink(self, Lien):
        self._dictLinks[Lien.getId()] = Lien

    def obtenirProchainsNoeuds(self, id):
        lien = self._dictNodes[id].__l1
        newdict = {}
        for i in range(0, len(lien)):
            if lien[i].getNoeud1 == id:
                newdict[lien[i].getNoeud2] = lien[i].getDistance
            else:
                newdict[lien[i].getNoeud1] = lien[i].getDistance
        return newdict

    def __str__(self):
        print("Id des noeuds du graphe :")
        for elem1 in self._dictNodes:
            self._dictNodes[elem1].__str__()
            
        print("Id des liens du graphe :")
        for elem2 in self._dictLinks:
            self._dictNodes[elem2].__str__()




