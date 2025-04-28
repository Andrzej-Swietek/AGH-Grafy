from random import choices

from lib.core.graph import Graph
from lib.generators.RandomGraphGeneator import RandomGraphGenerator
from lib.core.converter import GraphConverter
from lib.utils.graphic_sequence_checker import GraphicSequenceChecker
from lib.utils.graph_randomizer import GraphRandomizer


class RandomRegularGraph(RandomGraphGenerator):
    def __init__(
        self,
        num_vertices: int,
        vertex_degree: int,
        num_randomizations: int = 50,
    ):
        self.num_vertices = num_vertices
        self.vertex_degree = vertex_degree
        self.num_randomizations = num_randomizations

        if not self.check_input():
            raise ValueError("Number of vertices must be even for odd degree.")

    def check_input(self) -> bool:
        return (self.num_vertices > self.vertex_degree) and (self.num_vertices % 2 == 0 if self.vertex_degree % 2 == 1 else True)

    def generate(self) -> Graph:
        seq = [self.vertex_degree] * self.num_vertices

        if not GraphicSequenceChecker.is_graphic(seq):
            raise ValueError("Unable to generate graph with given parameters.")

        graph = GraphConverter.from_graphic_sequence(seq)
        GraphRandomizer.randomize(graph, self.num_randomizations)

        return graph
