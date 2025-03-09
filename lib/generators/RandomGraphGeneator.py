from abc import ABC, abstractmethod

class RandomGraphGenerator(ABC):
    @abstractmethod
    def generate(self) -> Graph:
        pass
