from typing import List

from lib.finders.finder import Finder
from lib.core.graph import Graph
from lib.graph_property_checker.connected_checker import ConnectedChecker
from lib.graph_traversal.bfs_traversal import BFSVisitor

class HamiltonianCycleFinder(Finder):
    @staticmethod
    def find(graph: Graph) -> List[int] | None:
        if not ConnectedChecker.check(graph):
            return None
        
        stack = []
        if HamiltonianCycleFinder._find_cycle(graph, 0, stack):
            return stack
        else:
            return None
    
    @staticmethod
    def _find_cycle(graph: Graph, vertex: int, stack: List[int]) -> bool:
        stack.append(vertex)
        
        if len(stack) == graph.num_vertices:
            if graph.edge_exists(stack[-1], stack[0]):
                return True
            else:
                stack.pop()
                return False
            
        for neighbor in graph.vertex_neighbors(vertex):
            if neighbor not in stack:
                if HamiltonianCycleFinder._find_cycle(graph, neighbor, stack):
                    break
        else:
            stack.pop()
            return False
        
        return True
    
    @staticmethod
    def print_cycle(cycle: List[int]| None):
        if cycle:
            print(" -> ".join(str(vertex) for vertex in cycle + [cycle[0]]))
        else:
            print()