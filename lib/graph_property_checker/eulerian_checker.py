from lib.graph_property_checker.graph_property_checker import GraphPropertyChecker
from lib.core.graph import Graph
from lib.graph_property_checker.connected_checker import ConnectedChecker

class EulerianChecker(GraphPropertyChecker):
    @staticmethod
    def check(graph: Graph) -> bool:
        return ConnectedChecker.check(graph) and all(graph.vertex_degree(v) % 2 == 0 for v in range(graph.num_vertices))