from random import choice

from lib.core.graph import Graph
from lib.core.adjacency_matrix_graph import AdjacencyMatrixGraph
from lib.generators.RandomGraphGeneator import RandomGraphGenerator


class RandomTree(RandomGraphGenerator):
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
    
    def generate(self) -> Graph:
        graph = AdjacencyMatrixGraph(self.num_vertices)
        vertices = list(range(self.num_vertices))
        root = choice(vertices)
        vertices.remove(root)
        picked_vertices = [root]
        
        while vertices:
            u = choice(picked_vertices)
            v = choice(vertices)
            graph.add_edge(u, v)
            picked_vertices.append(v)
            vertices.remove(v)
            
        return graph
        