from noeud import Noeud


class Lien:

    def __init__(self, node1, node2, distance):
        self.__id = 1
        self.__node1 = node1
        self.__node2 = node2
        self.__distance = distance

    def getId(cls):
        return Lien.Identifiant

    def setId(self, id):
        self.__id = id

    def getDistance(self):
        return self.__distance

    def setDistance(self, distance):
        self.__distance = distance

    def getNoeud1(self):
        return self.__node1

    def setNoeud1(self, noeud1):
        self.__node1 = noeud1

    def getNoeud2(self):
        return self.__node2

    def setNoeud2(self, noeud2):
        self.__node2 = noeud2

    def __str__(self):
        print("id = " + self.getId())
