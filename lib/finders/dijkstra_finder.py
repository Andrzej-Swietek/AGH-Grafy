import heapq
from lib.core.graph import Graph

class DijkstraFinder:
    @staticmethod
    def find_shortest_paths(graph: Graph, start_vertex: int):
        num_vertices = graph.num_vertices
        distances = {v: float('inf') for v in range(num_vertices)}
        predecessors = {v: None for v in range(num_vertices)}
        distances[start_vertex] = 0

        priority_queue = [(0, start_vertex)]
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in DijkstraFinder.get_neighbors_with_weights(graph, current_vertex):
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances, predecessors

    @staticmethod
    def get_neighbors_with_weights(graph: Graph, vertex: int):
        """ Extracts neighbors and assigns weights correctly for Graph and WeightedGraph. """
        if hasattr(graph, 'edges'):  # If it's a WeightedGraph
            return [(v, graph.edges.get((vertex, v), float('inf'))) for v in graph.vertex_neighbors(vertex)]
        else:  # If it's a normal Graph (unweighted)
            return [(v, 1) for v in graph.vertex_neighbors(vertex)]

    @staticmethod
    def reconstruct_path(predecessors, start_vertex, end_vertex):
        path = []
        current = end_vertex
        while current is not None:
            path.append(current)
            current = predecessors[current]
        path.reverse()
        return path if path and path[0] == start_vertex else []
