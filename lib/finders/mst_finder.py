import heapq
from lib.core.graph import Graph

class MSTFinder:
    @staticmethod
    def find_minimum_spanning_tree(graph: Graph):
        num_vertices = graph.num_vertices
        if num_vertices == 0:
            return [], 0  # Empty graph case

        mst_edges = []
        
        total_weight = 0
        visited = set()
        priority_queue = [(0, 0, None)]

        while len(visited) < num_vertices and priority_queue:
            weight, vertex, parent = heapq.heappop(priority_queue)

            if vertex in visited:
                continue

            visited.add(vertex)
            if parent is not None:
                mst_edges.append((parent, vertex, weight))
                total_weight += weight

            for neighbor, edge_weight in graph.vertex_neighbors_weights(vertex):
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (edge_weight, neighbor, vertex))

        return mst_edges, total_weight
