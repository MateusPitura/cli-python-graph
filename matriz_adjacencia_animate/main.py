"""
    Matriz de adjacências com animação
"""

import matplotlib.pyplot as plt
import networkx as nx


class Graph:
    """
        Classe para representação de um grafo por matriz de adjacências
    """

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for _ in range(self.vertices)]
        self.edges = []

    def adiciona_aresta(self, u, v):
        """
            Adiciona uma aresta entre os vértices u e v
        """

        if 1 <= u <= self.vertices and 1 <= v <= self.vertices:
            self.grafo[u - 1][v - 1] = 1
            self.grafo[v - 1][u - 1] = 1
            self.edges.append((min(u, v), max(u, v)))

    def remove_aresta(self, u, v):
        """
            Remove a aresta entre os vértices u e v
        """

        if 1 <= u <= self.vertices and 1 <= v <= self.vertices and self.grafo[u - 1][v - 1] == 1:
            self.grafo[u - 1][v - 1] = 0
            self.grafo[v - 1][u - 1] = 0
            self.edges.remove((min(u, v), max(u, v)))
        else:
            print("Erro: aresta não existente ou vértices fora do intervalo permitido.")

    def mostra_matriz(self):
        """
            Retorna a matriz de adjacências em formato de string
        """

        return "\n".join([" ".join(map(str, linha)) for linha in self.grafo])


quantidadeVertices = int(input("Digite a quantidade de vértices: "))
grafo_matriz = Graph(quantidadeVertices)

G = nx.Graph()
G.add_nodes_from(range(1, quantidadeVertices + 1))
pos = nx.circular_layout(G)
fig, ax = plt.subplots(figsize=(12, 6))

plt.subplots_adjust(left=0.1, right=0.8)

quantidadeArestas = int(input("Digite a quantidade de arestas: "))
for i in range(quantidadeArestas):
    start = int(input("De qual vértice parte esta aresta: "))
    end = int(input("Em qual vértice chega esta aresta: "))

    G.add_edge(start, end)
    grafo_matriz.adiciona_aresta(start, end)

    ax.clear()

    ax.set_title(f"Adicionando aresta: {start} -> {end}")
    nx.draw(G, pos, with_labels=True, node_color="skyblue",
            edge_color="black", node_size=700, font_size=12, ax=ax)

    MATRIZ_TEXTO = grafo_matriz.mostra_matriz()
    fig.text(0.85, 0.5, f"Matriz de \nAdjacências:\n{MATRIZ_TEXTO}", fontsize=10,
             family="monospace", ha="left", va="center", bbox={"facecolor": 'white', "alpha": 0.8})
    plt.pause(1)

resposta = input("Deseja remover alguma aresta? (s/n): ").strip().lower()
if resposta == 's':
    quantidadeRemover = int(input("Quantas arestas deseja remover? "))
    for i in range(quantidadeRemover):
        start = int(input("De qual vértice parte a aresta a ser removida: "))
        end = int(input("Em qual vértice chega a aresta a ser removida: "))

        if G.has_edge(start, end):
            G.remove_edge(start, end)
            grafo_matriz.remove_aresta(start, end)

            ax.clear()

            ax.set_title(f"Removendo aresta: {start} -> {end}")
            nx.draw(G, pos, with_labels=True, node_color="skyblue",
                    edge_color="black", node_size=700, font_size=12, ax=ax)

            MATRIZ_TEXTO = grafo_matriz.mostra_matriz()
            fig.text(0.85, 0.5, f"Matriz de \nAdjacências:\n{MATRIZ_TEXTO}",
                     fontsize=10, family="monospace", ha="left", va="center",
                     bbox={"facecolor": 'white', "alpha": 0.8})

            plt.pause(1)
        else:
            print("Erro: aresta não existe no grafo.")

plt.title("Grafo final - Pressione qualquer tecla para fechar")
print("\nClique no x da tela da animação para fechar o programa.")
plt.show()
