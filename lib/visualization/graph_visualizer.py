import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

from lib.core.weighted_graph import WeightedGraph

class GraphVisualizer:
    @staticmethod
    def draw(graph: WeightedGraph, show: bool = True, ax: plt.Axes = None):
        """Draws a weighted graph in a circular layout with edge weights."""
        num_vertices = graph.num_vertices
        edges = graph.get_edges()

        theta = np.linspace(0, 2 * np.pi, num_vertices, endpoint=False)
        positions = {i: (np.cos(theta[i]), np.sin(theta[i])) for i in range(num_vertices)}

        if ax is None:
            fig, ax = plt.subplots()
        ax.set_aspect('equal')
        ax.set_xticks([])
        ax.set_yticks([])
        ax.axis('off')

        for u, v, weight in edges:
            x_values = [positions[u][0], positions[v][0]]
            y_values = [positions[u][1], positions[v][1]]
            ax.plot(x_values, y_values, 'k-', lw=1)
            mid_x, mid_y = (x_values[0] + x_values[1]) / 2, (y_values[0] + y_values[1]) / 2
            ax.text(mid_x, mid_y, str(weight), fontsize=10, ha='center', va='center', color='blue')

        for i, (x, y) in positions.items():
            ax.scatter(x, y, s=100, c='r', edgecolors='black', zorder=3)
            ax.text(x, y, str(i), fontsize=12, ha='center', va='center', zorder=4, color='white',
                    bbox=dict(facecolor='black', edgecolor='black', boxstyle='circle'))

        if show:
            plt.show()
        
    @staticmethod
    def draw_natural(graph: WeightedGraph):
        """Uses NetworkX to visualize the graph with weighted edges."""
        G = nx.Graph()
        edges = graph.get_edges()
        G.add_weighted_edges_from(edges)

        pos = nx.spring_layout(G)

        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_color='red', edge_color='black', node_size=500, font_color='white')
        edge_labels = {(u, v): w for u, v, w in edges}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='blue')

        plt.show()
