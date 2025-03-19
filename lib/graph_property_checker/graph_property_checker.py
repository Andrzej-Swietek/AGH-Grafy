from abc import ABC, abstractmethod

from lib.core.graph import Graph

class GraphPropertyChecker(ABC):
    @staticmethod
    @abstractmethod
    def check(graph: Graph) -> bool:
        pass