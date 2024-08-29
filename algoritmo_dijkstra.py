import math

class HeapMin:
    def __init__(self):
        self.nos = 0
        self.heap = []

    def adiciona_no(self, u, indice):
        self.heap.append([u, indice])
        self.nos += 1
        f = self.nos
        while True:
            if f == 1: # Quando for a raiz
                break
            p = f//2 # Divide por 2 e pega a parte inteira
            if self.heap[p-1][0] <= self.heap[f-1][0]: # Se o pai for maior que o filho
                break
            else:
                self.heap[p-1], self.heap[f-1] = self.heap[f-1], self.heap[p-1] # Swap
                f = p

    def mostra_heap(self):
        # print(self.heap) # Forma simples
        print('A estrutura heap é a seguinte:')
        nivel = int(math.log(self.nos, 2)) # Calcula o nível/altura da alvore
        a = 0
        for i in range(nivel):
            for j in range(2 ** i): # Quantidade de elementos por nível
                print(f'{self.heap[a]}', end = '  ')
                a += 1
            print('')
        for i in range(self.nos - a):
            print(f'{self.heap[a]}', end = '  ')
            a += 1
        print('')

    def remove_no(self):
        x = self.heap[0]
        self.heap[0] = self.heap[self.nos - 1] # Coloca o último elemento na primeira posição
        self.heap.pop() # Remove o último elemento
        self.nos -= 1
        p = 1
        while True:
            f = 2 * p
            if f > self.nos: # Vai acontecer quando um nó não tiver filhos
                break
            if f+1  <= self.nos: 
                if self.heap[f+1-1][0] < self.heap[f-1][0]: # f+1 é o filho a direita, e f o filho a esquerda
                    f += 1
            if self.heap[p-1] <= self.heap[f-1]: # O pai é maior ou igual ao filho
                break
            else:
                self.heap[f-1], self.heap[p-1] = self.heap[p-1], self.heap[f-1] # Troca a posição entre pai e filho
                p = f
        return x
    
    def tamanho(self):
        return self.nos
    
    def maior_elemento(self):
        if self.nos != 0:
            return self.heap[0]
        return 'Árvore vazia'
    
    def filho_esquerda(self, i):
        if self.nos >= 2*i:
            return self.heap[2 * i - 1]
        return 'Esse nó não tem filho a esquerda'
    
    def filho_direita(self, i):
        if self.nos >= 2*i + 1:
            return self.heap[2 * i + 1 - 1]
        return 'Esse nó não tem filho a direita'
        
    def pai(self, i):
        return self.heap[1 // 2]
    
class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]

    def adiciona_aresta(self, u, v, peso):
        self.grafo[u-1][v-1] = peso
        self.grafo[v-1][u-1] = peso

    def mostra_matriz(self):
        print('A matriz de adjacências é:')
        for i in range(self.vertices):
            print(self.grafo[i])
    
    def dijkstra(self, origem):
        custo_vem = [[-1, 0] for i in range(self.vertices)]
        custo_vem[origem - 1] = [0, origem]
        h = HeapMin()
        h.adiciona_no(0, origem)
        while h.tamanho() > 0:
            dist, v = h.remove_no()
            for i in range(self.vertices):
                if self.grafo[v-1][i] != 0:
                    if custo_vem[i][0] == -1 or custo_vem[i][0] > dist + self.grafo[v-1][i]:
                        custo_vem[i] = [dist + self.grafo[v-1][i], v]
                        h.adiciona_no(dist + self.grafo[v-1][i], i+1)
        return custo_vem
    
g = Grafo(7)

g.adiciona_aresta(1, 2, 5)
g.adiciona_aresta(1, 3, 6)
g.adiciona_aresta(1, 4, 10)
g.adiciona_aresta(2, 5, 13)
g.adiciona_aresta(3, 4, 3)
g.adiciona_aresta(3, 5, 11)
g.adiciona_aresta(3, 6, 6)
g.adiciona_aresta(4, 5, 6)
g.adiciona_aresta(4, 6, 4)
g.adiciona_aresta(5, 7, 3)
g.adiciona_aresta(6, 7, 8)

g.mostra_matriz()

resultado = g.dijkstra(1)
print(resultado)