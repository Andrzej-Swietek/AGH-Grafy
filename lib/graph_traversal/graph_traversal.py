class GraphTraversal(ABC):
    @abstractmethod
    def traverse(self, graph: Graph, start_vertex: int, callback: Callable[[int], None]):
        pass
