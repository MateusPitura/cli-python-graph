import networkx as nx

def read_graph(fname):
    try:
        f = open(fname, "r")
    except:
        raise
    g = nx.Graph()
    for line in f:
        if line[0] == 'c':
            continue
        if line[0] == 'p':
            scan = line.split()
            n = int(scan[2]) # Quantidade de nodes
            m = int(scan[3]) # Quantidade de vertices
            g.add_nodes_from(range(n))
        if line[0] in 'ae':
            scan = line.split()
            u = int(scan[1])-1
            v = int(scan[2])-1
            # print(f"e {u} {v}")
            if not g.has_edge(u,v): # u e v representam uma ligação entre dois vértices
                g.add_edge(u, v)
    # print(f'Read dimacs graph with {g.number_of_nodes()} node and {g.number_of_edges()} edges')
    f.close()
    return g
