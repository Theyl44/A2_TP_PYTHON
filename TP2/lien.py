from noeud import Noeud


class Lien:
    id1 = 0

    def __init__(self, node1, node2, distance):
        Lien.id1 += 1
        self.__id = Lien.id1
        self.__node1 = node1
        self.__node2 = node2
        self.__distance = distance

    def getId(self):
        return self.__id

    def setId(self, id1):
        self.__id = id1

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

    def printLien(self):
        print("[" + str(self.getId()) + "] = ", end="")
        print("["+str(self.getNoeud1().getId())+"]", end="->")
        print("["+str(self.getNoeud2().getId())+"]", end="=")
        print(self.getDistance())
