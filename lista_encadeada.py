class Node:

    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def getValue(self):
        return self.valor
    
    def setNext(self, proximo):
        self.proximo = proximo

    def getNext(self):
        return self.proximo
    
node1 = Node(4)
node2 = Node(7)

node1.setNext(node2)

print(node1.getValue())
print(node2.getValue())

print(node1.getNext().getValue())