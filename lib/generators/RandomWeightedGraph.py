from random import randint, choice
from lib.core.weighted_graph import WeightedGraph
from lib.graph_property_checker.connected_checker import ConnectedChecker

class RandomWeightedGraphGenerator:
    def __init__(self, num_vertices: int, min_weight: int, max_weight: int):
        self.num_vertices = num_vertices
        self.min_weight = min_weight
        self.max_weight = max_weight
    
    def generate(self) -> WeightedGraph:
        graph = WeightedGraph(self.num_vertices)
        
        vertices = list(range(self.num_vertices))
        connected = {vertices.pop(0)}
        while vertices:
            u = choice(list(connected))
            v = vertices.pop()
            weight = randint(self.min_weight, self.max_weight)
            graph.add_edge(u, v, weight)
            connected.add(v)
        
        num_extra_edges = randint(self.num_vertices, self.num_vertices * 2)
        while len(graph.get_edges()) < num_extra_edges:
            u, v = randint(0, self.num_vertices - 1), randint(0, self.num_vertices - 1)
            if u != v and not graph.edge_exists(u, v):
                weight = randint(self.min_weight, self.max_weight)
                graph.add_edge(u, v, weight)
        
        return graph
