from collections import deque
from typing import List
from copy import deepcopy
from lib.core.flow_network import FlowNetwork
from lib.visualization.graph_visualizer import GraphVisualizer

#Ford-Fulkerson Algorithm
class MaxFlowFinder:
    @staticmethod
    def find(graph: FlowNetwork) -> List[List[int]] | None:
        f = {}
        for (u, v), weight in graph.edges.items():
            f[(u, v)] = 0
            f[(v, u)] = 0

        Gf = deepcopy(graph)
        s = 0
        t = Gf.num_vertices - 1
        p = MaxFlowFinder._breadth_first_search(Gf, graph.num_vertices, s, t)
        cfp = float('inf')

        while p:
            i = t
            while i != s:
                cfp = Gf.edges[(p[i], i)] if cfp > Gf.edges[(p[i], i)] else cfp
                i = p[i]

            i = t
            while i != s:
                u = p[i]
                v = i
                Gf.edges[(u, v)] -= cfp
                if Gf.edges[(u, v)] == 0:
                    Gf.remove_edge(u, v)
                f[(u, v)] += cfp

                if (v, u) not in Gf.edges:
                    Gf.add_edge(v, u, 0)
                Gf.edges[(v, u)] += cfp
                f[(v, u)] -= cfp

                i = u

            p = MaxFlowFinder._breadth_first_search(Gf, graph.num_vertices, s, t)
        
        MaxFlowFinder._print(graph, f)
    
    @staticmethod
    def _breadth_first_search(graph: FlowNetwork, n: int, source: int, sink: int) -> List[int] | None:
        ds = [float('inf')] * n
        ps = [source] * n
        ds[source] = 0
        Q = deque()
        Q.append(source)
        while Q:
            v = Q.popleft()
            for u in graph.vertex_neighbors(v):
                if ds[u] == float('inf'):
                    ds[u] = ds[v] + 1
                    ps[u] = v
                    Q.append(u)
                    if u == sink:
                        return ps
        return None
    
    @staticmethod
    def _print(graph: FlowNetwork, flows):
        GraphVisualizer.draw_max_flow_network(graph, flows)
