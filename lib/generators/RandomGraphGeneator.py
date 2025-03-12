from abc import ABC, abstractmethod
from lib.core.graph import Graph

class RandomGraphGenerator(ABC):
    @abstractmethod
    def generate(self) -> Graph:
        pass
