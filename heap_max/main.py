"""
    Este é um exemplo de implementação de um heap máximo
"""

import math


class HeapMax:
    """
        Implementação de um heap máximo
    """

    def __init__(self):
        self.nos = 0
        self.heap = []

    def adiciona_no(self, u):
        """
            Adiciona um nó ao heap
            Se for igual a raiz não faz nada
            Se o pai for maior que o filho não faz nada
            Se não, troca a posição entre pai e filho
        """

        self.heap.append(u)
        self.nos += 1
        f = self.nos
        while True:
            if f == 1:
                break
            p = f//2
            if self.heap[p-1] >= self.heap[f-1]:
                break
            self.heap[p-1], self.heap[f-1] = self.heap[f-1], self.heap[p-1]
            f = p

    def mostra_heap(self):
        """
            Mostra a estrutura do heap
        """

        print('A estrutura heap é a seguinte:')
        nivel = int(math.log(self.nos, 2))
        a = 0
        for i in range(nivel):
            for _ in range(2 ** i):  # Quantidade de elementos por nível
                print(f'{self.heap[a]}', end='  ')
                a += 1
            print('')
        for i in range(self.nos - a):
            print(f'{self.heap[a]}', end='  ')
            a += 1
        print('')

    def remove_no(self):
        """
            Remove o nó máximo
            Coloca o último elemento na primeira posição
        """

        x = self.heap[0]
        self.heap[0] = self.heap[self.nos - 1]
        self.heap.pop()
        self.nos -= 1
        p = 1
        while True:
            f = 2 * p
            if f > self.nos:
                break
            if f+1 <= self.nos:
                if self.heap[f+1-1] > self.heap[f-1]:
                    f += 1
            if self.heap[p-1] >= self.heap[f-1]:
                break
            self.heap[f-1], self.heap[p-1] = self.heap[p-1], self.heap[f-1]
            p = f
        return x

    def tamanho(self):
        """
            Retorna o tamanho do heap
        """

        return self.nos

    def maior_elemento(self):
        """
            Retorna o maior elemento do heap
        """

        if self.nos != 0:
            return self.heap[0]
        return 'Árvore vazia'

    def filho_esquerda(self, i):
        """
            Retorna o filho a esquerda do nó i
        """

        if self.nos >= 2*i:
            return self.heap[2 * i - 1]
        return 'Esse nó não tem filho a esquerda'

    def filho_direita(self, i):
        """
            Retorna o filho a direita do nó i
        """

        if self.nos >= 2*i + 1:
            return self.heap[2 * i + 1 - 1]
        return 'Esse nó não tem filho a direita'

    def pai(self, i):
        """
            Retorna o pai do nó i
        """

        return self.heap[i // 2]


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
