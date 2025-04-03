import heapq
from lib.core.directed_graph import DirectedGraph

class BellmanFordFinder:
    @staticmethod
    def find_shortest_paths(graph: DirectedGraph, start_vertex: int):
        num_vertices = graph.num_vertices
        distances = {v: float('inf') for v in range(num_vertices)}
        predecessors = {v: None for v in range(num_vertices)}
        distances[start_vertex] = 0

        for _ in range(num_vertices - 1):
            for u in range(num_vertices):
                for neighbor, weight in graph.vertex_out_neighbors_weights(u):
                    if distances[u] + weight < distances[neighbor]:
                        distances[neighbor] = distances[u] + weight
                        predecessors[neighbor] = u

        for u in range(num_vertices):
            for neighbor, weight in graph.vertex_out_neighbors_weights(u):
                if distances[u] + weight < distances[neighbor]:
                    print("Graph contains a negative weight cycle")
                
        return distances, predecessors

