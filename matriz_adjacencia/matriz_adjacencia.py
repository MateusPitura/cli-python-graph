"""
    Implementação de um grafo utilizando matriz de adjacências
"""


class Grafo:
    """
        Classe que representa um grafo utilizando matriz de adjacências
    """

    def __init__(self, vertices):
        """
            Cria uma matriz quadrada com a quantidade de vértices informados onde tudo é zero
        """
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]

    def adiciona_aresta(self, u, v):
        """
            Adiciona uma aresta entre os vértices u e v
        """
        self.grafo[u-1][v-1] = 1
        self.grafo[v-1][u-1] = 1

    def mostra_grafo(self):
        """
            Adiciona uma aresta com peso entre os vértices u e v
        """
        print('A matriz de adjacências é: ')
        for vertice in range(self.vertices):
            print(self.grafo[vertice])


quantidadeVertices = int(input('Digite a quantidade de vértices: '))
g = Grafo(quantidadeVertices)
quantidadeArestas = int(input('Digite a quantidade de arestas: '))
for i in range(quantidadeArestas):
    start = int(input("De qual vertice parte esta aresta: "))
    end = int(input("Em qual vertice chega esta aresta: "))
    g.adiciona_aresta(start, end)
g.mostra_grafo()
