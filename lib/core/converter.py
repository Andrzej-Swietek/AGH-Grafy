from typing import List, Dict, Tuple, Type

from lib.core.graph import Graph
from lib.core.adjacency_list_graph import AdjacencyListGraph
from lib.core.adjacency_matrix_graph import AdjacencyMatrixGraph
from lib.core.incidence_matrix_graph import IncidenceMatrixGraph


class GraphConverter:
    @classmethod
    def from_adjacency_matrix(cls: Type['Graph'], matrix: List[List[int]]) -> 'Graph':
        num_vertices = len(matrix)
        graph = AdjacencyMatrixGraph(num_vertices)
        for i in range(num_vertices):
            for j in range(num_vertices):
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
            elif len(vertices) > 2:
                print(f"Warning: Edge {edge_idx} has more than 2 vertices in incidence matrix.")

        return graph

    @classmethod
    def from_adjacency_list(cls: Type['Graph'], adjacency_list: Dict[int, List[int]]) -> 'Graph':
        num_vertices = max(adjacency_list.keys()) + 1
        graph = AdjacencyListGraph(num_vertices)

        for u, neighbors in adjacency_list.items():
            if u not in graph.adjacency_list:
                graph.adjacency_list[u] = []
            for v in neighbors:
                if v not in graph.adjacency_list:
                    graph.adjacency_list[v] = []
                graph.add_edge(u, v)

        return graph
