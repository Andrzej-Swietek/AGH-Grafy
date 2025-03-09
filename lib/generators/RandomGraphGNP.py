class RandomGraphGNP(RandomGraphGenerator):
    def __init__(self, num_vertices: int, probability: float):
        self.num_vertices = num_vertices
        self.probability = probability
    
    def generate(self) -> Graph:
        graph = AdjacencyMatrixGraph(self.num_vertices)
        for i in range(self.num_vertices):
            for j in range(i + 1, self.num_vertices):
                if random.random() < self.probability:
                    graph.add_edge(i, j)
        return graph
