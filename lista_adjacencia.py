class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)] # Cada linha será um vértice
    
    # def adiciona_aresta(self, u, v, peso): # Para grafo valorado
    def adiciona_aresta(self, u, v):
        # self.grafo[u-1].append([v, peso]) # Para grafo valorado
        self.grafo[u-1].append(v)
        self.grafo[v-1].append(u) # Para grafo não direcionado

    def mostra_lista(self):
        for i in range(self.vertices):
            print(f'{i+1}:', end='  ')
            for j in self.grafo[i]:
                print(f'{j}  ->', end='  ')
            print('')

g = Grafo(4)

g.adiciona_aresta(1, 2, 5)
g.adiciona_aresta(1, 3, 7)
g.adiciona_aresta(1, 4, 6)
g.adiciona_aresta(2, 3, 9)

g.mostra_lista()