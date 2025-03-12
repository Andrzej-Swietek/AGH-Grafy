from typing import List, Dict, Tuple
from lib.core.graph import Graph

class IncidenceMatrixGraph(Graph):
    """
    Implementacja grafu przy użyciu macierzy incydencji.
    """
    
    def __init__(self, num_vertices: int):
        super().__init__(num_vertices)
        self.edges = []
    
    def add_edge(self, u: int, v: int):
        self.edges.append((u, v))
    
    def remove_edge(self, u: int, v: int):
        if (u, v) in self.edges:
            self.edges.remove((u, v))
        elif (v, u) in self.edges:
            self.edges.remove((v, u))
    
    def get_edges(self) -> List[Tuple[int, int]]:
        return self.edges
    
    def to_adjacency_matrix(self) -> List[List[int]]:
        matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]
        for u, v in self.edges:
            matrix[u][v] = 1
            matrix[v][u] = 1
        return matrix
    
    def to_incidence_matrix(self) -> List[List[int]]:
        incidence_matrix = [[0] * len(self.edges) for _ in range(self.num_vertices)]
        for edge_idx, (u, v) in enumerate(self.edges):
            incidence_matrix[u][edge_idx] = 1
            incidence_matrix[v][edge_idx] = 1
        return incidence_matrix
    
    def to_adjacency_list(self) -> Dict[int, List[int]]:
        adjacency_list = {i: [] for i in range(self.num_vertices)}
        for u, v in self.edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
        return adjacency_list
