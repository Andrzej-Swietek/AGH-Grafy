import random
from lib.core.graph import Graph

class DirectedGraph(Graph):
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.edges = {}  # {(u, v): weight}
    
    def add_edge(self, u: int, v: int, weight: int):
        if u != v:
            self.edges[(u, v)] = weight
    
    def remove_edge(self, u: int, v: int):
        self.edges.pop((u, v), None)
    
    def get_edges(self):
        return [(u, v, w) for (u, v), w in self.edges.items()]
    
    def get_num_vertices(self):
        return self.num_vertices
    
    def edge_exists(self, u: int, v: int):
        return (u, v) in self.edges
    

    def vertex_degree(self, v: int):
        return sum(1 for (_, x) in self.edges.keys() if x == v)
    
    def vertex_out_degree(self, u: int):
        return sum(1 for (x, _) in self.edges.keys() if x == u)
    

    def vertex_neighbors(self, v: int):
        return [u for (u, x) in self.edges.keys() if x == v]
    
    def vertex_out_neighbors(self, u: int):
        return [v for (x, v) in self.edges.keys() if x == u]
    
    def vertex_neighbors_weights(self, v: int):
        return [[u, self.edges[(u, v)]] for (u, x) in self.edges.keys() if x == v]
    
    def vertex_out_neighbors_weights(self, u: int):
        return [[v, self.edges[(u, v)]] for (x, v) in self.edges.keys() if x == u]
    
    def to_adjacency_matrix(self):
        matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]
        for (u, v), w in self.edges.items():
            matrix[u][v] = w
        return matrix

    def to_adjacency_list(self):
        adj_list = {i: [] for i in range(self.num_vertices)}
        for (u, v), w in self.edges.items():
            adj_list[u].append((v, w))
        return adj_list

    def to_incidence_matrix(self):
        edge_list = list(self.edges.keys())
        matrix = [[0] * len(edge_list) for _ in range(self.num_vertices)]
        for j, (u, v) in enumerate(edge_list):
            matrix[u][j] = self.edges[(u, v)]
        return matrix
    
    def fill_with_random_weights(self, min_value: int, max_value: int):
        edges = self.get_edges()
        for (u, v, w) in edges:
            self.edges[(u, v)] = random.randint(min_value, max_value)
        return self
    
    def generate_random_strongly_connected_digraph(self, min_weight: int = -5, max_weight: int = 10):
        
        for i in range(self.num_vertices):
            self.add_edge(i, (i + 1) % self.num_vertices, random.randint(min_weight, max_weight))
        
        for u in range(self.num_vertices):
            for v in range(self.num_vertices):
                if u != v and random.random() < 0.5: 
                    weight = random.randint(min_weight, max_weight)
                    self.add_edge(u, v, weight)
