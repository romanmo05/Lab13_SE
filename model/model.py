import networkx as nx
from database.dao import DAO


class Model:
    def __init__(self):
        self.dao = DAO()
        self.graph = nx.DiGraph()

    def buildgraph(self):
        self.graph.clear()
        for c in self.dao.get_cromosomi():
            self.graph.add_node(c)

    def numVertici(self):
        return self.grafo.number_of_nodes()

    def numArchi(self):
        return self.grafo.number_of_edges()

    def getPesoMinMax(self):
        pesi = [d["weight"] for _, _, d in self.grafo.edges(data=True)]
        return min(pesi), max(pesi)

    def contaArchi(self, soglia):
        minori = 0
        maggiori = 0

        for _, _, d in self.grafo.edges(data=True):
            if d["weight"] < soglia:
                minori += 1
            elif d["weight"] > soglia:
                maggiori += 1

        return minori, maggiori

    def camminoMassimo(self, soglia):
        self.bestPeso = 0
        self.bestPath = []

        for nodo in self.grafo.nodes:
            self._dfs([nodo], 0, soglia)

        return self.bestPath, self.bestPeso

    def _dfs(self, path, peso, soglia):
        if peso > self.bestPeso:
            self.bestPeso = peso
            self.bestPath = list(path)

        last = path[-1]

        for succ in self.grafo.successors(last):
            if succ not in path:
                w = self.grafo[last][succ]["weight"]
                if w > soglia:
                    path.append(succ)
                    self._dfs(path, peso + w, soglia)
                    path.pop()


