from typing import Tuple
from lib.core.graph import Graph

import random


class GraphRandomizer:
    @staticmethod
    def can_exchange_edges(
        graph: Graph, edge1: Tuple[int, int], edge2: Tuple[int, int]
    ) -> bool:
        a, b = edge1
        c, d = edge2

        if edge1 == edge2:
            return False
        if graph.edge_exists(a, d) or graph.edge_exists(b, c):
            return False
        if a == c or a == d or b == c or b == d:
            return False
        return True

    @staticmethod
    def exchange_random_edges(graph: Graph) -> bool:
        edges = graph.get_edges()
        exchanged = False

        while edges:
            edge1 = random.choice(edges)
            a, b = edge1

            edges.remove(edge1)
            potential_edges = edges.copy()

            while potential_edges:
                edge2 = random.choice(potential_edges)
                c, d = edge2

                potential_edges.remove(edge2)

                if GraphRandomizer.can_exchange_edges(graph, edge1, edge2):
                    graph.remove_edge(*edge1)
                    graph.remove_edge(*edge2)
                    graph.add_edge(a, d)
                    graph.add_edge(b, c)
                    exchanged = True
                    break

            if exchanged:
                break

        return exchanged

    def randomize(graph: Graph, num_exchanges: int):
        for _ in range(num_exchanges):
            if not GraphRandomizer.exchange_random_edges(graph):
                raise ValueError("Cannot randomize graph.")
