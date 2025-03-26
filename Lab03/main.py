import argparse
from copy import deepcopy

from lib.core.converter import GraphConverter
from lib.visualization.graph_visualizer import GraphVisualizer
from lib.generators.RandomEulerianGraph import RandomEulerianGraph
from lib.generators.RandomRegularGraph import RandomRegularGraph
from lib.utils.graphic_sequence_checker import GraphicSequenceChecker
from lib.finders.components_finder import ComponentsFinder
from lib.finders.euler_cycle_finder import EulerCycleFinder
from lib.finders.hamiltonian_cycle_finder import HamiltonianCycleFinder
from lib.utils.graph_randomizer import GraphRandomizer

GRAPHIC_SEQUENCE = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
NON_GRAPHIC_SEQUENCE = [4, 4, 3, 1, 2]

def task_one():
    print("Task 1")
    for seq in [GRAPHIC_SEQUENCE, NON_GRAPHIC_SEQUENCE]:
        print(f"Examined sequence: {seq}")
        graphic = GraphicSequenceChecker.is_graphic(seq)
        print(f"Is graphic: {graphic}")
        if graphic:
            graph = GraphConverter.from_graphic_sequence(seq)
            print("Visualizing graph...")
            GraphVisualizer.draw(graph)
            print("Visualization complete.")


def task_two():
    print("Task 2")
    n = 10
    print(f"Creating graph from graphic sequence: {GRAPHIC_SEQUENCE} ...")
    graph = GraphConverter.from_graphic_sequence(GRAPHIC_SEQUENCE)
    graph_randomized = deepcopy(graph)
    print("Graph created successfully.")
    print(f"Randomizing graph {n} times...")
    GraphRandomizer.randomize(graph_randomized, n)
    print("Randomizing done.")
    print("Comparing graphs...")
    GraphVisualizer.draw_side_by_side(graph, graph_randomized)
    print("Visualization complete.")


def task_three():
    print("Task 3")
    print(f"Creating graph from graphic sequence: {GRAPHIC_SEQUENCE}")
    graph = GraphConverter.from_graphic_sequence(GRAPHIC_SEQUENCE)
    graph_randomized = deepcopy(graph)
    print("Graph created successfully.")
    print("Randomizing graph until it is has more than 1 connected component...")
    n = 0
    while len(ComponentsFinder.find(graph_randomized)) == 1:
        GraphRandomizer.randomize(graph_randomized, 1)
        n += 1
    print(f"Graph randomized {n} times.")
    print("Graph components:")
    ComponentsFinder.print_components(ComponentsFinder.find(graph))
    print("Randomized graph components:")
    ComponentsFinder.print_components(ComponentsFinder.find(graph_randomized))
    print("Comparing graphs...")
    GraphVisualizer.draw_side_by_side(graph, graph_randomized)
    print("Visualization complete.")

def task_four():
    print("Task 4")
    n=6
    print(f"Creating random eulerian graph with {n} vertices ...")
    graph = RandomEulerianGraph(n).generate()
    print("Graph created successfully.")
    euler_cycle = EulerCycleFinder.find(graph)
    print("Euler cycle: ", end="")
    EulerCycleFinder.print_cycle(euler_cycle)
    print("Visualizing graph...")
    GraphVisualizer.draw(graph)
    print("Visualization complete.")
    print("Removing subsequent edges to show that euler cycle is correct...")
    for i in range(len(euler_cycle) - 1):
        graph.remove_edge(euler_cycle[i], euler_cycle[i + 1])
        GraphVisualizer.draw(graph)
    print("Visualization complete.")
    
    
def task_five():
    print("Task 5")
    n=7
    k=4
    print(f"Creating random regular graph with {n} vertices and {k} vertex degree ...")
    graph = RandomRegularGraph(n, k).generate()
    print("Graph created successfully.")
    print(f"Calculated vertex degrees: {[graph.vertex_degree(i) for i in range(graph.num_vertices)]}") 
    print("Visualizing graph...")
    GraphVisualizer.draw(graph)
    print("Visualization complete.")
    
def task_six():
    print("Task 6")
    n=10
    k=3
    print(f"Creating random regular graph with {n} vertices and {k} vertex degree ...")
    graph = RandomRegularGraph(n, k).generate()
    print("Graph created successfully.")
    hamiltonian_cycle = HamiltonianCycleFinder.find(graph)
    print("Hamiltonian cycle: ", end="")
    HamiltonianCycleFinder.print_cycle(hamiltonian_cycle)
    print("Visualizing graph...")
    GraphVisualizer.draw(graph)
    print("Visualization complete.")

def main() -> None:
    parser = argparse.ArgumentParser(description="Grafy-Lab02")
    parser.add_argument(
        "-t", "--task", type=int, required=True, help="Select Task (1-6)"
    )
    args = parser.parse_args()
    
    tasks = [task_one, task_two, task_three, task_four, task_five]
    if 1 <= args.task <= 5:
        tasks[args.task - 1]()
    else:
        print("Invalid task selected.")