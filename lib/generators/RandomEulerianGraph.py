from random import choices

from lib.core.graph import Graph
from lib.generators.RandomGraphGeneator import RandomGraphGenerator
from lib.core.converter import GraphConverter
from lib.utils.graphic_sequence_checker import GraphicSequenceChecker
from lib.graph_property_checker.connected_checker import ConnectedChecker
from lib.utils.graph_randomizer import GraphRandomizer

class RandomEulerianGraph(RandomGraphGenerator):
    def __init__(self, num_vertices: int, num_min_randomizations: int=10, num_max_randomizations: int=500):
        self.num_vertices = num_vertices
        self.num_min_randomizations = num_min_randomizations
        self.num_max_randomizations = num_max_randomizations
        
    def generate(self) -> Graph:
        possible_degrees = list(range(2, self.num_vertices, 2))
        
        while not GraphicSequenceChecker.is_graphic(seq:=choices(possible_degrees, k=self.num_vertices)):
            pass
        
        graph = GraphConverter.from_graphic_sequence(seq)
        
        GraphRandomizer.randomize(graph, self.num_min_randomizations)
        num_randomizations = self.num_min_randomizations
            
        while not ConnectedChecker.check(graph) and num_randomizations < self.num_max_randomizations:
            GraphRandomizer.randomize(graph, 1)
            num_randomizations += 1
            
        if num_randomizations == self.num_max_randomizations:
            raise ValueError("Maximal number of randomizations reached.")
        
        return graph
        
        
        
            
        