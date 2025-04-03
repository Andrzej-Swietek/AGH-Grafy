import argparse
from lib.generators.RandomGraphGNK import RandomGraphGNK
from lib.visualization.graph_visualizer import GraphVisualizer

def task_one():
    print("Generating digraph.")
    n, k = 10, 15
    graph = RandomGraphGNK(n, k).generate_connected_weighted()
    
    graph.fill_with_random_edges_uniform(1, 10)
    GraphVisualizer.draw_digraph(graph)

def task_two():
    print("")

def task_three():
    print("")

def task_four():
    print("")

def main():
    parser = argparse.ArgumentParser(description="Grafy-Lab04")
    parser.add_argument("-t", "--task", type=int, required=True, help="Select Task (1-4)")
    args = parser.parse_args()
    
    tasks = [task_one, task_two, task_three, task_four]
    if 1 <= args.task <= 4:
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
    liczbami całkowitymi z zakresu [−5, 10]. Zaimplementować algorytm
    Bellmana-Forda do znajdowania najkrótszych ścieżek od danego wierzchołka.
    """

    """
    4.  Zaimplementować algorytm Johnsona do szukania odegłości pomiędzy
    wszystkimi parami wierzchołków na ważonym grafie skierowanym.
    """

    main()