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