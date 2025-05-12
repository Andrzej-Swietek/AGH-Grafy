from typing import List, Dict, Tuple
from lib.core.graph import Graph
from lib.core.weighted_digraph import WeightedDigraph


class IncidenceMatrixDigraph(Graph):
    """
    Implementacja digrafu przy użyciu macierzy incydencji.
    """

    def __init__(self, num_vertices: int):
        super().__init__(num_vertices)
        self.edges = []

    def add_edge(self, u: int, v: int):
        self.edges.append((u, v))

    def remove_edge(self, u: int, v: int):
        if (u, v) in self.edges:
            self.edges.remove((u, v))

    def get_edges(self) -> List[Tuple[int, int]]:
        return self.edges
    
    def edge_exists(self, u: int, v: int) -> bool:
        return (u, v) in self.edges
    
    def vertex_degree(self, u: int) -> int:
        return sum(1 for edge in self.edges if u in edge)
    
    def vertex_neighbors(self, u: int) -> List[int]:
        return [v for edge in self.edges if u in edge for v in edge if v != u]

    def to_adjacency_matrix(self) -> List[List[int]]:
        matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]
        for u, v in self.edges:
            matrix[u][v] = 1
        return matrix

    def to_incidence_matrix(self) -> List[List[int]]:
        incidence_matrix = [[0] * len(self.edges) for _ in range(self.num_vertices)]
        for edge_idx, (u, v) in enumerate(self.edges):
            incidence_matrix[u][edge_idx] = 1
        return incidence_matrix

    def to_adjacency_list(self) -> Dict[int, List[int]]:
        adjacency_list = {i: [] for i in range(self.num_vertices)}
        for u, v in self.edges:
            adjacency_list[u].append(v)
        return adjacency_list

    def convert_to_weighted(self) -> WeightedDigraph:
        graph = WeightedDigraph(self.num_vertices)
        for edge in self.get_edges():
            graph.add_edge(edge[0], edge[1], 0)
        return graph