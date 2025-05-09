from typing import List
from lib.core.weighted_digraph import WeightedDigraph

#BellmanFord Algorithm
class ShortestPathFinder:
    @staticmethod
    def find(graph: WeightedDigraph, source: int = 0) -> List[int] | None:
        n = graph.num_vertices
        ds = [float('inf')] * n
        ds[source] = 0

        for _ in range(n - 1):
            for (u, v), weight in graph.edges.items():
                ShortestPathFinder._relax(u, v, weight, ds)

        for (u, v), weight in graph.edges.items():
            if ds[u] + weight < ds[v]:
                print("Negative-weight cycle detected.")
                return None
        
        ShortestPathFinder._print(ds, source)
        return ds

    @staticmethod
    def _relax(u: int, v: int, weight: float, ds: List[float]):
        if ds[u] + weight < ds[v]:
            ds[v] = ds[u] + weight

    @staticmethod
    def _print(ds: List[int], source: int):
        print(f"From source {source}: ")
        for v, d in enumerate(ds):
            if d == float('inf'):
                print(f"No path to {v}")
            else:
                print(f"Shortest path to {v}: {d}")


