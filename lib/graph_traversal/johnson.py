import heapq
import copy
from collections import defaultdict

class JohnsonAlgorithm:
    def __init__(self, graph):
        self.original_graph = graph
        self.V = graph.get_num_vertices()
        self.vertex_list = list(range(self.V))
        
    def _create_temp_graph(self):
        temp_graph = copy.deepcopy(self.original_graph)
        temp_graph.num_vertices += 1
        new_vertex = self.V
        
        for v in self.vertex_list:
            temp_graph.add_edge(new_vertex, v, 0)
            
        return temp_graph, new_vertex

    def _bellman_ford(self, temp_graph, new_vertex):
        h = {v: float('inf') for v in range(temp_graph.get_num_vertices())}
        h[new_vertex] = 0
        
        for _ in range(temp_graph.get_num_vertices() - 1):
            for (u, v), w in temp_graph.edges.items():
                if h[u] + w < h[v]:
                    h[v] = h[u] + w
                    
        for (u, v), w in temp_graph.edges.items():
            if h[u] + w < h[v]:
                raise ValueError("Graf zawiera cykl o ujemnej wadze")
                
        return {v: h[v] for v in self.vertex_list}

    def _dijkstra(self, graph, src, h):
        dist = {v: float('inf') for v in self.vertex_list}
        dist[src] = 0
        heap = [(0, src)]
        
        while heap:
            current_dist, u = heapq.heappop(heap)
            if current_dist > dist[u]:
                continue
                
            for v, w in graph.vertex_out_neighbors_weights(u):
                new_weight = w + h[u] - h[v]
                if dist[u] + new_weight < dist[v]:
                    dist[v] = dist[u] + new_weight
                    heapq.heappush(heap, (dist[v], v))
                    
        return dist

    def johnson(self):
        temp_graph, new_vertex = self._create_temp_graph()
        
        try:
            h = self._bellman_ford(temp_graph, new_vertex)
        except ValueError as e:
            return str(e)
            
        all_pairs = defaultdict(dict)
        
        for u in self.vertex_list:
            dist = self._dijkstra(self.original_graph, u, h)
            for v in self.vertex_list:
                if dist[v] != float('inf'):
                    all_pairs[u][v] = dist[v] + h[v] - h[u]
                else:
                    all_pairs[u][v] = float('inf')
                    
        return all_pairs