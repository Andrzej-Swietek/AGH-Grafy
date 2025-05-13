import argparse
from collections import defaultdict

from lib.core.converter import GraphConverter
from lib.generators.RandomGraphGNP import RandomGraphGNP
from lib.utils.graph_importer import GraphWriter, GraphReader
from lib.visualization.graph_visualizer import GraphVisualizer

from lib.finders.strongly_connected_components_finder import SCCFinder
from lib.finders.shortest_path_finder import ShortestPathFinder
from lib.finders.distance_finder import DistanceFinder

def process_graph(input_file: str, input_type: str):
    if input_type == "adjacency_matrix":
        matrix = GraphReader.read_adjacency_matrix(input_file)
        graph = GraphConverter.digraph_from_adjacency_matrix(matrix)
    elif input_type == "adjacency_list":
        adjacency_list = GraphReader.read_adjacency_list(input_file)
        graph = GraphConverter.digraph_from_adjacency_list(adjacency_list)
    elif input_type == "incidence_matrix":
        incidence_matrix = GraphReader.read_incidence_matrix(input_file)
        graph = GraphConverter.digraph_from_incidence_matrix(incidence_matrix)
    else:
        raise ValueError("Invalid input type")

    print("Graph loaded successfully. Converting representations...")
    GraphWriter.write_adjacency_matrix(graph, "output_adjacency_matrix.txt")
    GraphWriter.write_adjacency_list(graph, "output_adjacency_list.txt")
    GraphWriter.write_incidence_matrix(graph, "output_incidence_matrix.txt")

    print("Graph representations saved. Generating visualizations...")
    GraphVisualizer.draw_digraph(graph)
    GraphVisualizer.draw_natural_digraph(graph)
    print("Visualization complete.")

    return graph

def generate_random_graph(n: int, param: float):
    generator = RandomGraphGNP(n, param)
    graph = generator.generate_directed()
    print("Random graph generated successfully.")
    GraphWriter.write_adjacency_matrix(graph, "output_adjacency_matrix.txt")
    GraphWriter.write_adjacency_list(graph, "output_adjacency_list.txt")
    GraphWriter.write_incidence_matrix(graph, "output_incidence_matrix.txt")
    print("Graph representations saved. Generating visualizations...")
    GraphVisualizer.draw_digraph(graph)
    GraphVisualizer.draw_natural_digraph(graph)
    print("Visualization complete.")
    return graph

def convert_to_strongly_connected(graph):
    scc = SCCFinder.find(graph)
    groups = defaultdict(list)
    for v, c in enumerate(scc):
        groups[c].append(v)

    if len(groups) > 1:
        print("Converting digraph to strongly connected...")
        first_vertices = [vertices[0] for vertices in groups.values()]
        u = first_vertices[0]
        for v in first_vertices:
            if u != v:
                if not graph.edge_exists(u, v):
                    graph.add_edge(u, v)
                if not graph.edge_exists(v, u):
                    graph.add_edge(v, u)
            u = v

        print("Generating visualizations...")
        GraphVisualizer.draw_digraph(graph)
        print("Visualization complete.")
        SCCFinder.find(graph)

        print("Digraph converted into strongly connected.")
    else:
        print("Digraph strongly connected.")

    return graph



def task_one(input: str):
    if "adj_list" in input:
        process_graph(input, "adjacency_list")
    elif "adj_matrix" in input:
        process_graph(input, "adjacency_matrix")
    elif "incidence_matrix" in input:
        process_graph(input, "incidence_matrix")

def task_one(n: int, p: float):
        generate_random_graph(n, p)



def task_two():
    graph = process_graph("output_adjacency_matrix.txt", "adjacency_matrix")
    SCCFinder.find(graph)
    

def task_three():
    graph = process_graph("output_adjacency_matrix.txt", "adjacency_matrix")

    graph = convert_to_strongly_connected(graph)
    weighted_graph = graph.convert_to_weighted()
    weighted_graph.fill_with_random_weights(-3, 10) # range of weights;

    print("Graph filled with random weights. Generating visualizations...")
    GraphVisualizer.draw_weighted_digraph(weighted_graph)
    print("Visualization complete.")

    ShortestPathFinder.find(weighted_graph)

    return weighted_graph

def task_four():

    graph = task_three()
    DistanceFinder.find(graph)

    """
    graph = process_graph("Lab04/data/adj_matrix.txt", "adjacency_matrix")

    weighted_graph = graph.convert_to_weighted()
    weighted_graph.edges[(0, 1)] = 6
    weighted_graph.edges[(0, 2)] = 3
    weighted_graph.edges[(0, 4)] = -1

    weighted_graph.edges[(1, 0)] = 10
    weighted_graph.edges[(1, 2)] = -5
    weighted_graph.edges[(1, 3)] = -4
    weighted_graph.edges[(1, 4)] = 4
    weighted_graph.edges[(1, 6)] = 4

    weighted_graph.edges[(2, 5)] = 2

    weighted_graph.edges[(3, 1)] = 5
    weighted_graph.edges[(3, 6)] = 9

    weighted_graph.edges[(4, 6)] = -4

    weighted_graph.edges[(5, 1)] = 9
    
    weighted_graph.edges[(6, 5)] = 4

    print("Graph filled with random weights. Generating visualizations...")
    GraphVisualizer.draw_weighted_digraph(weighted_graph)
    print("Visualization complete.")

    DistanceFinder.find(weighted_graph)
    """


def main():
    parser = argparse.ArgumentParser(description="Grafy-Lab04")
    parser.add_argument("-t", "--task", type=int, required=True, help="Select Task (1-4)")
    parser.add_argument('-i', '--input', type=str, help='Input file')
    parser.add_argument('-n', '--verticles', type=int, help='Number of verticles')
    parser.add_argument('-p', '--probability', type=float, help='Probability')
    args = parser.parse_args()
    
    tasks = [task_one, task_two, task_three, task_four]
    if 1 <= args.task <= 4:
        if(args.task == 1):
            if args.input:
                tasks[0](args.input)
            elif args.verticles is not None and args.probability is not None:
                tasks[0](args.verticles, args.probability)
            else:
                print("Task 1 requires either -i INPUT or both -n VERTICLES and -p PROBABILITY.")
        else:
            tasks[args.task - 1]()
    else:
        print("Invalid task selected.")

if __name__ == "__main__":
    """
    1. Napisać program do kodowania grafów skierowanych (digrafów) i do
    generowania losowych digrafów z zespołu G(n, p).
    """

    """
    2. Zaimplementować algorytm Kosaraju do szukania silnie spójnych składowych na digrafie i zastosować go do digrafu losowego.
    """

    """
    3. Wykorzystując algorytmy z powyższych punktów wygenerować losowy
    silnie spójny digraf. Łukom tego digrafu przypisać losowe wagi będące
    liczbami całkowitymi z zakresu [-5, 10]. Zaimplementować algorytm
    Bellmana-Forda do znajdowania najkrótszych ścieżek od danego wierzchołka.
    """

    """
    4.  Zaimplementować algorytm Johnsona do szukania odegłości pomiędzy
    wszystkimi parami wierzchołków na ważonym grafie skierowanym.
    """

    main()