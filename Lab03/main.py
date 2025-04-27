import argparse
import random
import numpy as np
from copy import deepcopy
from lib.generators.RandomGraphGNK import RandomGraphGNK
from lib.finders.dijkstra_finder import DijkstraFinder
from lib.visualization.graph_visualizer import GraphVisualizer
from lib.core.converter import GraphConverter
from lib.utils.graph_importer import GraphReader
from lib.core.weighted_graph import WeightedGraph
from lib.finders.mst_finder import MSTFinder

def task_one():
    print("Generating connected random graph and assigning random weights.")
    n, k = 10, 15
    graph = RandomGraphGNK(n, k).generate_connected_weighted()
    
    graph.fill_with_random_edges_uniform(1, 10)    
    edges = graph.get_edges()
    for (u, v, w) in edges:
        print(f"{u} {v} {w}")
    print("Graph generated with random weights.")
    GraphVisualizer.drawWeighted(graph, True)

def task_two():
    print("Finding shortest paths for graph from the first task using Dijkstra's algorithm")
    graph = task_one_graph()
    source = 0
    distances, paths = DijkstraFinder.find_shortest_paths(graph, source)
    
    print(f"Shortest paths from vertex {source}:")
    for target, path in paths.items():
        print(f"To {target}: Path {path}, Distance {distances[target]}")
    
    GraphVisualizer.drawWeighted(graph)

def task_three():
    print("Computing all-pairs shortest path distance matrix for graph from the first task")
    graph = task_one_graph()
    num_vertices = graph.num_vertices
    distance_matrix = np.full((num_vertices, num_vertices), np.inf)
    
    for i in range(num_vertices):
        distances, _ = DijkstraFinder.find_shortest_paths(graph, i)
        for j in range(num_vertices):
            distance_matrix[i][j] = distances[j]
    
    print("Distance Matrix:")
    print(distance_matrix)
    GraphVisualizer.drawWeighted(graph)

def task_four():
    print("Finding graph center and minimax center for graph from the first task")
    graph = task_one_graph()
    num_vertices = graph.num_vertices
    distance_matrix = np.full((num_vertices, num_vertices), np.inf)
    
    for i in range(num_vertices):
        distances, _ = DijkstraFinder.find_shortest_paths(graph, i)
        for j in range(num_vertices):
            distance_matrix[i][j] = distances[j]
    
    eccentricities = np.max(distance_matrix, axis=1)
    min_eccentricity = np.min(eccentricities)
    minimax_center = np.argmin(eccentricities)
    
    sums = np.sum(distance_matrix, axis=1)
    center = np.argmin(sums)
    
    print("Distance Matrix:")
    print(distance_matrix)
    print(f"Graph Center: {center}")
    print(f"Minimax Center: {minimax_center}")
    GraphVisualizer.drawWeighted(graph)

def task_five():
    print("Finding Minimum Spanning Tree using Prim's algorithm for graph from the first task")
    graph = task_one_graph()
    mst, tolalWeight = MSTFinder.find_minimum_spanning_tree(graph)
    
    print("MST Edges:")
    for u, v, weight in mst:
        print(f"{u} - {v}, weight: {weight}")
    
    GraphVisualizer.drawWeighted(graph)

def task_one_graph():
    """ Helper function to ensure graph is the same across tasks """
    n, k = 10, 15
    graph = RandomGraphGNK(n, k).generate_connected_weighted()
    graph.fill_with_random_edges_uniform(1, 10) 
    return graph

def main():
    parser = argparse.ArgumentParser(description="Grafy-Lab03")
    parser.add_argument("-t", "--task", type=int, required=True, help="Select Task (1-5)")
    args = parser.parse_args()
    
    tasks = [task_one, task_two, task_three, task_four, task_five]
    if 1 <= args.task <= 5:
        tasks[args.task - 1]()
    else:
        print("Invalid task selected.")

if __name__ == "__main__":
    """
    1. Korzystając z programów z poprzednich zestawów wygenerować spójny
    graf losowy. Przypisać każdej krawędzi tego grafu losową wagę będącą
    liczbą naturalną z zakresu 1 do 10.
    """
    """
    2. Zaimplementować algorytm Dijkstry do znajdowania najkrótszych ścieżek od zadanego wierzchołka do pozostałych wierzchołków i zastosować
    go do grafu z zadania pierwszego, w którym wagi krawędzi interpretowane są jako odległości wierzchołków. Wypisać wszystkie najkrótsze
    ścieżki od danego wierzchołka i ich długości.
    """
    """
    3. Wyznaczyć macierz odległości miedzy wszystkimi parami wierzchołków
    na tym grafie.
    """
    """
    4. Wyznaczyć centrum grafu, to znaczy wierzchołek, którego suma odległości do pozostałych wierzchołków jest minimalna. Wyznaczyć centrum minimax, to znaczy wierzchołek, którego odległość do najdalszego
    wierzchołka jest minimalna.
    """
    """
    5. Wyznaczyć minimalne drzewo rozpinające (algorytm Prima lub Kruskala). Wybrano algorytm Prima
    """
    main()
