from abc import ABC, abstractmethod
from typing import List, Dict, Tuple

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
