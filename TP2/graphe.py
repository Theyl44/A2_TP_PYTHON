
class Graph:
    def __init__(self, id):
        self._id = id
        self._nbrNodes = 0
        self._dictNodes = {}
        self._dictLinks = {}

    def getNbrNodes(self):
        return self._nbrNodes

    def addNoeud(self, noeud):
        self._dictNodes[noeud.getId()] = noeud
