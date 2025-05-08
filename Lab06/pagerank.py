import random
from concurrent.futures import ProcessPoolExecutor

import numpy as np
from dataclasses import dataclass, field
from collections import defaultdict
from typing import Dict, List


class DirectedGraph:
    def __init__(self):
        self.adj: Dict[int, List[int]] = {}

    def add_edge(self, u: int, v: int):
        self.adj.setdefault(u, []).append(v)
        self.adj.setdefault(v, [])

    def vertices(self) -> List[int]:
        return list(self.adj.keys())

    def neighbors(self, u: int) -> List[int]:
        return self.adj[u]

    def out_degree(self, u: int) -> int:
        return len(self.adj[u])

    def node_count(self) -> int:
        return len(self.adj)


@dataclass
class PageRank:
    graph: DirectedGraph
    d: float = 0.15
    result: Dict[int, float] = field(default_factory=dict)

    def random_walk(self, steps: int = 1_000_000) -> Dict[int, float]:
        visits = defaultdict(int)
        nodes = self.graph.vertices()
        current = random.choice(nodes)

        for _ in range(steps):
            if random.random() < self.d or self.graph.out_degree(current) == 0:
                current = random.choice(nodes)
            else:
                current = random.choice(self.graph.neighbors(current))
            visits[current] += 1

        total = sum(visits.values())
        self.result = {node: visits[node] / total for node in nodes}
        return self.result

    def power_iteration(self, max_iter: int = 100, tol: float = 1e-6) -> Dict[int, float]:
        nodes = self.graph.vertices()
        n = len(nodes)
        idx_map = {node: i for i, node in enumerate(nodes)}
        rev_map = {i: node for node, i in idx_map.items()}

        P = np.zeros((n, n))
        for j in nodes:
            neighbors = self.graph.neighbors(j)
            if neighbors:
                prob = (1 - self.d) / len(neighbors)
                for i in neighbors:
                    P[idx_map[i], idx_map[j]] = prob
            P[:, idx_map[j]] += self.d / n

        p = np.ones(n) / n
        for _ in range(max_iter):
            new_p = P @ p
            if np.linalg.norm(new_p - p, 1) < tol:
                break
            p = new_p

        self.result = {rev_map[i]: float(val) for i, val in enumerate(p)}
        return self.result

    def parallel_random_walk(self, total_steps: int = 1_000_000, workers: int = 4) -> Dict[int, float]:
        node_ids = self.graph.vertices()
        adjacency = self.graph.adj

        def _simulate_walks(node_ids: List[int], adjacency: Dict[int, List[int]],
                            steps: int, damping: float, seed: int) -> Dict[int, int]:
            random.seed(seed)
            visits = defaultdict(int)
            current = random.choice(node_ids)

            for _ in range(steps):
                if random.random() < damping or not adjacency[current]:
                    current = random.choice(node_ids)
                else:
                    current = random.choice(adjacency[current])
                visits[current] += 1

            return dict(visits)

        with ProcessPoolExecutor(max_workers=workers) as executor:
            futures = [
                executor.submit(_simulate_walks, node_ids, adjacency,
                                total_steps // workers, self.d, i)
                for i in range(workers)
            ]
            results = [f.result() for f in futures]

        total_visits = defaultdict(int)
        for partial in results:
            for k, v in partial.items():
                total_visits[k] += v

        total = sum(total_visits.values())
        self.result = {node: total_visits[node] / total for node in node_ids}
        return self.result
