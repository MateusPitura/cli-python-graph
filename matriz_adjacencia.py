class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)] #Cria uma matriz quadrada com a quantidade de vértices informados onde todos os campos são zero

    # def adiciona_aresta(self, u, v, peso): # Para matriz de distância
    def adiciona_aresta(self, u, v): 
        #self.grafo[u-1][v-1] = 1 # Para matriz de distância
        self.grafo[u-1][v-1] = 1
        # self.grafo[u-1][v-1] += 1 # Para multigrafo
        self.grafo[v-1][u-1] = 1 # Para grafos não direcionado
    
    def mostra_grafo(self):
        print('A matriz de adjacências é: ')
        for  i in range(self.vertices):
            print(self.grafo[i])

    # Para descobrir os vizinhos de um vértice, basta iterar seu array e verificar onde há o valor 1

quantidadeVertices = int(input('Digite a quantidade de vértices: '))
g = Grafo(quantidadeVertices)

quantidadeArestas = int(input('Digite a quantidade de arestas: '))
for i in range(quantidadeArestas):
    u = int(input("De qual vertice parte esta aresta: "))
    v = int(input("Em qual vertice chega esta aresta: "))
    g.adiciona_aresta(u, v)

g.mostra_grafo()