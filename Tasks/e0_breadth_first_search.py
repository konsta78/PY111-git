from typing import Hashable, List
import networkx as nx
#import matplotlib.pyplot as plt
from collections import deque


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    visited = {node: False for node in g.nodes} # посещенные вершины
    visited[start_node] = True # записали стартовую ноду в список посещенных
    queue = [start_node] # создали очередь для посещения
    list_out = [] # список посещенных нод

    while not all(visited.values()): # пока все ноды не будут посещены

        current_node = queue[0] # берем первую ноду из очереди
        del queue[0] # и удаляем эту ноду из очереди

        list_out.append(current_node) # добавляем текущую ноду в список посещенных

        for item in g.adj.get(current_node):
            if item not in list_out and item not in queue:
                queue.append(item) # добавляем в очередь соседние ноды, если их еще нет в очереди

        visited[current_node] = True # помечаем ноду как посещенную

    return list_out # возвращаем список с порядком посещения нод



# def print_graph(graph):
#     pos = nx.spring_layout(graph)
#     labels = {node: node for node in graph.nodes()}
#     nx.draw_networkx_nodes(graph, pos)
#     nx.draw_networkx_edges(graph, pos)
#     nx.draw_networkx_labels(graph, pos, labels, font_size=16)
#     plt.show()

def test_graph():
    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFGHIJ")
    graph.add_edges_from([
        ('A', 'B'),
        ('A', 'F'),
        ('B', 'G'),
        ('F', 'G'),
        ('G', 'C'),
        ('G', 'H'),
        ('G', 'I'),
        ('C', 'H'),
        ('I', 'H'),
        ('H', 'D'),
        ('H', 'E'),
        ('H', 'J'),
        ('E', 'D'),
    ])

    visited = {node: False for node in graph.nodes} # посещенные вершины
    start_node = list(graph.nodes())[0] # начальная нода (в нашем случае - 'A')
    visited[start_node] = True # записали стартовую ноду в список посещенных
    queue = [start_node] # создали очередь для посещения
    list_out = [] # список посещенных нод
    print(graph['G'])

    print(graph.adj.get('G'))
    print([v for v in graph.adj.get('G')])

    while not all(visited.values()): # пока все ноды не будут посещены

        current_node = queue[0] # берем первую ноду из очереди
        del queue[0] # и удаляем эту ноду из очереди
        print("Current node: ", current_node)

        list_out.append(current_node) # добавляем текущую ноду в список посещенных
        print("List of visited:", list_out)

        for item in graph.adj.get(current_node):
            if item not in list_out and item not in queue:
                queue.append(item) # добавляем в очередь соседние ноды, если их еще нет в очереди
        print("Queue: ", queue)

        visited[current_node] = True

    return list_out

    print(list_out)


if __name__ == '__main__':
    test_graph()