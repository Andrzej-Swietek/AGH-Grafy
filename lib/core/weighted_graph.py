import random
from lib.core.graph import Graph
class WeightedGraph(Graph):
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.edges = {}  # {(u, v): weight}
    
    def add_edge(self, u: int, v: int, weight: int):
        if u != v:
            self.edges[(u, v)] = weight
    
    def remove_edge(self, u: int, v: int):
        self.edges.pop((u, v), None)
        self.edges.pop((v, u), None)
    
    def get_edges(self):
        return [(u, v, w) for (u, v), w in self.edges.items() if u < v]
    
    def get_num_vertices(self):
        return self.num_vertices
    
    def edge_exists(self, u: int, v: int):
        return (u, v) in self.edges
    
    def vertex_degree(self, u: int):
        return sum(1 for (x, _) in self.edges.keys() if x == u)
    
    def vertex_neighbors(self, u: int):
        return [v for (x, v) in self.edges.keys() if x == u]
    
    def vertex_neighbors_weights(self, u: int):
        return [[v, self.edges[(u, v)]] for (x, v) in self.edges.keys() if x == u]
    
    def to_adjacency_matrix(self):
        matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]
        for (u, v), w in self.edges.items():
            matrix[u][v] = w
            matrix[v][u] = w
        return matrix

    def to_adjacency_list(self):
        adj_list = {i: [] for i in range(self.num_vertices)}
        for (u, v), w in self.edges.items():
            adj_list[u].append((v, w))
            adj_list[v].append((u, w))
        return adj_list

    def to_incidence_matrix(self):
        edge_list = list(self.edges.keys())
        matrix = [[0] * len(edge_list) for _ in range(self.num_vertices)]
        for j, (u, v) in enumerate(edge_list):
            matrix[u][j] = self.edges[(u, v)]
            matrix[v][j] = self.edges[(u, v)]
        return matrix
    
    def fill_with_random_edges_uniform(self, min_value: int, max_value: int):
        for u in range(self.num_vertices):
            for v in range(u + 1, self.num_vertices):
                random_int = random.randint(min_value, max_value)
                self.add_edge(u, v, random_int)
                self.add_edge(v, u, random_int)
        return