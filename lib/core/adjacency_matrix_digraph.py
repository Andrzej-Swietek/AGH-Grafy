from typing import List, Dict, Tuple
from lib.core.graph import Graph
from lib.core.weighted_digraph import WeightedDigraph


class AdjacencyMatrixDigraph(Graph):
    """
    Implementacja digrafu przy użyciu macierzy sąsiedztwa.
    """

    def __init__(self, num_vertices: int):
        super().__init__(num_vertices)
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u: int, v: int):
        self.matrix[u][v] = 1

    def remove_edge(self, u: int, v: int):
        self.matrix[u][v] = 0

    def get_edges(self) -> List[Tuple[int, int]]:
        edges = []
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if self.matrix[i][j] == 1:
                    edges.append((i, j))
        return edges
    
    def edge_exists(self, u: int, v: int) -> bool:
        return self.matrix[u][v] == 1
    
    def vertex_degree(self, u: int) -> int:
        return sum(self.matrix[u])
    
    def vertex_neighbors(self, u: int) -> List[int]:
        return [v for v in range(self.num_vertices) if self.matrix[u][v] == 1 and u != v]

    def to_adjacency_matrix(self) -> List[List[int]]:
        return self.matrix

    def to_incidence_matrix(self) -> List[List[int]]:
        edges = self.get_edges()
        incidence_matrix = [[0] * len(edges) for _ in range(self.num_vertices)]

        for edge_idx, (u, v) in enumerate(edges):
            incidence_matrix[u][edge_idx] = 1
            incidence_matrix[v][edge_idx] = -1

        return incidence_matrix

    def to_adjacency_list(self) -> Dict[int, List[int]]:
        adjacency_list = {i: [] for i in range(self.num_vertices)}
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if self.matrix[i][j] == 1:
                    adjacency_list[i].append(j)
        return adjacency_list

    def convert_to_weighted(self) -> WeightedDigraph:
        graph = WeightedDigraph(self.num_vertices)
        for edge in self.get_edges():
            graph.add_edge(edge[0], edge[1], 0)
        return graph
    