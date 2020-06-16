from typing import Hashable, Mapping, Union
import networkx as nx


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """
    print(g, starting_node)
    return dict()


def test():
    g = nx.DiGraph()
    g.add_nodes_from("ABCDEFG")
    g.add_weighted_edges_from([
        ("A", "B", 1),
        ("B", "C", 3),
        ("C", "E", 4),
        ("E", "F", 3),
        ("B", "E", 8),
        ("C", "D", 1),
        ("D", "E", 2),
        ("B", "D", 2),
        ("G", "D", 1),
        ("D", "A", 2),
    ])
    way = {node: float('inf') for node in g.nodes()}
    print(way)
    #start_node = list(g.nodes())[0]
    start_node = 'B'
    visited = {node: False for node in g.nodes}

    for item in g.adj.get(start_node):
        if g[start_node][item]['weight'] < way[start_node]:
            way[item] = g[start_node][item]['weight']
    visited[start_node] = True
    print(way)

    # for item in g.edges():
    #     if 'A' in item:
    #         print(item)
            #print('Node: ', item, 'Weight', g['A'][item]['weight'])




if __name__ == '__main__':
    test()