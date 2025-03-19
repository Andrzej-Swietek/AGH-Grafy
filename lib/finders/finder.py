from abc import ABC, abstractmethod

from lib.core.graph import Graph

class Finder(ABC):
    @staticmethod
    @abstractmethod
    def find(graph: Graph):
        pass