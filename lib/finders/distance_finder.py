import copy
from typing import List
from lib.core.weighted_digraph import WeightedDigraph
from lib.finders.shortest_path_finder import ShortestPathFinder
from lib.finders.dijkstra_finder import DijkstraFinder

#Johnson Algorithm
class DistanceFinder:
    @staticmethod
    def find(graph: WeightedDigraph) -> List[List[int]] | None:

        graph_prim = DistanceFinder._add_s(graph)
        graph_scaled_weights = copy.deepcopy(graph_prim)
        s = graph_prim.num_vertices - 1
        print(graph.num_vertices)
        print(graph_prim.num_vertices)

        ds = ShortestPathFinder.find(graph_prim, s)
        h = [0] * graph_prim.num_vertices

        if ds == None:
            print("Negative-weight cycle detected.")
            return None
        else:
            for v in range(graph_prim.num_vertices):
                h[v] = ds[v]
            
            for (u, v), weight in graph_prim.edges.items():
                graph_scaled_weights.edges[(u, v)] = weight + h[u] - h[v]
        
            D = [[0 for _ in range(graph.num_vertices)] for _ in range(graph.num_vertices)]

            for u in range(graph.num_vertices):
                du, _ = DijkstraFinder.find_shortest_paths(graph_scaled_weights, u)
                for v in range(graph.num_vertices):
                    D[u][v] = du[v] - h[u] + h[v]

            DistanceFinder._print(D)
            return D
    
    @staticmethod
    def _add_s(graph: WeightedDigraph) -> WeightedDigraph:
        graph_prim = copy.deepcopy(graph)
        s = graph.num_vertices
        for v in range(graph.num_vertices):
            graph_prim.add_edge(s, v, 0)
        graph_prim.num_vertices += 1
        return graph_prim
    
    @staticmethod
    def _print(D: List[List[int]]) -> None:
        if D is None:
            print("No distance matrix to display.")
            return

        print("Distance matrix (Johnson's algorithm result):")
        for row in D:
            print("  ".join(f"{val:5}" if val != float('inf') else "  inf" for val in row))