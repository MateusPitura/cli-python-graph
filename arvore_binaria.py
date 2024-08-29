class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def getValue(self):
        return self.value
    
    def setRight(self, right):
        self.right = right

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right
    
    def getLeft(self):
        return self.left

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def oberraiz(self):
        return self.raiz
    
    def insere(self, valor):
        no = Node(valor)
        if self.raiz == None:
            self.raiz = no
        else:
            no_atual = self.raiz
            no_pai = None
            while True:
                if no_atual != None:
                    no_pai = no_atual
                    if no.getValue() < no_atual.getValue():
                        no_atual = no_atual.getLeft()
                    else:
                        no_atual = no_atual.getRight()
                else:
                    if no.getValue() < no_pai.getValue():
                        no_pai.setLeft(no)
                    else:
                        no_pai.setRight(no)
                    break

    def mostraarvore(self, no_atual):
        if no_atual != None:
            self.mostraarvore(no_atual.getLeft())
            print(f'{no_atual.getValue()}', end = ' ')
            self.mostraarvore(no_atual.getRight())
                
t = ArvoreBinariaBusca()
t.insere(8)
t.insere(3)
t.insere(6)
t.insere(10)
t.insere(14)
t.insere(1)
t.insere(7)
t.insere(13)
t.insere(4)

t.mostraarvore(t.oberraiz())
