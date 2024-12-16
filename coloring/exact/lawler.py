"""
    Este arquivo contém o ínicio da implementação do 
    algoritmo de Lawler para coloração exata de grafos.
    Seu pseudocódigo é pode ser encontrado no artigo 
    Exact Algorithms for the Graph Coloring Problem.PDF
"""


class Graph:
    """
        Classe que representa um grafo
    """

    def __init__(self, nodes):
        self.nodes = nodes
        # Cada linha será um vértice contendo um array vazio
        self.graph = [[] for i in range(self.nodes)]

    def add_edge(self, u, v):
        """
            Adiciona uma aresta entre os vértices u e v
        """

        self.graph[u-1].append(v)
        self.graph[v-1].append(u)

    def show(self):
        """
            Mostra o grafo
        """

        for i in range(self.nodes):
            print(f'{i+1}:', end='  ')
            for j in self.graph[i]:
                print(f'{j} ->', end='  ')
            print('')

    def lawler(self):
        """
            Não está finalizado, algoritmo em si de lawler
        """

        n = self.nodes
        # Guardará as cores usadas, inicializa com infinito
        x = [[float('inf')]*(2**self.nodes-1)]
        x[0] = 0
        for s in range(1, 2**n):  # Acho que falta o - 1 no 2**n
            # As próximas 3 linhas geram todas os subsets possíveis,
            # se n = 3 e self.graph = {A, B, C},
            # todos os subsets gerados seriam
            # {A}, {B}, {A, B}, {C}, {A, C}, {B, C}, {A, B, C}
            subset = set()
            for i, vertex in enumerate(self.graph):
                # Desloca a forma binária do s para a direita e compara o último digito com 1
                if (s >> i) & 1:
                    subset.add(vertex)
            # O nº cromático do subset de index s começará com infinito
            x[s] = float('inf')
