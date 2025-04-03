import argparse
from lib.generators.RandomGraphGNP import RandomGraphGNP
from lib.visualization.graph_visualizer import GraphVisualizer
from lib.finders.KosarajuSCC import KosarajuSCC

def task_one():
    print("Generating digraph.")
    n, p = 10, 0.5
    graph = RandomGraphGNP(n, p).generate_directed()

    graph.fill_with_random_weights(1, 10)    
    edges = graph.get_edges()
    for (u, v, w) in edges:
        print(f"{u} {v} {w}")
    print("Graph generated with random weights.")
    
    GraphVisualizer.draw_digraph(graph)

def task_two():
    graph = RandomGraphGNK(10, 15).generate_connected_weighted()
    sccs = KosarajuSCC(graph).find_sccs()
    
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