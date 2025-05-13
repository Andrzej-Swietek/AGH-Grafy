from typing import List, Dict, Tuple
from lib.core.graph import Graph
from lib.core.weighted_digraph import WeightedDigraph


class AdjacencyListDigraph(Graph):
    """
    Implementacja digrafu przy użyciu listy sąsiedztwa.
    """

    def __init__(self, num_vertices: int):
        super().__init__(num_vertices)
        self.adjacency_list = {i: [] for i in range(num_vertices)}

    def add_edge(self, u: int, v: int):
        self.adjacency_list[u].append(v)

    def remove_edge(self, u: int, v: int):
        self.adjacency_list[u].remove(v)

    def get_edges(self) -> List[Tuple[int, int]]:
        edges = []
        for u in self.adjacency_list:
            for v in self.adjacency_list[u]:
                edges.append((u, v))
        return edges

    def edge_exists(self, u: int, v: int) -> bool:
        return u in self.adjacency_list.get(v, [])
    
    def vertex_degree(self, u: int) -> int:
        return len(self.adjacency_list[u])
    
    def vertex_neighbors(self, u: int) -> List[int]:
        return self.adjacency_list[u]

    def to_adjacency_matrix(self) -> List[List[int]]:
        matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]
        for u in self.adjacency_list:
            for v in self.adjacency_list[u]:
                matrix[u][v] = 1
        return matrix

    def to_incidence_matrix(self) -> List[List[int]]:
        edges = self.get_edges()
        incidence_matrix = [[0] * len(edges) for _ in range(self.num_vertices)]

        for edge_idx, (u, v) in enumerate(edges):
            incidence_matrix[u][edge_idx] = 1
            incidence_matrix[v][edge_idx] = -1

        return incidence_matrix

    def to_adjacency_list(self) -> Dict[int, List[int]]:
        return self.adjacency_list

    def convert_to_weighted(self) -> WeightedDigraph:
        graph = WeightedDigraph(self.num_vertices)
        for edge in self.get_edges():
            graph.add_edge(edge[0], edge[1], 0)
        return graph

    