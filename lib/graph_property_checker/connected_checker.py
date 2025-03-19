from lib.graph_property_checker.graph_property_checker import GraphPropertyChecker
from lib.core.graph import Graph
from lib.graph_traversal.dfs_traversal import DFSVisitor

class ConnectedChecker(GraphPropertyChecker):
    @staticmethod
    def check(graph: Graph) -> bool:
        """
        Sprawdza, czy graf jest spójny.
        """

        visited = set()
        DFSVisitor().traverse(graph, 0, lambda u: visited.add(u))
        return len(visited) == graph.num_vertices