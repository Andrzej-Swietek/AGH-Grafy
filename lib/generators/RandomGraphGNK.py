from lib.core.graph import Graph

class RandomGraphGNK(RandomGraphGenerator):
    def __init__(self, num_vertices: int, num_edges: int):
        self.num_vertices = num_vertices
        self.num_edges = num_edges
    
    def generate(self) -> Graph:
        graph = AdjacencyMatrixGraph(self.num_vertices)
        edges = set()
        while len(edges) < self.num_edges:
            u, v = random.sample(range(self.num_vertices), 2)
            if (u, v) not in edges and (v, u) not in edges:
                graph.add_edge(u, v)
                edges.add((u, v))
        return graph
