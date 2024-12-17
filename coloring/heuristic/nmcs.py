"""
    Esse código implementa o algoritmo de NMCS e também exibe uma animação da
	árvore de recursão, pode ser encontrado no artigo Monte Carlos Graph Coloring
"""

import math
import random
import heapq
import copy
from visualiser.visualiser import Visualiser as vs
import read_dimacs


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
        print(self.queue)

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

    sequence = []
    while True:
        if state.is_terminal():  # Até todos os vértices serem coloridos
            return score(state), sequence

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


@vs(
    # Argumentos que não serão mostrados
    ignore_args=["state", "policy", "vertex_queue"],
    show_return_value=False,  # Não mostrar o valor de retorno
    show_argument_name=False,  # Não mostra o nome do argumento
    node_properties_kwargs={"shape": "record", "color": "#f57542",
                            "style": "filled", "fillcolor": "grey"}  # Estilização
)
def nmcs(state, policy, vertex_queue, level):
    """
        Algoritmo em si do NMCS
    """

    if level == 0:
        return playout(state, policy, vertex_queue)

    best_score = float('-inf')
    best_sequence = []

    while not state.is_terminal():
        possible_moves = state.get_possible_moves(vertex_queue.pop())
        for move in possible_moves:
            state.play(move)
            current_score, sequence = nmcs(
                state=copy.deepcopy(state),
                policy=policy,
                vertex_queue=copy.deepcopy(vertex_queue),
                level=level - 1
            )
            if current_score > best_score:
                best_score = current_score
                best_sequence = sequence + [move]
    return best_score, best_sequence


def main():
    """
        Cria um grafo a partir de um arquivo DIMACS
        Colore usando o algoritmo de NCMS, irá gerar um PNG e GIF da árvore de recursão
        Chame com python3 nmcs.py
        TODO: também exibir a animação de coloração
    """

    graph = read_dimacs.read_graph('instances/sample.col')
    level = 1  # Mude a linha 188 para aumentar os níveis de recursão, irá demorar mais
    state = State(graph, level)

    # Irá retornar {(0, 0): 0, ..., (0, 2): 0}, onde o 1º elemento é o vértice
    # e o 2º a cor, cada tupla terá a mesma probabilidade de ser escolhida
    policy = {
        (vertex, color): 0
        for vertex in state.graph.nodes()
        for color in range(state.max_colors)
    }

    vertex_queue = VertexQueue(graph)
    print(f'nmcs_recursiontree_output/nmcs-level={level}', nmcs(
        state=state,
        policy=policy,
        vertex_queue=vertex_queue,
        level=3
    ))
    vs.make_animation(f'nmcs_recursiontree_output/nmcs-level={level}.gif')


if __name__ == "__main__":
    main()
