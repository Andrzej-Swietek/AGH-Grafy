from random import random

from lib.core.adjacency_matrix_graph import AdjacencyMatrixGraph
from lib.core.adjacency_matrix_digraph import AdjacencyMatrixDigraph
from lib.core.graph import Graph
from lib.generators.RandomGraphGeneator import RandomGraphGenerator


class RandomGraphGNP(RandomGraphGenerator):
    def __init__(self, num_vertices: int, probability: float):
        self.num_vertices = num_vertices
        self.probability = probability
    
    def generate(self) -> Graph:
        graph = AdjacencyMatrixGraph(self.num_vertices)
        for i in range(self.num_vertices):
            for j in range(i + 1, self.num_vertices):
                if random() < self.probability:
                    graph.add_edge(i, j)
        return graph
    
    def generate_directed(self) -> Graph:
        graph = AdjacencyMatrixDigraph(self.num_vertices)
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if random() < self.probability and i != j:
                    graph.add_edge(i, j)
        return graph
