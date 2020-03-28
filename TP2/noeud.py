class Noeud:
    id1 = 0

    def __init__(self, list):
        Noeud.id1 += 1
        self.__id = Noeud.id1
        self.__l1 = list

    def getId(self):
        return self.__id

    def getl1(self):
        return self.__l1

    def setId(self, id):
        self.__id = id

    def setl1(self, l1):
        self.__l1 = l1

    def printNoeud(self):
        print("[" + str(self.getId()) + "] =>", end="")
        self.afficherIdentifiantLien()
        print()

    def afficherIdentifiantLien(self):
            for elem in self.__l1:
                print("["+str(elem.getId())+"]", end="")

    def ajoutIdentifiantLien(self, id):
        self.__l1.append(id)







