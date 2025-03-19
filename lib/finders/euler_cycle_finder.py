from typing import List
from copy import deepcopy

from lib.finders.finder import Finder
from lib.graph_property_checker.eulerian_checker import EulerianChecker
from lib.core.graph import Graph
from lib.utils.bridge_checker import BridgeChecker


class EulerCycleFinder(Finder):
    @staticmethod
    def find(graph: Graph) -> List[int] | None:
        if not EulerianChecker.check(graph):
            return None
        
        graph_cp = deepcopy(graph)
        
        cycle = [0]
        euler_cycle = []
        
        while cycle:
            current_vertex = cycle[-1]
            
            if neighbors:=graph_cp.vertex_neighbors(current_vertex):
                next_vertex = neighbors[0]
                cycle.append(next_vertex)
                graph_cp.remove_edge(current_vertex, next_vertex)
            else:
                euler_cycle.append(cycle.pop())
        
        return euler_cycle[::-1]