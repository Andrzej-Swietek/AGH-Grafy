from collections import defaultdict
from lib.core.weighted_graph import WeightedGraph

class KosarajuSCC:
    def __init__(self, graph: WeightedGraph):
        self.graph = graph
        self.V = graph.get_num_vertices()
    
    def _dfs(self, v, visited, stack):
        """Performs DFS and stores finishing order."""
        visited[v] = True
        for neighbor, _ in self.graph.vertex_neighbors_weights(v):
            if not visited[neighbor]:
                self._dfs(neighbor, visited, stack)
        stack.append(v)
    
    def _dfs_transposed(self, v, visited, component, reversed_graph):
        """Performs DFS on the transposed graph to collect SCC."""
        visited[v] = True
        component.append(v)
        for neighbor in reversed_graph[v]:
            if not visited[neighbor]:
                self._dfs_transposed(neighbor, visited, component, reversed_graph)
    
    def find_sccs(self):
        """Finds and returns all strongly connected components."""
        stack = []
        visited = {i: False for i in range(self.V)}
        
        # Step 1: Fill stack with vertices in order of finishing time
        for i in range(self.V):
            if not visited[i]:
                self._dfs(i, visited, stack)
        
        # Step 2: Transpose the graph
        reversed_graph = defaultdict(list)
        for (u, v), _ in self.graph.edges.items():
            reversed_graph[v].append(u)
        
        # Step 3: Process vertices in decreasing order of finish time
        visited = {i: False for i in range(self.V)}
        sccs = []
        
        while stack:
            v = stack.pop()
            if not visited[v]:
                component = []
                self._dfs_transposed(v, visited, component, reversed_graph)
                sccs.append(component)
        
        return sccs