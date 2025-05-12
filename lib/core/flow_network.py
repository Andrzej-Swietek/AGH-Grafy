from lib.core.weighted_digraph import WeightedDigraph



class FlowNetwork(WeightedDigraph):
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.edges = {}  # {(u, v): weight}
        self.inter_layers = list[list[int]]
    
    def add_edge(self, u: int, v: int, weight: int = 0):
        if u != v:
            self.edges[(u, v)] = weight
    
    def remove_edge(self, u: int, v: int):
        self.edges.pop((u, v), None)
    
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
    
    def successors(self, u: int):
        return [v for (a, v), _ in self.edges.items() if a == u]

    def get_layers(self) -> list[list[int]]:
        return self.inter_layers