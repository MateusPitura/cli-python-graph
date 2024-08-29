class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = [[] for i in range(self.nodes)] # Cada linha será um vértice contendo um array vazio
    
    def add_edge(self, u, v):
        self.graph[u-1].append(v)
        self.graph[v-1].append(u)

    def show(self):
        for i in range(self.nodes):
            print(f'{i+1}:', end='  ')
            for j in self.graph[i]:
                print(f'{j} ->', end='  ')
            print('')

    def lawler(self):
        n = self.nodes
        X = [[float('inf')]*(2**self.nodes-1)] # Guardará as cores usadas, inicializa com infinito
        X[0] = 0
        for s in range(1, 2**n): # Acho que falta o - 1 no 2**n
            # As próximas 3 linhas geram todas os subsets possíveis, se n = 3 e self.graph = {A, B, C}, todos os subsets gerados seriam {A}, {B}, {A, B}, {C}, {A, C}, {B, C}, {A, B, C}
            subset = set()
            for i, vertex in enumerate(self.graph):
                if(s >> i) & 1: # Desloca a forma binária do s para a direita e compara o último digito com 1
                    subset.add(vertex)

            X[s] = float('inf') # O nº cromático do subset de index s começará com infinito
