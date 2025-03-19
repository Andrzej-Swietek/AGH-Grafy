from copy import deepcopy

from lib.core.graph import Graph
from lib.graph_traversal.dfs_traversal import DFSVisitor


class BridgeChecker:
    @staticmethod
    def is_bridge(graph: Graph, u: int, v: int) -> bool:
        """
        Sprawdza, czy podana krawędź jest mostem w grafie.
        """
        visited = set()
        DFSVisitor().traverse(graph, u, lambda u: visited.add(u))

        graph.remove_edge(u, v)

        visited_after_removal = set()
        DFSVisitor().traverse(graph, u, lambda u: visited_after_removal.add(u))

        graph.add_edge(u, v)

        return len(visited) != len(visited_after_removal)
