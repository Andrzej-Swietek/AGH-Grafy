from collections import defaultdict
from lib.core.directed_graph import DirectedGraph

class KosarajuSCC:
    def __init__(self, graph: DirectedGraph):
        self.graph = graph
        self.V = graph.get_num_vertices()
    
    def _dfs(self, v, visited, stack):
        """Performs DFS and stores finishing order."""
        visited[v] = True
        for neighbor in self.graph.vertex_out_neighbors(v):
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
        
        for i in range(self.V):
            if not visited[i]:
                self._dfs(i, visited, stack)
        
        reversed_graph = defaultdict(list)
        for (u, v), _ in self.graph.edges.items():
            reversed_graph[v].append(u)
        
        visited = {i: False for i in range(self.V)}
        sccs = []
        
        while stack:
            v = stack.pop()
            if not visited[v]:
                component = []
                self._dfs_transposed(v, visited, component, reversed_graph)
                sccs.append(component)
        
        return sccs