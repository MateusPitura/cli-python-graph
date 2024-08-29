import math

class HeapMax:
    def __init__(self):
        self.nos = 0
        self.heap = []

    def adiciona_no(self, u):
        self.heap.append(u)
        self.nos += 1
        f = self.nos
        while True:
            if f == 1: # Quando for a raiz
                break
            p = f//2 # Divide por 2 e pega a parte inteira
            if self.heap[p-1] >= self.heap[f-1]: # Se o pai for maior que o filho
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
                if self.heap[f+1-1] > self.heap[f-1]: # f+1 é o filho a direita, e f o filho a esquerda
                    f += 1
            if self.heap[p-1] >= self.heap[f-1]: # O pai é maior ou igual ao filho
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

h = HeapMax()
h.adiciona_no(17)
h.adiciona_no(36)
h.adiciona_no(25)
h.adiciona_no(7)
h.adiciona_no(3)
h.adiciona_no(100)
h.adiciona_no(1)
h.adiciona_no(2)
h.adiciona_no(19)

elementomax = h.remove_no()
print(f'O elemento máximo é: {elementomax}')

print(f'Tamanho: {h.tamanho()}')
print(f'Filho a esquerda de 25: {h.filho_esquerda(3)}')
print(f'Filho a direita de 25: {h.filho_direita(3)}')


h.mostra_heap()