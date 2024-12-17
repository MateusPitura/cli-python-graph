"""
    Esse código realiza o playout e também exibe uma animação,
    o playout é a coloração em si do grafo
"""


import heapq
import math
import random
import networkx as nx
import read_dimacs
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

sequence = []


class VertexQueue:
    """
        Cria uma fila de prioridade máxima pelo grau para os vértices
        TODO: teria que usar DSATUR também, porém a fila deveria alterar enquanto o grafo é colorido
    """

    def __init__(self, graph):
        self.graph = graph
        self.queue = []
        for vertex in graph.nodes():
            # heapq é uma fila de prioriedade mínima, por isso "-" na frente
            heapq.heappush(self.queue, (-graph.degree(vertex), vertex))

    def pop(self):
        """
            Remove e retorna o vértice com maior grau, [1] pois pega o vértice, [0] seria o grau
        """

        return heapq.heappop(self.queue)[1]


class State:
    """
        Métodos para a coloração do grafo
    """

    def __init__(self, graph, max_colors):
        """
            Cria um dicionário {v: None, ..., v: None}, cada chave é um vértice e seu valor a cor
        """

        self.graph = graph
        self.max_colors = max_colors
        self.coloring = {vertex: None for vertex in graph.nodes()}

    def is_terminal(self):
        """
            Verifica se todos os vértices já foram coloridos
        """

        return all([color is not None for color in self.coloring.values()])

    def is_color_valid(self, vertex, color):
        """
            Verifica se uma cor é válida seguindo a ideia básica do problema da coloração
        """

        for neighbor in self.graph.neighbors(vertex):
            if self.coloring[neighbor] == color:
                return False

        return True

    def get_possible_moves(self, vertex):
        """
            Retorna as cores/movimentos possíveis para um vértice
            Aqui retorno a primeira cor caso não haja movimentos válidos
            TODO: experimentar com outros retornos
        """

        possible_moves = []
        if self.coloring[vertex] is None:
            # Retorna [(1, 0), (1, 1), (1, 2), (1, 3)] onde a 1ª posição é o vértice e a 2ª a cor
            possible_moves = [
                (vertex, color)
                for color in range(self.max_colors)
                if self.is_color_valid(vertex, color)
            ]

        if len(possible_moves) > 0:
            return possible_moves

        return [(vertex, 0)]

    def play(self, move):
        """
            Realiza uma coloração de fato de um vértice
        """

        vertex, color = move
        self.coloring[vertex] = color


def playout(state, policy, vertex_queue):
    """
        Realiza a coloração toda do grafo
    """

    sequence.clear()  # Deixa vazio o array, para limpar quanto for chamado em sequência
    while not state.is_terminal():  # Até todos os vértices serem coloridos
        # Pega os movimentos possíveis para o maior vértice
        possible_moves = state.get_possible_moves(vertex_queue.pop())

        # math.exp calcula a constante de euler elevada a x, que no geral será 0, resultadno em 1
        sum_total = sum([math.exp(policy[move]) for move in possible_moves])

        # Retorna algo como [0.25, 0.25, 0.25, 0.25]
        move_probabilities = [
            math.exp(policy[move]) / sum_total for move in possible_moves
        ]

        # Escolhe aleatoriamente um movimento baseado nas probabilidades,
        # como serão iguais, qualquer um pode ser escolhido igualmente
        chosen_move = random.choices(
            possible_moves, weights=move_probabilities
        )[0]

        state.play(chosen_move)
        sequence.append(chosen_move)
        yield state.coloring


def get_final_result(state):
    """
        Retorna o score e a sequência de coloração
    """

    return score(state), sequence


def score(state):
    """
        Verifica quantos conflitos existem no grafo, isto é, 
        quantos vértices adjascentes são coloridos com as mesmas cores
    """

    inconsistent_edges = 0
    # edge é uma tupla em que o 1º elemento é o vértice de origem e o 2º o vértice de destino
    for edge in state.graph.edges():
        if state.coloring[edge[0]] == state.coloring[edge[1]]:
            inconsistent_edges += 1
    # Maior o score melhor, se o score for igual a quantidade de vértices então achamos uma solução
    return state.graph.number_of_edges() - inconsistent_edges


def animate_coloring(graph, frames_function):
    """
        Animação de coloração
    """

    fig, ax = plt.subplots()
    pos = nx.spring_layout(graph)

    def update(coloring):
        ax.clear()
        colors = [coloring.get(node, 'grey') for node in graph.nodes()]
        nx.draw(graph, pos, node_color=colors, with_labels=True,
                node_size=500, ax=ax)
        ax.set_title("Playout")

    anim = FuncAnimation(
        fig, update, frames=frames_function(), interval=1000, repeat=False
    )
    anim.resume()
    plt.show()


def main():
    """
        Cria um grafo a partir de um arquivo DIMACS
        Colore e exibe a animação, chame com python3 playout_animate.py
    """

    graph = read_dimacs.read_graph('instances/sample.col')
    state = State(graph, 3)

    # Irá retornar {(0, 0): 0, ..., (0, 2): 0}, onde o 1º elemento é o vértice
    # e o 2º a cor, cada tupla terá a mesma probabilidade de ser escolhida
    policy = {
        (vertex, color): 0
        for vertex in state.graph.nodes()
        for color in range(state.max_colors)
    }
    vertex_queue = VertexQueue(graph)

    animate_coloring(graph, lambda: playout(state, policy, vertex_queue))

    # Irá retornar algo como (10, [(4, 2), (1, 2), (2, 1), (3, 0), (5, 3), (0, 0), (6, 1)]),
    # onde 10 seria o score e as tuplas os vértices coloridos
    print('playout', get_final_result(state))


if __name__ == "__main__":
    main()
