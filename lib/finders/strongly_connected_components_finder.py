from typing import List
from collections import defaultdict
from lib.finders.finder import Finder
from lib.core.graph import Graph
from lib.core.converter import GraphConverter

#Kosaraju Algorithm
class SCCFinder(Finder):
    t: int = 0

    @staticmethod
    def find(graph: Graph) -> List[int] | None:
        n = graph.num_vertices
        d = [-1] * n
        f = [-1] * n
        comp = [-1] * n
        SCCFinder.t = 0
        nodes = list(range(graph.num_vertices))
        for v in nodes:
            d[v] = -1
            f[v] = -1

        for v in nodes:
            if d[v] == -1 :
                SCCFinder._first_depth_first_search(v, graph, d, f)

        transposed_graph = SCCFinder._transpose_graph(graph)
        nr = 0

        for v in nodes:
            comp[v] = -1

        nodes_with_f = list(zip(nodes, f))
        sorted_nodes = sorted(nodes_with_f, key=lambda x: x[1], reverse=True)
        for v, _ in sorted_nodes:
            if comp[v] == -1:
                nr += 1
                comp[v] = nr
                SCCFinder._second_depth_first_search(nr, v, transposed_graph, comp)

        SCCFinder._print_comp(comp)
        return comp
    
    @staticmethod
    def _first_depth_first_search(vertex: int, graph: Graph, d: List[int], f: List[int]) -> None:
        global t
        SCCFinder.t += 1
        d[vertex] = SCCFinder.t
        for u in graph.vertex_neighbors(vertex):
            if d[u] == -1:
                SCCFinder._first_depth_first_search(u, graph, d, f)

        SCCFinder.t += 1
        f[vertex] = SCCFinder.t

    @staticmethod
    def _transpose_graph(graph: Graph):
        matrix = [list(row) for row in zip(*graph.to_adjacency_matrix())]
        transposed_graph = GraphConverter.digraph_from_adjacency_matrix(matrix)
        return transposed_graph
    
    @staticmethod
    def _second_depth_first_search(nr: int, vertex: int, graph: Graph, comp: List[int]):
        for u in graph.vertex_neighbors(vertex):
            if comp[u] == -1:
                comp[u] = nr
                SCCFinder._second_depth_first_search(nr, u, graph, comp)

    @staticmethod
    def _print_comp(comp: List[int]):
        groups = defaultdict(list)
        for v, c in enumerate(comp):
            groups[c].append(v+1)
        for comp_id in sorted(groups):
            vertices = groups[comp_id]
            print(f"{comp_id} component, vertices: {vertices}")
            