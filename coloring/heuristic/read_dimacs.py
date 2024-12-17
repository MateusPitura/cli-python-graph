"""
    Este código consegue ler arquivos do tipo .col e criar grafos a partir deles,
    esses arquivos contém representações de grafos em formato DIMACS
"""

import networkx as nx


def read_graph(fname):
    """
        Recebe o arquivo .col, para usar descomente a linha 
        28, 31, 32 e 37 e chame com python3 read_dimacs.py
    """

    with open(fname, "r", encoding="utf-8") as file:
        g = nx.Graph()
        for line in file:
            if line[0] == 'c':  # Representa um comentário
                continue
            if line[0] == 'p':
                scan = line.split()
                n = int(scan[2])  # Quantidade de nodes
                # m = int(scan[3])  # Quantidade de vertices
                g.add_nodes_from(range(n))
            if line[0] in 'ae':
                scan = line.split()
                u = int(scan[1])-1
                v = int(scan[2])-1
                # print(f"e {u} {v}")
                if not g.has_edge(u, v):  # u e v representam uma ligação entre dois vértices
                    g.add_edge(u, v)
        # print(
        #     f'Read dimacs graph with {g.number_of_nodes()} node {g.number_of_edges()} edges')
        file.close()
        return g


# read_graph("instances/sample.col")
