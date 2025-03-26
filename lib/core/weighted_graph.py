from random import randint, choice
from lib.core.graph import Graph
from lib.graph_property_checker.connected_checker import ConnectedChecker

class WeightedGraph(Graph):
    def __init__(self, num_vertices: int):
        super().__init__(num_vertices)
        self.edges = {}  # {(u, v): weight}
    
    def add_edge(self, u: int, v: int, weight: int):
        if u != v:
            self.edges[(u, v)] = weight
            self.edges[(v, u)] = weight
    
    def remove_edge(self, u: int, v: int):
        self.edges.pop((u, v), None)
        self.edges.pop((v, u), None)
    
    def get_edges(self):
        return [(u, v, w) for (u, v), w in self.edges.items() if u < v]
    
    def edge_exists(self, u: int, v: int):
        return (u, v) in self.edges
    
    def vertex_degree(self, u: int):
        return sum(1 for (x, _) in self.edges.keys() if x == u)
    
    def vertex_neighbors(self, u: int):
        return [v for (x, v) in self.edges.keys() if x == u]