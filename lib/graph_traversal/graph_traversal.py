from abc import ABC, abstractmethod
from typing import Callable
from lib.core.graph import Graph

class GraphTraversal(ABC):
    @abstractmethod
    def traverse(self, graph: Graph, start_vertex: int, callback: Callable[[int], None]):
        pass
