from typing import Callable

from lib.core.graph import Graph
from lib.graph_traversal.graph_traversal import GraphTraversal


class DFSVisitor(GraphTraversal):
    def traverse(self, graph: Graph, start_vertex: int, callback: Callable[[int], None]):
        visited = set()

        def dfs(v):
            if v in visited:
                return
            visited.add(v)
            callback(v)
            for neighbor in graph.vertex_neighbors(v):
                dfs(neighbor)

        dfs(start_vertex)
