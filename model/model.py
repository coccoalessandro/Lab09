import networkx as nx
from UI.view import View
from database.DAO import DAO
from UI.controller import Controller

class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._aeroporti = DAO.getAllAeroporti()

    def buildGraph(self, distanza):
        self._grafo.add_nodes_from(self._aeroporti)
        self.addEdges(distanza)

    def addEdges(self, distanza):
        voli = DAO.getAllVoli(distanza)
        for volo in voli:
            self._grafo.add_edge(volo.id_Partenza, volo.id_Arrivo, peso = volo.distanza)

    def numNodi(self):
        return len(self._grafo.nodes)

    def numArchi(self):
        return len(self._grafo.edges)
