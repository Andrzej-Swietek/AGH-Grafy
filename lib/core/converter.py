from typing import List, Dict, Tuple, Type
from lib.core.graph import Graph

class GraphConverter:
    @classmethod
    def from_adjacency_matrix(cls: Type['Graph'], matrix: List[List[int]]) -> 'Graph':
        num_vertices = len(matrix)
        graph = AdjacencyMatrixGraph(num_vertices)
        for i in range(num_vertices):
            for j in range(i + 1, num_vertices):
                if matrix[i][j] == 1:
                    graph.add_edge(i, j)
        return graph
    
    @classmethod
    def from_incidence_matrix(cls: Type['Graph'], matrix: List[List[int]]) -> 'Graph':
        num_vertices = len(matrix)
        num_edges = len(matrix[0]) if matrix else 0
        graph = IncidenceMatrixGraph(num_vertices)
        for edge_idx in range(num_edges):
            vertices = [i for i in range(num_vertices) if matrix[i][edge_idx] == 1]
            if len(vertices) == 2:
                graph.add_edge(vertices[0], vertices[1])
        return graph
    
    @classmethod
    def from_adjacency_list(cls: Type['Graph'], adjacency_list: Dict[int, List[int]]) -> 'Graph':
        num_vertices = len(adjacency_list)
        graph = AdjacencyListGraph(num_vertices)
        for u, neighbors in adjacency_list.items():
            for v in neighbors:
                if u < v:
                    graph.add_edge(u, v)
        return graph
