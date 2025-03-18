from abc import ABC, abstractmethod
from typing import List, Dict, Tuple

import random

class GraphOperations(ABC):
    @abstractmethod
    def add_edge(self, u: int, v: int):
        pass

    @abstractmethod
    def remove_edge(self, u: int, v: int):
        pass

    @abstractmethod
    def get_edges(self) -> List[Tuple[int, int]]:
        pass
    
    @abstractmethod
    def edge_exists(self, u: int, v: int) -> bool:
        pass

    def can_exchange_edges(self, edge1: Tuple[int, int], edge2: Tuple[int, int]) -> bool:
        a, b = edge1
        c, d = edge2

        if edge1 == edge2:
            return False
        if self.edge_exists(a, d) or self.edge_exists(b, c):
            return False
        if a == c or a == d or b == c or b == d:
            return False
        return True

    def exchange_random_edges(self) -> bool:
        edges = self.get_edges()
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

                if self.can_exchange_edges(edge1, edge2):
                    self.remove_edge(*edge1)
                    self.remove_edge(*edge2)
                    self.add_edge(a, d)
                    self.add_edge(b, c)
                    exchanged = True
                    break
                    
            if exchanged:
                break

        return exchanged

    def randomize(self, num_exchanges: int):
        for _ in range(num_exchanges):
            if not self.exchange_random_edges():
                raise ValueError("Cannot randomize graph.")


class GraphRepresentation(ABC):
    @abstractmethod
    def to_adjacency_matrix(self) -> List[List[int]]:
        pass

    @abstractmethod
    def to_incidence_matrix(self) -> List[List[int]]:
        pass

    @abstractmethod
    def to_adjacency_list(self) -> Dict[int, List[int]]:
        pass

    @abstractmethod
    def to_graphic_sequence(self) -> List[int]:
        pass


class Graph(GraphOperations, GraphRepresentation, ABC):
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
