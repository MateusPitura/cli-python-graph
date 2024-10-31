import math
import random
import networkx as nx
import read_dimacs
import heapq
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

sequence = []

class VertexQueue: # Cria uma fila de prioridade máxima para os vértices # TODO: teria que usar DSATUR também, porém a fila deveria alterar enquanto o grafo é colorido
  def __init__(self, graph):
    self.graph = graph
    self.queue = []
    for vertex in graph.nodes():
      heapq.heappush(self.queue, (-graph.degree(vertex), vertex)) # heapq é uma fila de prioriedade mínima, por isso "-" na frente

  def pop(self):
    return heapq.heappop(self.queue)[1] # [1] pois pega o vértice, [0] seria o grau

class State:
    def __init__(self, graph, max_colors):
        self.graph = graph
        self.max_colors = max_colors
        self.coloring = {vertex: None for vertex in graph.nodes()} # Cria um dicionário do tipo {v: None, ..., v: None}, cada chave representa um vértice e seu valor a cor

    def is_terminal(self): # Verifica se todos os vértices já foram coloridos
        return all([color is not None for color in self.coloring.values()])

    def is_color_valid(self, vertex, color):
      for neighbor in self.graph.neighbors(vertex):
        if self.coloring[neighbor] == color:
          return False
      return True

    def get_possible_moves(self, vertex): # Retorna as cores/movimentos possíveis para um vértice
      if self.coloring[vertex] is None:
        possible_moves = [(vertex, color) for color in range(self.max_colors) if self.is_color_valid(vertex, color)] # Retorna [(1, 0), (1, 1), (1, 2), (1, 3)] onde a 1ª posição é o vértice e a 2ª a cor
      if(len(possible_moves) > 0):
        return possible_moves
      return [(vertex, 0)] # TODO: melhorar as cores inválidas retornadas

    def play(self, move): # Quanto de fato colore um vértice
        vertex, color = move
        self.coloring[vertex] = color

def playout(state, policy, vertex_queue):
    sequence.clear() # Deixa vazio o array, apenas para limpar quanto esse método for chamado várias vezes em sequência
    while not state.is_terminal(): # Até todos os vértices serem coloridos
        possible_moves = state.get_possible_moves(vertex_queue.pop()) # Pega os movimentos possíveis para o maior vértice

        z = sum([math.exp(policy[move]) for move in possible_moves]) # math.exp calcula a constante de euler elevada a x, que no geral será 0, resultadno em 1
        move_probabilities = [math.exp(policy[move]) / z for move in possible_moves] # Retorna algo como [0.25, 0.25, 0.25, 0.25]
        chosen_move = random.choices(possible_moves, weights=move_probabilities)[0] # Escolhe aleatoriamente um movimento baseado nas probabilidades, como serão iguais, qualquer um pode ser escolhido igualmente

        state.play(chosen_move)
        sequence.append(chosen_move)
        yield state.coloring

def get_final_result(state):
    return score(state), sequence

def score(state): # Verifica quantos conflitos existem no grafo, isto é, quantos vértices adjascentes são coloridos com as mesmas cores
    inconsistent_edges = 0
    for edge in state.graph.edges(): # edge é uma tupla em que o 1º elemento é o vértice de origem e o 2º o vértice de destino
        if state.coloring[edge[0]] == state.coloring[edge[1]]:
            inconsistent_edges += 1
    return state.graph.number_of_edges() - inconsistent_edges  # Quanto maior o score melhor, se o score for igual a quantidade de vértices então achamos uma solução

def animate_coloring(graph, frames_function):
    fig, ax = plt.subplots()
    pos = nx.spring_layout(graph)
    
    def update(coloring):
        ax.clear()
        colors = [coloring.get(node, 'grey') for node in graph.nodes()]
        nx.draw(graph, pos, node_color=colors, with_labels=True, node_size=500, cmap=plt.cm.jet, ax=ax)
        ax.set_title("Graph Coloring")

    anim = FuncAnimation(fig, update, frames=frames_function(), interval=1000, repeat=False)
    plt.show()

def main():
    graph = read_dimacs.read_graph('instances/sample') # Lê um arquivo com as características do grafo e cria uma instância com networkx
    state = State(graph, 3)
    policy = {(vertex, color): 0 for vertex in state.graph.nodes() for color in range(state.max_colors)} # Irá retornar {(0, 0): 0, ..., (0, 2): 0}, onde o 1º elemento é o vértice e o 2º a cor, cada tupla terá a mesma probabilidade de ser escolhida 
    vertex_queue = VertexQueue(graph)
    animate_coloring(graph, lambda: playout(state, policy, vertex_queue)) # TODO: retornar mais informações durante a coloração e o resultado final
    print('playout', get_final_result(state)) # Irá retornar algo como (10, [(4, 2), (1, 2), (2, 1), (3, 0), (5, 3), (0, 0), (6, 1)]), onde 10 seria o score e as tuplas os vértices coloridos

if __name__ == "__main__":
    main()
    