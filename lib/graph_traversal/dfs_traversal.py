class DFSVisitor(GraphTraversal):
    def traverse(self, graph: Graph, start_vertex: int, callback: Callable[[int], None]):
        visited = set()
        
        def dfs(v):
            if v in visited:
                return
            visited.add(v)
            callback(v)
            for neighbor in graph.to_adjacency_list().get(v, []):
                dfs(neighbor)
        
        dfs(start_vertex)