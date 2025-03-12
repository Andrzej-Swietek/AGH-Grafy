from lib.core.graph import Graph
from lib.core.adjacency_matrix_graph import AdjacencyMatrixGraph
from lib.core.incidence_matrix_graph import IncidenceMatrixGraph
from lib.core.adjacency_list_graph import AdjacencyListGraph


class GraphFactory:
    @staticmethod
    def create_graph(graph_type: str, num_vertices: int) -> Graph:
        if graph_type == "adjacency_matrix":
            return AdjacencyMatrixGraph(num_vertices)
        elif graph_type == "incidence_matrix":
            return IncidenceMatrixGraph(num_vertices)
        elif graph_type == "adjacency_list":
            return AdjacencyListGraph(num_vertices)
        else:
            raise ValueError("Unknown graph type")
