class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]

    def adiciona_aresta(self, u, v): 
        self.grafo[u-1][v-1] += 1
        if u != v: #Caso seja feito um laço, para não ficar repetido
            self.grafo[v-1][u-1] += 1
    
    def mostra_grafo(self):
        print('A matriz de adjacências é: ')
        for  i in range(self.vertices):
            print(self.grafo[i])

    def tem_aresta(self, u, v):
        if self.grafo[u-1][v-1] == 0:
            print(f'Não tem aresta entre {u} e {v}')
        else:
            print(f'Existe {self.grafo[u-1][v-1]} de arestas entre os vértices {u} e {v}')

    def isEuleriano(self):
        contador = 0
        for i in range(self.vertices):
            grau = 0
            for j in range(self.vertices):
                if i == j: #Laço conta como 2 graus
                    grau += 2 * self.grafo[i][j]
                else:
                    grau += self.grafo[i][j]
            if grau % 2 != 0: #Verifica se é impar
                contador += 1
        if contador == 0:
            print("É euleriano")
        elif contador == 2:
            print('É semi-euleriano')
        else:
            print('Não é euleriano nem semi-euleriano')


g = Grafo(4)

g.adiciona_aresta(1, 2)
g.adiciona_aresta(3, 4)
g.adiciona_aresta(2, 3)

g.isEuleriano()

g.mostra_grafo()
