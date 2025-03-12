import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

from lib.core.graph import Graph


class GraphVisualizer:
    @staticmethod
    def draw(graph: Graph):
        num_vertices = graph.num_vertices
        edges = graph.get_edges()

        theta = np.linspace(0, 2 * np.pi, num_vertices, endpoint=False)
        positions = {i: (np.cos(theta[i]), np.sin(theta[i])) for i in range(num_vertices)}

        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        ax.set_xticks([])
        ax.set_yticks([])
        ax.axis('off')

        for u, v in edges:
            x_values = [positions[u][0], positions[v][0]]
            y_values = [positions[u][1], positions[v][1]]
            ax.plot(x_values, y_values, 'k-', lw=1)

        for i, (x, y) in positions.items():
            ax.scatter(x, y, s=100, c='r', edgecolors='black', zorder=3)
            ax.text(x, y, str(i), fontsize=12, ha='center', va='center', zorder=4, color='white',
                    bbox=dict(facecolor='black', edgecolor='black', boxstyle='circle'))

        plt.show()

    @staticmethod
    def draw_natural(graph: Graph):
        G = nx.Graph()
        G.add_edges_from(graph.get_edges())
        pos = nx.spring_layout(G)

        plt.figure()
        nx.draw(G, pos, with_labels=True, node_color='red', edge_color='black', node_size=500, font_color='white')
        plt.show()
