class AdjacencyListGraph(Graph):
    """
    Implementacja grafu przy użyciu listy sąsiedztwa.
    """
    
    def __init__(self, num_vertices: int):
        super().__init__(num_vertices)
        self.adjacency_list = {i: [] for i in range(num_vertices)}
    
    def add_edge(self, u: int, v: int):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)
    
    def remove_edge(self, u: int, v: int):
        self.adjacency_list[u].remove(v)
        self.adjacency_list[v].remove(u)
    
    def get_edges(self) -> List[Tuple[int, int]]:
        edges = []
        for u in self.adjacency_list:
            for v in self.adjacency_list[u]:
                if u < v:
                    edges.append((u, v))
        return edges
    
    def to_adjacency_matrix(self) -> List[List[int]]:
        matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]
        for u in self.adjacency_list:
            for v in self.adjacency_list[u]:
                matrix[u][v] = 1
        return matrix
    
    def to_incidence_matrix(self) -> List[List[int]]:
        edges = self.get_edges()
        incidence_matrix = [[0] * len(edges) for _ in range(self.num_vertices)]
        
        for edge_idx, (u, v) in enumerate(edges):
            incidence_matrix[u][edge_idx] = 1
            incidence_matrix[v][edge_idx] = 1
        
        return incidence_matrix
    
    def to_adjacency_list(self) -> Dict[int, List[int]]:
        return self.adjacency_list
