import random
from copy import deepcopy
from collections import deque, defaultdict

from lib.core.flow_network import FlowNetwork
from lib.generators.RandomGraphGeneator import RandomGraphGenerator


class RandomFlowNetwork(RandomGraphGenerator):
    def __init__(self, inter_layers: int, probability: float):
        self.num_vertices = 0
        self.inter_layers = inter_layers
        self.probability = probability

    def infer_layers(self, graph: FlowNetwork, source: int) -> list[list[int]]:
        visited = set()
        level = {source: 0}
        layers = defaultdict(list)

        queue = deque([source])
        visited.add(source)

        while queue:
            u = queue.popleft()
            layers[level[u]].append(u)
            for v in graph.successors(u):
                if v not in level or level[v] > level[u] + 1:
                    level[v] = level[u] + 1
                    queue.append(v)
                    visited.add(v)

        # Convert layers dict to ordered list of lists
        max_layer = max(level.values())
        return [layers[i] for i in range(max_layer + 1)]
    
    def generate(self) -> FlowNetwork:
        graph = FlowNetwork(2)
        prev_layer = [0]
        vert = 0
        for _ in range(self.inter_layers):
            new_layer = []
            pool = deepcopy(prev_layer)
            for i in range(self.inter_layers):
                if i < 2 or random.random() < self.probability:
                    vert += 1
                    node = None
                    if not pool:
                        node = random.choice(prev_layer)
                    else:
                        node = random.choice(pool)
                        pool.remove(node)
                    graph.add_edge(node, vert, random.choice(range(1, 11)))
                    new_layer.append(vert)
            if pool:
                for node in pool:
                    graph.add_edge(node, random.choice(new_layer), random.choice(range(1, 11)))
            prev_layer = new_layer

        vert += 1
        for node in prev_layer:
            graph.add_edge(node, vert, random.choice(range(1, 11)))
        graph.num_vertices = vert
        graph.inter_layers = self.infer_layers(graph, 0)

        for _ in range(2*self.inter_layers):
            u = random.choice(range(1, graph.num_vertices - 1))
            v = random.choice(range(1, graph.num_vertices - 1))
            added = False
            while not added:
                if u != v and not graph.edge_exists(u, v):
                    graph.add_edge(u, v, random.choice(range(1, 11)))
                    added = True
                else:
                    u = random.choice(range(1, graph.num_vertices - 1))
                    v = random.choice(range(1, graph.num_vertices - 1))
        return graph

