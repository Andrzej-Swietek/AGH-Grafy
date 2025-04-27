from random import random, sample

from lib.core.graph import Graph
from lib.core.weighted_graph import WeightedGraph
from lib.core.adjacency_matrix_graph import AdjacencyMatrixGraph
from lib.generators.RandomGraphGeneator import RandomGraphGenerator
from lib.generators.RandomTree import RandomTree

class RandomGraphGNK(RandomGraphGenerator):
    def __init__(self, num_vertices: int, num_edges: int):
        self.num_vertices = num_vertices
        self.num_edges = num_edges
        
        if num_edges > num_vertices * (num_vertices - 1) / 2:
            raise ValueError("Too many edges for given number of vertices.")
    
    def generate(self) -> Graph:
        graph = AdjacencyMatrixGraph(self.num_vertices)
        edges = set()
        while len(edges) < self.num_edges:
            u, v = sample(range(self.num_vertices), 2)
            if (u, v) not in edges and (v, u) not in edges:
                graph.add_edge(u, v)
                edges.add((u, v))
        return graph
    
    def generate_connected(self) -> Graph:
        if self.num_edges < self.num_vertices - 1:
            raise ValueError("Too few edges to generate connected graph.")
        
        graph = RandomTree(self.num_vertices).generate()
        edges = set(graph.get_edges())
        
        while len(edges) < self.num_edges:
            u, v = sample(range(self.num_vertices), 2)
            if (u, v) not in edges and (v, u) not in edges:
                graph.add_edge(u, v)
                edges.add((u, v))
    
    def generateWeighted(self) -> WeightedGraph:
        graph = WeightedGraph(self.num_vertices)
        edges = set()
        while len(edges) < self.num_edges:
            u, v = sample(range(self.num_vertices), 2)
            if (u, v) not in edges and (v, u) not in edges:
                graph.add_edge(u, v, 0)
                edges.add((u, v))
        return graph
    
    def generate_connected_weighted(self) -> WeightedGraph:
        if self.num_edges < self.num_vertices - 1:
            raise ValueError("Too few edges to generate a connected graph.")
        if self.num_edges > self.num_vertices * (self.num_vertices - 1) // 2:
            raise ValueError("Too many edges for a simple undirected graph.")

        graph = WeightedGraph(self.num_vertices)
        
        tree = RandomTree(self.num_vertices).generate()
        edge_set = set()
        for u, v in tree.get_edges():
            graph.add_edge(u, v, 0)
            edge_set.add((min(u, v), max(u, v)))

        while len(edge_set) < self.num_edges:
            u, v = sample(range(self.num_vertices), 2)
            edge = (min(u, v), max(u, v))
            if edge not in edge_set:
                graph.add_edge(u, v, 0)
                edge_set.add(edge)

        return graph
