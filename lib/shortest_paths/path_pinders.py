class ShortestPathFinder(ABC):
    @abstractmethod
    def find_shortest_path(self, graph: Graph, start: int) -> Dict[int, float]:
        pass


class Dijkstra(ShortestPathFinder):
    def find_shortest_path(self, graph: Graph, start: int) -> Dict[int, float]:
        distances = {v: float('inf') for v in range(graph.num_vertices)}
        distances[start] = 0
        pq = [(0, start)]
        
        while pq:
            current_distance, current_vertex = heapq.heappop(pq)
            
            if current_distance > distances[current_vertex]:
                continue
            
            for neighbor, weight in graph.to_adjacency_list().get(current_vertex, []):
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        
        return distances



class BellmanFord(ShortestPathFinder):
    def find_shortest_path(self, graph: Graph, start: int) -> Dict[int, float]:
        distances = {v: float('inf') for v in range(graph.num_vertices)}
        distances[start] = 0
        
        for _ in range(graph.num_vertices - 1):
            for u, v, weight in graph.get_edges():
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
        
        return distances



class DFSPathFinder(ShortestPathFinder):
    def find_shortest_path(self, graph: Graph, start: int) -> Dict[int, float]:
        distances = {v: float('inf') for v in range(graph.num_vertices)}
        distances[start] = 0
        
        def dfs(v, current_distance):
            for neighbor, weight in graph.to_adjacency_list().get(v, []):
                if distances[neighbor] > current_distance + weight:
                    distances[neighbor] = current_distance + weight
                    dfs(neighbor, distances[neighbor])
        
        dfs(start, 0)
        return distances



class BFSPathFinder(ShortestPathFinder):
    def find_shortest_path(self, graph: Graph, start: int) -> Dict[int, float]:
        distances = {v: float('inf') for v in range(graph.num_vertices)}
        distances[start] = 0
        queue = [start]
        
        while queue:
            v = queue.pop(0)
            for neighbor, weight in graph.to_adjacency_list().get(v, []):
                if distances[neighbor] > distances[v] + weight:
                    distances[neighbor] = distances[v] + weight
                    queue.append(neighbor)
        
        return distances
