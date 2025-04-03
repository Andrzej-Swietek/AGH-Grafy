import heapq
import copy
from collections import defaultdict
from lib.core.directed_graph import DirectedGraph
from lib.finders.bellmanford_finder import BellmanFordFinder
from lib.finders.dijkstra_finder import DijkstraFinder
class JohnsonAlgorithm:
    def __init__(self, graph: DirectedGraph):
        self.original_graph = graph
        self.V = graph.get_num_vertices()
        
    def johnson(self):
        temp_graph = copy.deepcopy(self.original_graph)
        temp_graph.num_vertices += 1
        new_vertex = self.V
        
        for v in range(self.V):
            temp_graph.add_edge(new_vertex, v, 0)
            
        try:
            h_distances, _ = BellmanFordFinder.find_shortest_paths(temp_graph, new_vertex)
        except ValueError as e:
            return str(e)
            
        for u in range(temp_graph.num_vertices):
            for v, weight in temp_graph.vertex_out_neighbors_weights(u):
                if h_distances[u] + weight < h_distances[v]:
                    raise ValueError("Graph contains a negative weight cycle")
        
        h = {v: h_distances[v] for v in range(self.V)}
        
        reweighted_graph = DirectedGraph(self.V)
        for (u, v), w in self.original_graph.edges.items():
            new_w = w + h[u] - h[v]
            reweighted_graph.add_edge(u, v, new_w)
            
        all_pairs = {}
        for u in range(self.V):
            distances, _ = DijkstraFinder.find_shortest_paths(reweighted_graph, u)
            all_pairs[u] = {
                v: (distances[v] + h[v] - h[u] if distances[v] != float('inf') else float('inf')) 
                for v in range(self.V)
            }
            
        return all_pairs