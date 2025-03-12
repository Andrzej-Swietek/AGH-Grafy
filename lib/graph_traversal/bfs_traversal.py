class BFSVisitor(GraphTraversal):
    def traverse(self, graph: Graph, start_vertex: int, callback: Callable[[int], None]):
        visited = set()
        queue = [start_vertex]
        
        while queue:
            v = queue.pop(0)
            if v not in visited:
                visited.add(v)
                callback(v)
                queue.extend(neighbor for neighbor in graph.to_adjacency_list().get(v, []) if neighbor not in visited)