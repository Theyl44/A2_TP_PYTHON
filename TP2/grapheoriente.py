from graphe import Graph

class GrapheOriente(Graph):

    def obtenirProchainsNoeuds(self, id):
        nextNode = dict()
        lien = self.dictNode[id].getl1()
        for i in range(len(lien)):
            if lien[i].getNoeud1().getId() == id:
                nextNode[lien[i].getNoeud2().getId()] = lien[i].getDistance()

        return nextNode
