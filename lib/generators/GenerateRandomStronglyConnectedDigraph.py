import random
from lib.core.directed_graph import DirectedGraph

def generate_random_strongly_connected_digraph(
    num_vertices: int,
    extra_edge_prob: float = 0.1,
    min_weight: int = -5,
    max_weight: int = 10
) -> DirectedGraph:
    graph = DirectedGraph(num_vertices)
    
    if num_vertices <= 1:
        return graph
    
    nodes = list(range(num_vertices))
    random.shuffle(nodes)
    
    for i in range(num_vertices):
        u = nodes[i]
        v = nodes[(i + 1) % num_vertices]
        graph.add_edge(u, v, 1)
    
    for u in range(num_vertices):
        for v in range(num_vertices):
            if u != v and not graph.edge_exists(u, v):
                if random.random() < extra_edge_prob:
                    graph.add_edge(u, v, 1)
    
    H = max(max_weight, 1) 
    h = {v: random.randint(0, H) for v in range(num_vertices)}
    
    for (u, v) in list(graph.edges.keys()):
        delta = h[u] - h[v]
        possible_min_k = max(0, min_weight - delta)
        possible_max_k = max_weight - delta
        k = random.randint(possible_min_k, possible_max_k)
        graph.edges[(u, v)] = delta + k
    
    return graph