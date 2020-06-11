from typing import Hashable, List
import networkx as nx


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    visited = list() # список посещенных вершин
    queue = [start_node] # очередь для посещения (начиная со стартовой ноды)

    # рекурсивная функция поиска еще не посещенных нод
    def search_rec():
        current_node = queue[-1] # текукщя нода = последня из очереди
        del queue[-1] # удаляем эту ноду из очереди
        visited.append(current_node) # и записываем ее в список посещенных

        if len(visited) == len(list(g)): # если посетили все ноды из графа, то возвращаем список
            return visited

        for item in g.adj.get(current_node): # если соседней ноды нет в очереди и в списке посещенных,
                                             # то добавляем эту ноду в очередь
            if item not in visited and item not in queue:
                queue.append(item)

        return search_rec()

    search_rec()

    return visited


def test():
    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFG")
    graph.add_edges_from([
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'D'),
        ('B', 'E'),
        ('C', 'F'),
        ('E', 'G'),
    ])
    return graph

if __name__ == '__main__':
    dfs(test(), 'A')