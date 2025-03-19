from typing import List

from lib.finders.finder import Finder
from lib.core.graph import Graph
from lib.graph_traversal.dfs_traversal import DFSVisitor


class ComponentsFinder(Finder):
    @staticmethod
    def find(graph: Graph) -> List[List[int]]:
        """
        Znajduje spójne składowe grafu.
        """
        components = []
        visited = [False] * graph.num_vertices
        dfs = DFSVisitor()

        for v in range(graph.num_vertices):
            if not visited[v]:
                component = set()

                def mark_visited(u):
                    component.add(u)
                    visited[u] = True

                dfs.traverse(graph, v, lambda u: mark_visited(u))
                components.append(list(component))

        return components
    
    @staticmethod
    def largest_component(graph: Graph) -> List[int]:
        """
        Znajduje największą spójną składową grafu.
        """
        components = ComponentsFinder.find(graph)
        return max(components, key=len)

    @staticmethod
    def print_components(components: List[List[int]]):
        """
        Wypisuje spójne składowe grafu wraz z największą z nich.
        """
        for i, component in enumerate(components):
            print(f"{i+1}) {' '.join(map(str, component))}")
        print(f"Largest component: {components.index(max(components, key=len)) + 1}")
