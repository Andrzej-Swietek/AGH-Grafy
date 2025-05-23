import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

from lib.core.graph import Graph
from lib.core.weighted_graph import WeightedGraph
from lib.core.weighted_digraph import WeightedDigraph
from lib.core.flow_network import FlowNetwork

class GraphVisualizer:
    @staticmethod
    def draw(graph: Graph, show:bool = True, ax: plt.Axes = None):
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

        for u, v in edges:
            x_values = [positions[u][0], positions[v][0]]
            y_values = [positions[u][1], positions[v][1]]
            ax.plot(x_values, y_values, 'k-', lw=1)

        for i, (x, y) in positions.items():
            ax.scatter(x, y, s=100, c='r', edgecolors='black', zorder=3)
            ax.text(x, y, str(i), fontsize=12, ha='center', va='center', zorder=4, color='white',
                    bbox=dict(facecolor='black', edgecolor='black', boxstyle='circle'))

        if show:
            plt.show()
        
    @staticmethod
    def draw_side_by_side(graph1: Graph, graph2: Graph):
        fig, axs = plt.subplots(1, 2)
        GraphVisualizer.draw(graph1, show=False, ax=axs[0])
        GraphVisualizer.draw(graph2, show=False, ax=axs[1])
        plt.show()

    @staticmethod
    def draw_natural(graph: Graph):
        G = nx.Graph()
        G.add_edges_from(graph.get_edges())
        pos = nx.spring_layout(G)

        plt.figure()
        nx.draw(G, pos, with_labels=True, node_color='red', edge_color='black', node_size=500, font_color='white')
        plt.show()
        
    @staticmethod
    def drawWeighted(graph: WeightedGraph, show: bool = True, ax: plt.Axes = None):
        num_vertices = graph.get_num_vertices()
        edges = graph.get_edges()

        theta = np.linspace(0, 2 * np.pi, num_vertices, endpoint=False)
        positions = {i: (np.cos(theta[i]), np.sin(theta[i])) for i in range(num_vertices)}

        if ax is None:
            fig, ax = plt.subplots()
        ax.set_aspect('equal')
        ax.set_xticks([])
        ax.set_yticks([])
        ax.axis('off')

        for (u, v, weight) in edges:
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
    def draw_natural_weighted(graph: WeightedGraph):
        G = nx.Graph()
        edges = graph.get_edges()
        G.add_weighted_edges_from(edges)

        pos = nx.spring_layout(G)

        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_color='red', edge_color='black', node_size=500, font_color='white')
        edge_labels = {(u, v): w for u, v, w in edges}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='blue')

        plt.show()

    @staticmethod
    def draw_digraph(graph: Graph):
        G = nx.DiGraph()
        edges = graph.get_edges()
        G.add_edges_from(edges)

        nodes = list(G.nodes())
        if min(nodes) == 0:
            mapping = {i: i + 1 for i in nodes}
            G = nx.relabel_nodes(G, mapping)

        pos = nx.circular_layout(G)

        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_color='red', edge_color='black', node_size=500, font_color='white', connectionstyle="arc3,rad=0.1")
        plt.show()
    
    @staticmethod
    def draw_natural_digraph(graph: Graph):
        G = nx.DiGraph()
        edges = graph.get_edges()
        G.add_edges_from(edges)

        nodes = list(G.nodes())
        if min(nodes) == 0:
            mapping = {i: i + 1 for i in nodes}
            G = nx.relabel_nodes(G, mapping)

        pos = nx.spring_layout(G)

        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_color='red', edge_color='black', node_size=500, font_color='white', connectionstyle="arc3,rad=0.1")
        plt.show()

    @staticmethod
    def draw_weighted_digraph(graph: WeightedDigraph):
        G = nx.DiGraph()
        edges_dict = graph.edges
        weighted_edges = [(u, v, w) for (u, v), w in edges_dict.items()]
        G.add_weighted_edges_from(weighted_edges)

        nodes = list(G.nodes())
        if min(nodes) == 0:
            mapping = {i: i + 1 for i in nodes}
            G = nx.relabel_nodes(G, mapping, copy=True)

        pos = nx.circular_layout(G)

        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_color='red', edge_color='black', node_size=500, font_color='white', connectionstyle="arc3,rad=0.1")
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, connectionstyle="arc3,rad=0.1")
        plt.show()
    
    @staticmethod
    def draw_natural_weighted_digraph(graph: WeightedDigraph):
        G = nx.DiGraph()
        edges_dict = graph.edges
        weighted_edges = [(u, v, w) for (u, v), w in edges_dict.items()]
        G.add_weighted_edges_from(weighted_edges)

        nodes = list(G.nodes())
        if min(nodes) == 0:
            mapping = {i: i + 1 for i in nodes}
            G = nx.relabel_nodes(G, mapping)

        pos = nx.spring_layout(G)

        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_color='red', edge_color='black', node_size=500, font_color='white', connectionstyle="arc3,rad=0.1")
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, connectionstyle="arc3,rad=0.1")
        plt.show()

    @staticmethod
    def draw_flow_network(graph: FlowNetwork):
        G = nx.DiGraph()
        edges_dict = graph.edges
        weighted_edges = [(u, v, w) for (u, v), w in edges_dict.items()]
        G.add_weighted_edges_from(weighted_edges)

        layers = graph.get_layers()
        pos = {}
        for layer_idx, layer in enumerate(layers):
            y_step = 1.0 / (len(layer) + 1)
            for i, node in enumerate(layer):
                pos[node] = (layer_idx, (i + 1) * y_step)

        plt.figure(figsize=(10, 5))
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=600, font_color='black', edge_color='gray', arrows=True, connectionstyle="arc3,rad=0.1")
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, connectionstyle="arc3,rad=0.1")
        plt.title("Auto-Layered Flow Network")
        plt.axis('off')
        plt.show()

    @staticmethod
    def draw_max_flow_network(graph: FlowNetwork, flows):
        G = nx.DiGraph()
        edges_dict = graph.edges
        weighted_edges = [(u, v, w) for (u, v), w in edges_dict.items()]
        G.add_weighted_edges_from(weighted_edges)

        layers = graph.get_layers()
        pos = {}
        for layer_idx, layer in enumerate(layers):
            y_step = 1.0 / (len(layer) + 1)
            for i, node in enumerate(layer):
                pos[node] = (layer_idx, (i + 1) * y_step)

        plt.figure(figsize=(10, 5))
        nx.draw(
            G, pos, with_labels=True, node_color='skyblue', node_size=600,
            font_color='black', edge_color='gray', arrows=True,
            connectionstyle="arc3,rad=0.1"
        )

        # Create edge labels in format "flow/capacity"
        edge_labels = {}
        for (u, v), capacity in edges_dict.items():
            flow = flows.get((u, v), 0)
            edge_labels[(u, v)] = f"{flow}/{capacity}"

        nx.draw_networkx_edge_labels(
            G, pos, edge_labels=edge_labels,
            connectionstyle="arc3,rad=0.1"
        )

        plt.title("Auto-Layered Flow Network")
        plt.axis('off')
        plt.show()
