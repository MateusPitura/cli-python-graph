"""
    Representação de um grafo por meio de lista de adjacência
"""


class Grafo:
    """
        Classe que representa um grafo por meio de lista de adjacência
    """

    def __init__(self, vertices):
        """
            Cada linha será um vértice
        """

        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]

    def adiciona_aresta(self, u, v):
        """
            Adiciona uma aresta entre os vértices u e v
        """

        self.grafo[u-1].append(v)
        self.grafo[v-1].append(u)

    def mostra_lista(self):
        """
            Mostra a lista de adjacências            
        """

        for i in range(self.vertices):
            print(f'{i+1}:', end='  ')
            for j in self.grafo[i]:
                print(f'{j}  ->', end='  ')
            print('')


g = Grafo(4)
g.adiciona_aresta(1, 2)
g.adiciona_aresta(1, 3)
g.adiciona_aresta(1, 4)
g.adiciona_aresta(2, 3)
g.mostra_lista()
